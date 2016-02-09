import numpy as np
import pickle
import MySQLdb as mdb
import pandas as pd

from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

import modelmaker

import ConfigParser

def GetPred(df,v1,v2):
    
    #Word list::
    corpus_train1 = df['words']
    x1 = v1.transform(corpus_train1).toarray()

    #Tag list:
    corpus_train2 = df['taglist']
    x2 = v2.transform(corpus_train2).toarray()

    norm1 = np.zeros(x1.shape[0])
    for i,x in enumerate(x1):
        norm1[i] = np.linalg.norm(x)

    norm2 = np.zeros(x1.shape[0])
    for i,x in enumerate(x2):
        norm2[i] = (np.linalg.norm(x))
        
    norm1 = norm1.reshape(len(norm1),1)
    norm2 = norm2.reshape(len(norm2),1)
    
    results = ((norm1 > 5) | (norm2 > 1))
    
    return results


def GetSFModel(name,con,path,cut):

    sql_query = 'SELECT * FROM sfilterMeta WHERE name="%s"' % name
    
    query_results=pd.read_sql(sql_query,con)

    fmodel = "%s/%s" % (path,query_results['mf'][0])
    fv1 = "%s/%s" % (path,query_results['v1f'][0])
    fv2 = "%s/%s" % (path,query_results['v2f'][0])

    cutval = query_results[cut][0]
    
    with open(fmodel, 'rb') as fid:
        model = pickle.load(fid)
    with open(fv1, 'rb') as fid:
        v1 = pickle.load(fid)
    with open(fv2, 'rb') as fid:
        v2 = pickle.load(fid)       

    return model, v1, v2, cutval

def GetPFModel(name,con,path):

    sql_query = 'SELECT * FROM pfilterMeta WHERE name="%s"' % name
    
    query_results=pd.read_sql(sql_query,con)

    fv1 = "%s/%s" % (path,query_results['v1p'][0])
    fv2 = "%s/%s" % (path,query_results['v2p'][0])

    cutval = query_results['cut_pre'][0]
    
    with open(fv1, 'rb') as fid:
        v1 = pickle.load(fid)
    with open(fv2, 'rb') as fid:
        v2 = pickle.load(fid)       

    return v1, v2, cutval

def ModelIt(name,cut,df,myconfig):

    config = ConfigParser.RawConfigParser()
    config.read(myconfig)

    #MySQL info:                                                                                                                                                               
    db_username = config.get('DB', 'username')
    db_pwd = config.get('DB', 'pwd')

    #Database connection:
    con = mdb.connect('localhost', db_username, db_pwd, 'InsightPaths')
    path = "/home/ubuntu/WebApp/Web/FanGuardFlask/files"

    #Prefilter Models:
    vp1,vp2,pcutval = GetPFModel(name,con,path)
    c0 = GetPred(df,vp1,vp2)
    #p0 = pmodel.predict_proba(Xp0)[:,1]

    #Spoiler Filter Models:   
    smodel,vs1,vs2,scutval = GetSFModel(name,con,path,cut)
    p1 = modelmaker.model_tester(df,smodel,vs1,vs2)

    #c0 = (p0>pcutval).astype(int)
    #c0 = c0.reshape(c0.shape[0],1)
    
    c1 = (p1>scutval).astype(int)
    c1 = c1.reshape(c1.shape[0],1)

    return c0*c1
