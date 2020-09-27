# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:19:16 2020

@author: ADITYA THAKAR
"""
import PyPDF2
import pyttsx3
import os
books=[]
reader=pyttsx3.init()
reader.say("welcome to a mini library, we have the following books here.")
reader.runAndWait()

def choice():
    for main,sub,file in os.walk("library"):
        for i in range(0,len(file)):
             reader.say(str(i+1)+file[i])
             reader.runAndWait()
             books.append(file[i])
    
    
    reader.say("Enter your choice by using the index number")
    reader.runAndWait()  
        
    while True:
        try:
            
            n=int(input("Enter your choice: "))
        except:
            reader.say("please enter avalid input")
            reader.runAndWait()
        else:
            break
            
    return n
    

num=choice()
   

f=open("library/"+books[num-1],"rb")
reader_obj=PyPDF2.PdfFileReader(f)
reader.say(f"the above book has {reader_obj.numPages} pages. Please enter the range of pages you would like to read.")
reader.runAndWait()
start= int(input("Start: "))
end= int(input("End: "))
for k in range(start-1,end-1):
    reader.say(reader_obj.getPage(k).extractText())
    reader.runAndWait()
f.close()
    
reader.say("Thank you")  
reader.runAndWait()     
 






