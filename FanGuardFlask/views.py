from __future__ import division
from flask import render_template
from FanGuardFlask import app
import pandas as pd
import pytumblr
import MySQLdb as mdb
import time 
import request
from flask import request

from WebModel import ModelIt
import cleaners
import postGather

#Intro page:
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

#Output page:
@app.route('/output')#,methods=['POST'])
def blogcheck_output():

    #List of available properties
    prod_key = {
        "sw": "Star Wars",
        "aou": "Age of Ultron",
        "madmax": "Mad Max",
        "dai": "Dragon Age Inquisition",
        "lis": "Life is Strange",
        "utale": "Undertale",
        "han": "Hannibal",
        "slock": "Sherlock",
        "got": "Game of Thrones"
    }

    #Star Wars is the default:
    default_name = "star-wars"
    default_options = "cut80"
        
    #pull 'state' from input field and store it
    name = request.args.get('tag_name')
    options = request.args.get('options')
    ipname = request.args.get('IPname')

    #Defaults:
    if not name:
        name = default_name
    if not options:
        options = default_options
        
    #Configurations:
    myconfig = "/home/ubuntu/WebApp/Web/FanGuardFlask/myconfigs.cfg"
    df = postGather.FrontendGetPosts(name,40,myconfig)
    #df = postGather.GetDashPosts(myconfig)
    print "Done gathering"

    #The prediction:
    pred = ModelIt(ipname,options,df,myconfig)

    #The proper name of the filter
    iptitle = prod_key[ipname]

    #Turn the prediction into a usable product:
    sum_pred = 0
    blog_posts = []
    for i in range(0, df.shape[0]):
        bname = df.iloc[i]['blog_name']
        myid = df.iloc[i]['id']
        mytime=df.iloc[i]['date']

        if pred[i][0] == 1:
            prob="Yes"
            sum_pred += 1
        else:
            prob="No"
        
        mytags=df.iloc[i]['taglist']
        mytext=df.iloc[i]['words']

        has_spoil="No"
        if "spoil" in mytext:
            has_spoil = "Yes"
        if "spoil" in mytags:
            has_spoil = "Yes"
                    
        myurl=df.iloc[i]['short_url']

        stime = time.strptime(mytime, "%Y-%m-%d %H:%M:%S %Z")
        postday = "%d/%d/%d" % (stime.tm_mon,stime.tm_mday,stime.tm_year ) 

        blog_posts.append(dict(text=mytext, myid=myid, time=postday, \
                            prob=prob,tags=mytags,author=bname,myurl=myurl, \
                            has_spoil = has_spoil))
                           

    #Proportion of spoilers:
    spoperc = int((100.0*sum_pred)/df.shape[0])

    #Send it to the template:
    return render_template("output.html", blog_name = name, blog_posts = blog_posts, spoiler_perc = spoperc,num=df.shape[0], iptitle = iptitle)
