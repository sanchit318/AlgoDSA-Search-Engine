import io
import sys, numpy as np
import json
import math
# import Similarity.py
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

porter=PorterStemmer()
stop_words = set(stopwords.words('english'))

# print(stop_words)


dict1={}
dict={}

final_keywords_file=open("FinalKeywordsFile.txt","r")
line =final_keywords_file.read()
words=line.split()
tfidfQ_file = open("TFIDFQ.txt","w")
idf_file=open("IDF.txt","r")

total_keyword_cnt=0
mp={}#maps index to keyword
for r in words:
    dict[r]=0
    mp[total_keyword_cnt]=r
    total_keyword_cnt += 1
    # print(r)


line =idf_file.read()
words=line.split()
idf={}#key->idf_val
cnt=0
for r in words:
    idf[mp[cnt]]=float(r)
    cnt+=1

# print(cnt)

query_file=open("QueryString.txt","r")
line = query_file.read()
words = line.split()

# lines = sys.stdin.readlines()
# query=json.loads(lines[0])
# print(query)
# words=query.split()

wordcnt=0
for r in words:
    s=porter.stem(r)
    print(s)
    if s in dict:
        if s in dict1:
            dict1[s]+=1
        else:
            dict1[s]=1
        # print(s)
        wordcnt+=1 #cnt of occurences of keywords in the query string

# print(wordcnt)

tfidf={}
for key in dict:
    #key is already stemmed
    if key in dict1:
        tf_val = dict1[key] / wordcnt
    else:
        tf_val=0
    tfidf_val=tf_val*idf[key]
    tfidf[key] = round(tfidf_val, 5)
    tfidfQ_file.write(str(tfidf[key]) + " ")

# print("OK")
# exec(open("Similarity.py").read())


def similarity():

    # tfidfQ=open("TFIDFQ.txt","r")
    # line=tfidfQ.read()
    # words=line.split() ->I am facing problems using this as the file is not read properly

    v=[]
    v_magnitude=0
    for key in dict:
        val=tfidf[key]
        v.append(val)
        v_magnitude+=val*val
    # print("v.len= ",len(v))
    v_magnitude=math.sqrt(v_magnitude)

    arr=[]
    for i in range(1,690):
        mag=0
        numerator=0
        tfidf_file=open("/Users/HP/Desktop/Sanchit/node-test/TFIDF/TFIDF"+str(i)+".txt")
        line  =tfidf_file.read()
        words=line.split()
        cnt=0
        for r in words:
            val=float(r)
            mag+=val*val
            numerator+=v[cnt]*val
            cnt+=1
        mag=math.sqrt(mag)
        if v_magnitude!=0:
            val=numerator/(v_magnitude*mag)
        else:
            val=0
        arr.append(val)

    # print(len(arr))
    most_similar=[]
    index=-1
    for cnt in range(1,6):
        max_similarity = -1
        for i in range(0,689):
            if arr[i]>max_similarity:
                index=i
                max_similarity=arr[i]
        arr[index]=-1
        most_similar.append(index)

    urls_file=open("problem_urls.txt","r")

    line=urls_file.read()
    words=line.split()
    #one url will be one word

    urls=[]
    for r in words:
        urls.append(r)

    final_result=[]
    for i in range(1,6):
        final_result.append(urls[most_similar[i-1]])
        # print(urls[most_similar[i-1]])

    search_result=open("SearchResult.txt","w")
    for i in range(0,5):
        search_result.write(str(final_result[i])+"\n")

    return final_result

#Finding similarity
arr=similarity()
print(arr)
