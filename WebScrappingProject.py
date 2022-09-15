from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pymysql as pq
import tkinter as tk
import pywebcopy
from pywebcopy import save_webpage
from tkinter import messagebox
from builtwith import builtwith
import csv


app = tk.Tk()

Website_URL = tk.StringVar()
Website_Folder_Name = tk.StringVar()


label_Programming_Language = tk.Label(text="Programming Language:- ", bg="lightblue")
label_Programming_Language.grid(row=26,column=0)
label_Programming_Language_val = tk.Label(text="N/A", bg="lightblue")
label_Programming_Language_val.grid(row=26,column=1)


label_Web_Servers = tk.Label(text="Web Server:- ", bg="lightblue")
label_Web_Servers.grid(row=27,column=0)
label_Web_Servers_val = tk.Label(text="N/A", bg="lightblue")
label_Web_Servers_val.grid(row=27,column=1)


label_Font_Scripts = tk.Label(text="Font Scripts:- ", bg="lightblue")
label_Font_Scripts.grid(row=28,column=0)
label_Font_Scripts_val = tk.Label(text="N/A", bg="lightblue")
label_Font_Scripts_val.grid(row=28,column=1)


label_Web_Frameworks = tk.Label(text="Web Frameworks:- ", bg="lightblue")
label_Web_Frameworks.grid(row=29,column=0)
label_Web_Frameworks_val = tk.Label(text="N/A", bg="lightblue")
label_Web_Frameworks_val.grid(row=29,column=1)


label_Javascript_Frameworks = tk.Label(text="Javascript Frameworks:- ", bg="lightblue")
label_Javascript_Frameworks.grid(row=30,column=0)
label_Javascript_Frameworks_val = tk.Label(text="N/A", bg="lightblue")
label_Javascript_Frameworks_val.grid(row=30,column=1)


label_Website_URL = tk.Label(text="Enter Website URL", bg="lightblue")
label_Website_URL.grid(row=0,column=0)
text_Website_URL = tk.Entry(textvariable=Website_URL)
text_Website_URL.grid(row=0,column=1)


label_Website_Folder = tk.Label(text="Enter Website Folder Name", bg="lightblue")
label_Website_Folder.grid(row=2,column=0)
text_Website_Folder = tk.Entry(textvariable=Website_Folder_Name)
text_Website_Folder.grid(row=2,column=1)


def kill_app():
    
    kill_app = messagebox.askokcancel("Quit","Do You Want To Quit")
    
    if kill_app is True :
       app.destroy()
    
    else:
        messagebox.showinfo('Return','You will now return to the application screen')


def downloadWebSite():
    kwargs2 = {
    'url' : Website_URL.get(),
    'project_folder' : 'D:/DownloadWebSites/',
    'project_name' : Website_Folder_Name.get(),
    'bypass_robots' : True
    }
    
    pywebcopy.save_website(**kwargs2)

def clearscreen():
    Website_URL.set("")
    Website_Folder_Name.set("")
    label_Programming_Language_val.config(text = "N/A")
    label_Web_Servers_val.config(text = "N/A")
    label_Font_Scripts_val.config(text = "N/A")
    label_Javascript_Frameworks_val.config(text = "N/A")
    label_Web_Frameworks_val.config(text = "N/A")


def getWebsiteInfo():
    Q = builtwith(Website_URL.get())
    label_Programming_Language_val.config(text = Q['programming-languages'])
    label_Web_Servers_val.config(text = Q['web-servers'])
    label_Font_Scripts_val.config(text = Q['font-scripts'])
    label_Javascript_Frameworks_val.config(text = Q['javascript-frameworks'])
    label_Web_Frameworks_val.config(text = Q['web-frameworks'])


def saveWebsiteInfo():
    f=open(r'C:\Users\ivanb\OneDrive\Desktop\Web Scrapping files\WebsiteInfo.csv','a+', newline="")
    Q = builtwith(Website_URL.get())
    Q['Website URL'] = Website_URL.get()
    # data=""
    # for i in range(0,len(Q['programming-languages'])):
	#     for j in Q.keys():
	# 	    data+=str(Q[j][i])
	# 	    data+=(",")
	# 	    data.split(",")
	#     data+=("\n")
    # f.write(data)
    list1 = []
    def getList(dict):
        
        for key in Q.keys():
            list1.append(key)
          
        return list1

    with f:
        header = ['programming-languages', 'web-servers', 'web-server-extensions', 'font-scripts', 'web-frameworks', 'javascript-frameworks', 'Website URL']
        Q_List = []
        getList(Q)
        for i in range(len(header)):
            if(header[i] not in list1):
                Q[header[i]] = "N/A"

        for i in range(len(header)):
	        Q_List.append(Q[header[i]])

        for i in range(len(Q_List)-1):
            Q_List[i]=Q_List[i][0]

        Q_List_1 = [Q_List]
        writer = csv.writer(f)
        writer.writerows(Q_List_1)
    f.close()


app.geometry('927x320')
app.configure(bg="LightBlue")
app.title("Web Scrapping Project")


URL=tk.Label(font=("Times", 33, "bold"),text="Enter URL")



Programming_Language = tk.StringVar()
Web_Servers = tk.StringVar()
Font_Scripts = tk.StringVar()
Web_Frameworks = tk.StringVar()
Javascript_Frameworks = tk.StringVar()


B1 = tk.Button(app, text = "Download Website", command = downloadWebSite, width=25)
B2 = tk.Button(app, text = "Get Details", command = getWebsiteInfo, width=25)
B3 = tk.Button(app, text = "Save To CSV ", command=saveWebsiteInfo, width=25)
B4 = tk.Button(app, text = "Reset", command =clearscreen, width=25)
B5 = tk.Button(app, text = "Exit", command=kill_app, width=25)

B1.grid(row=7,column=0)
B2.grid(row=7,column=1)
B3.grid(row=7,column=2)
B4.grid(row=7,column=3)
B5.grid(row=7,column=4)

app.mainloop()





#Websites to Scrap
#https://opentender.eu/
#https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid
#https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid
