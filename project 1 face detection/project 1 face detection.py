#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2 as cv
import matplotlib.pyplot as plt
def rotate(img,angle,rot=None):
    (hight,width)=img.shape[:2]
    if rot is None:
        rot=(width//2,hight//2)
    rotmat=cv.getRotationMatrix2D(rot,angle,1.0)
    dimension=(width,hight)
    return cv.warpAffine(img,rotmat,dimension)
def videoReader(video):
    if video=='cam':
        return cv.VideoCapture(0)
    else:
        return cv.VideoCapture(video)
def resizeScreen(x,y):
    return cv.resize(frame,(x,y),interpolation=cv.INTER_CUBIC)
def playVideo(video):
    counter=0
    while True:
        isTrue,frame=video.read()
        if isTrue:
            counter+=1
            haar_cascade=cv.CascadeClassifier('haar_face.xml')
            faces_rect=haar_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=2)
            for(x,y,w,h)in faces_rect:
                cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
            cv.imshow('my Vid',frame)
            if cv.waitKey(1) & 0xFF==ord('d'):
                break
        else:
            break
def windowDestroy(capture):
    capture.release()
    cv.destroyAllWindows()


# In[7]:


capture=videoReader()
playVideo(capture)
windowDestroy(capture)


# In[ ]:




