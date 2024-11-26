'''import numpy as np
import pandas as pd'''
#import matplotlib.pyplot as plt
#everything is installed inside the venv. verified by using an echo command in basj terminal
import torchvision
from torchvision import resnet50, Resnet50_Weights

import torch #giving a traeeback i have no idea why
import time
import os
import cv2
#learing the ropes of transfer learning in torch
'''image_transforms = {
    'train' : transforms.Compose([
        transforms.RandomResizedCrop(size=256, scale =(0.8,1.0)),
        transforms.RandomRotation(degrees=15),
        transform.RandomHorizontalFlip(),


    ])
}'''

#reading in the alexnet model
'''alexnet = models.alexnet(pretrained = True) #downloads the weights for the network
print(alexnet)
'''




#Data Preparation
#DSRiDdata = pd.read_csv("DS_IDRID.csv") #need to learn how to read in images using pandas
DR = []
NonDR = []
#print(dir(models))
#print('alexnet' in dir(models))

#0 is NonDR, 3 and 4 is DR

'''
#
'''
