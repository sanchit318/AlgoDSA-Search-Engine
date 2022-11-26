import math
tfidfQ=open("TFIDFQ.txt","r")
line=tfidfQ.read()
words=line.split()

v=[]
v_magnitude=0
for r in words:
    val=float(r)
    v.append(val)
    v_magnitude+=val*val

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

print(final_result)
