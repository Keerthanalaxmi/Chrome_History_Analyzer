import os
import urllib.parse
import sqlite3
history=os.path.join(r<PATH>, 'history')
conn = sqlite3.connect(history)
curs=conn.cursor()
curs_out=curs.execute('select url,visit_count from urls')
url_count={}
for row in curs_out:
        url=urllib.parse.urlparse(row[0]).netloc
        if url in url_count.keys():
                url_count[url]+=row[1]
        else:
                url_count[url]=row[1]

new_sorted_url_count=sorted(url_count.items(),key=lambda e :e[1],reverse=True)
print("The top 10 Most visited Websites in Chrome")
print("##########################################")
for i in new_sorted_url_count[0:10]:
	print(i[0],i[1])
print("##########################################")
	
