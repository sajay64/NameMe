#!/usr/bin/env python
# coding: utf-8

# In[1]:


# A programme to test skill of user to identify the image
# For a tourister, this can be places or attractions like pisa, eiffle tower etc
# For kids, this can be images of dog, cat etc

import tkinter
import os
from tkinter import *
from PIL import ImageTk,Image

islate=Tk()
islate.title("Name Me!")
islate.bg="red"
islate.geometry("500x610")
ans=StringVar()
fileNum=1
fileList=[]
myfiles=[]
mylist=[]

def fetchFiles(): # to fill the list with images
    global fileList, myfiles,mylist
    validNames=[".jpg",".jpeg",".png",".gif",".bmp"] #consider only images with these extension
    fileList=os.listdir(".\images") # get files in images folder in the python root. alternatively a file dialog can be used to set this up
    for i in range(0,len(fileList)):
        for x in range(0,len(validNames)):
            if fileList[i].find(validNames[x])!=-1: #-1 means not found
                imgname=".\images"+"\\"  +  str(fileList[i])                
                img=Image.open(imgname)  # opening image
                img=img.resize((450,450), Image.LANCZOS) # resizing to suite our image box
                photoImg=ImageTk.PhotoImage(img) # assigning to photoimage
                mylist.append(str.upper(fileList[i].replace(validNames[x],""))) #this is answer list. answers are filenames without extension
                myfiles.append(photoImg) # filling a list with file names
    print(mylist)

def result(): #display result 
    global showAnswerlbl,ansbox,ans,mylist,fileNum
    showAnswerlbl.text=""  # clear current
    showAnswerlbl.grid_forget()
    ans1=str.upper(ansbox.get())
    if ans1==mylist[fileNum-1]: # comparing image name with list
        showAnswerlbl=Label(islate,text="Correct Answer",font=("Helvetica", 10), justify="center",fg="blue")
        showAnswerlbl.grid(row=6,column=2,ipadx=2)
    else:
        showAnswerlbl=Label(islate,text="In Correct",font=("Helvetica", 10), justify="center",fg="red")        
        showAnswerlbl.grid(row=6,column=2)
    showAnswerlbl.grid() #row=8,column=0
    ansbox.select_range(0,'end') # set focus so that easy to enter next text

def shownext(num):
    global fileNum,imgbox,myfiles,showAnswerlbl
    showAnswerlbl.text=""  # clear current
    showAnswerlbl.grid_forget()
    imgbox.grid_forget()
    fileNum+=num
    imgname=myfiles[fileNum-1]
    imgbox=Label(slate,text="Checking words",image=imgname)
    imgbox.grid(row=10,column=0)    
    shownpreviousbtn=Button(islate,text='<< Last Img',command=lambda :showprevious(1),state=NORMAL)
    shownpreviousbtn.grid(row=5,column=1) #C,columnspan=3
    if (fileNum)==len(myfiles):
        shownextbtn=Button(islate,text='Next Img >>',command=lambda :shownext(1),state=DISABLED)
        shownextbtn.grid(row=5,column=3) #,columnspan=3
        print("End of Files")
        return

def showprevious(num):
    global fileNum,imgbox,myfiles,showAnswerlbl
    showAnswerlbl.text=""  # clear current 
    showAnswerlbl.grid_forget()
    imgbox.grid_forget()
    fileNum-=num
    imgbox=Label(slate,text="Checking words",image=myfiles[fileNum-1])
    imgbox.grid(row=10,column=0)    
    shownextbtn=Button(islate,text='Next Img >>',command=lambda :shownext(1),state=NORMAL)
    shownextbtn.grid(row=5,column=3) #,columnspan=3
    if (fileNum)==1:
        shownpreviousbtn=Button(islate,text='<< Last Img',command=lambda :showprevious(1),state=DISABLED)
        shownpreviousbtn.grid(row=5,column=1) #C,columnspan=3
        return

slate=LabelFrame(islate,text="Type name of the Image in the box below and click check Result",padx=5,pady=1,fg="black")
slate.grid(row=0,column=0,padx=15,pady=20,columnspan=5)

fetchFiles() # Fill the images

imgname=myfiles[fileNum-1]
imgbox=Label(slate,text="IMAGE",image=imgname)
imgbox.grid(row=10,column=0)
sk=Button(islate,text="Check Result",command=result)
sk.grid(row=5,column=2)
shownextbtn=Button(islate,text='Next Img >>',command=lambda :shownext(1))
shownpreviousbtn=Button(islate,text='<< Last Img',command=lambda :showprevious(1),state=DISABLED)
shownextbtn.grid(row=5,column=3) #,columnspan=3
shownpreviousbtn.grid(row=5,column=1) #C,columnspan=3
showAnswerlbl=Label(islate,text="",font=("Helvetica", 10), justify="center",fg="blue")
showAnswerlbl.grid(row=6,column=2,ipadx=2)
ansbox=Entry(slate,textvariable=ans,font="Arial 20 bold", justify="center",bd=2)
ansbox.grid(row=40,column=0)
ansbox.focus()

islate.mainloop()


# In[ ]:





# In[ ]:




