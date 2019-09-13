# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np
import time 
import urllib.request  
import threading 
import math 
def pok(start,end): 
    
    for i in range(start,end):
        url ='https://assets.pokemon.com/assets/cms2/img/pokedex/detail/'+'{:03d}'.format(i)+'.png'
        request= urllib.request.Request(url)
        response=urllib.request.urlopen(request)
        binarystr=response.read()
        bytarray=bytearray(binarystr)
        numpyarray=np.asarray(bytarray,dtype="uint8")
        image=cv2.imdecode(numpyarray,cv2.IMREAD_UNCHANGED)
        cv2.imwrite("images/"+"{:03d}".format(i)+".png",image)
        print("saved")

threads=16
imgs=800
threadlist=[]

for i in range(threads):
    start=math.floor(i*imgs/threads)+1
    end=math.floor((i+1)*imgs/threads)+1
    threadlist.append(threading.Thread(target=pok,args=(start,end)))
    
for thread in threadlist:
    thread.start()
    
for thread in threadlist:
    thread.join()
    