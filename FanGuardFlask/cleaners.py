from bs4 import BeautifulSoup  
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def make_text(x,wtitle=True):
    
    tot_txt = ""
    
    if x['type'] == 'text':    
        if wtitle:
            if x['title']:
                tot_txt += x['title']
            if x['body']:
                tot_txt += x['body']
        elif x['body']:
            tot_txt += x['body']
    elif x['type'] == 'photo':
        if wtitle:
            if x['title']:
                tot_txt += x['title']
            if x['caption']:
                tot_txt += x['caption']
        elif x['caption']:
            tot_txt += x['caption']
    elif x['type'] == 'answer':
        if x['question']:
            tot_txt += x['question']
        if x['answer']:
            tot_txt += x['answer']
    elif x['type'] == 'chat':
        tot_txt =""

    soup = BeautifulSoup(tot_txt,'html')
        
    return soup.get_text()

def cleaner(x,wtitle=True):

    post_txt=make_text(x,wtitle)

    # Use regular expressions to do a find-and-replace
    letters_only = re.sub("[^a-zA-Z]"," ", post_txt )  # The text to search
        
    lower_case = letters_only.lower()        # Convert to lower case

    words = lower_case.split(" ")
    str_return=""
    
    wnl = WordNetLemmatizer()
    
    for w in words:
        if (len(w) > 1) and (w not in stopwords.words("english")):
            str_return += wnl.lemmatize(w)
            str_return += " "
    
    return str_return.encode('ascii')

def count(x):
       
    post_txt=make_text(x)

    count = len(re.findall(r'\w+', post_txt))
    return count

def gather_tags(x):
    
    tag_txt = ""
    
    for t in x['tags']:
        t = re.sub("[^a-zA-Z ]","", t )
        t = t.lower()  
        words = t.split(" ")
        str_return=""
        wnl = WordNetLemmatizer()
    
        for w in words:
            if (len(w) > 1) and (w not in stopwords.words("english")):
                str_return += wnl.lemmatize(w)
                str_return += " "   

        tag_txt += '"%s",' % str_return
    return tag_txt.encode('ascii')
