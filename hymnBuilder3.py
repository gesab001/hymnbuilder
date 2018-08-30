import requests
"""
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
"""

response = requests.get("http://adventisthymns.com/numbers/")
hymnnumbers = str(response.content)
hymnnumbers = hymnnumbers.split('href="')
numbercategories = []
for hymn in hymnnumbers:
   if hymn.startswith("http://adventisthymns.com/numbers/"):
      split = hymn.split('" title="')
      numbercategories.append(split[0])

hymnlinks =  []
for value in numbercategories:
   response = requests.get(value)
   #print(response.status_code)
   hymntitles = str(response.content)    
   hymntitles = hymntitles.split('href="')
   for hymn in hymntitles:
      if hymn.startswith("http://adventisthymns.com/lyrics/"):
         hymn1 = hymn.split("&ndash;")
         hymn2 = hymn1[0].split('">')
         hymnlinks.append(hymn2[0])

print(len(hymnlinks))

