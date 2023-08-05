'''
    - This file should contain APIs "function in class" that can deal with database

    - The two services are:
        1. Store DICOM image in database
        2. Search about an image with ID in database
'''

from PIL import Image
# import os, os.path
# import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# import numpy as np


# image = {id:path}
images={"1":"./images/ct.png",
        "2":"./images/ct (1).png",
        "3":"./images/ct (2).png",
        "4":"./images/ct (3).png",
        "5":"./images/ct (4).png",
        "6":"./images/ct (5).png",
        "7":"./images/ct (6).png",
        "8":"./images/ct (7).png",
        "9":"./images/ct (8).png",
        "10":"./images/mri (1).png",
        "11":"./images/mri (2).png",
        "12":"./images/mri (3).png",
        "13":"./images/mri (4).png",
        "14":"./images/mri (5).png",
        "15":"./images/mri (6).png",
        "16":"./images/mri (7).png",
        "17":"./images/mri (8).png",
        "18":"./images/mri (9).png",
        "19":"./images/mri (11).png",
        "20":"./images/us (1).png",
        "21":"./images/us (2).png",
        "22":"./images/x-ray (1).png",
        "23":"./images/x-ray (2).png",
        "24":"./images/x-ray (3).png",
        "25":"./images/x-ray (4).png",
        "26":"./images/x-ray (5).png",
        "27":"./images/x-ray (6).png",
        "28":"./images/x-ray (7).png",
        "29":"./images/x-ray (8).png",
        "30":"./images/x-ray (9).png",
        "31":"./images/x-ray (10).png",
        "32":"./images/x-ray (11).png",
        "33":"./images/x-ray (12).png",
        "34":"./images/x-ray (13).png",
        "35":"./images/x-ray (14).png",
        "36":"./images/x-ray (15).png",
        "37":"./images/x-ray (16).png",
        "38":"./images/x-ray (17).png",
        "39":"./images/x-ray (18).png",
        "40":"./images/x-ray (19).png",
        "41":"./images/x-ray (20).png",
        }
 
# search in database then return the path
def search(imageID):
    # search
    if imageID in list(images.keys()):
        # return the path
        return images[imageID]
    

    
# read image and return it as np.array 
def send_img_data (imageId):
    imagePath = search(imageId)
    if imagePath is None:
        return None
    return imagePath
    




# create a path and return it as a new path for storing 
# the new image
randomNumber = 0
def getPath():
    global randomNumber
    # get path
    path = "./images/"+str(randomNumber)+".png"
    randomNumber+=1
    lastID = list(images.keys())[-1]
    id = int(lastID) + 1
    images[str(id)] = path
    return path


