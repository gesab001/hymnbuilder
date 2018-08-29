#!/usr/bin/python3
import os
import sqlite3

def addHymn(number, title, verses):
        conn = sqlite3.connect('hymn1.db')
        conn.execute("INSERT INTO HYMNS (NUMBER, TITLE, VERSES) VALUES(?, ?, ?)", (number, title, verses));
        conn.commit()
        print (number + " " + str(title) + "  added successfully");
        conn.close()    


aBook = open("HymnWords.txt", "r")
lines = aBook.read()
lines = lines.split("\n"*13)
lines = [line.strip('\n') for line in lines]
lines = [line.strip(" ") for line in lines]
#filter(None,list)
#lines = [lines.remove(line) for line in lines if line=='']
#print (lines)

for line in lines:
  if line!='': 
    titleAndVerse = line.split("\n"*3)
    if len(titleAndVerse)>1:
      numberAndTitle = titleAndVerse[0].split("  ")
      number = numberAndTitle[0]
      title =  numberAndTitle[2]
      if title=="":
         title=numberAndTitle[3]
      verses = titleAndVerse[1]
      addHymn(number, title, verses)

