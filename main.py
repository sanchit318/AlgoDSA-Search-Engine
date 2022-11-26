import io
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
porter=PorterStemmer()

# word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))

dict={}
keywords_file=open("KeywordsFile.txt","r")
final_keywords_file=open("FinalKeywordsFile.txt",'w')

#Stemming the keywords file and storing the stemmed keywords in the dictionary
line = keywords_file.read()
words = line.split()
for r in words:
	s=porter.stem(r)
	dict[s]=0

#storing the stemmed keywords in the new file *FinalKeywordsFile.txt*
for key in dict:
	final_keywords_file.write(str(key)+" ")

#filteredtexts are the documents that don't contain the stopwords.. they are not stemmed!!
for i in range(1,690):
	file = open("filteredtext"+str(i)+".txt")
	# Use this to read file content as a stream:
	line = file.read()
	words = line.split()
	dict1={}
	for r in words:
		dict1[porter.stem(r)]=1
	for key in dict1:
		dict[key]+=1
#dict[key] = number of documents that contain that key

# 		keywords_file.write(" "+r)
# keywords_file.close()
# keywordMap_file=open("KeywordMapFile.txt",'a')
# for key in dict:
# 	keywordMap_file.write(key+" "+str(dict[key])+"\n")
# print(dict.keys())


idf_file=open("IDF.txt",'w')
N=len(dict)
idf={}
for key in dict:
	idf[key]=round(math.log(N/dict[key],10),5)
	idf_file.write(str(idf[key])+" ")




for i in range(1,690):
	dict2 = {}
	file = open("filteredtext" + str(i) + ".txt")
	# Use this to read file content as a stream:
	line = file.read()
	words = line.split()
	wordcnt=0;
	for r in words:
		if porter.stem(r) in dict2:
			dict2[porter.stem(r)]+=1
		else:
			dict2[porter.stem(r)]=1
		wordcnt+=1
	tfidf_file = open("TFIDF"+str(i)+".txt", 'w')
	tfidf = {}
	for key in dict:
		if key in dict2:
			tfidf[key]=idf[key]*(dict2[key]/wordcnt)
		else:
			tfidf[key]=0
		tfidf[key]=round(tfidf[key],5)
		tfidf_file.write(str(tfidf[key])+" ")

print("OK!")
