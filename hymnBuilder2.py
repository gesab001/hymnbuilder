import requests
response = requests.get('http://sdahymnals.com/Hymnal/')
#print(response.status_code)
hymntitles = str(response.content)
hymntitles = hymntitles.split('href="')
print(len(hymntitles))
hymnlinks = []
for hymn in hymntitles:
   if hymn.startswith("http://sdahymnals.com/Hymnal/"):
      hymn = hymn.split("</a>")
      hymn2 = hymn[0]
      hymn3 = hymn2.split('">')
      if hymn3[0].endswith("/"):
         hymnlinks.append(hymn3[0])

print (len(hymnlinks))

print (hymnlinks[0])

response = requests.get(hymnlinks[0])
#print(response.status_code)
hymn = str(response.content)    
print(hymn)

