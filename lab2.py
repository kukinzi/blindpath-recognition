import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import ndimage
import torch
import torchvision
import imageio

#1
def cal1(i):
    i1=ndimage.uniform_filter(i,size=10)
    return i1
#2
def cal(i,s):
    x,y,z = i.shape
    res=np.zeros_like(i,dtype=np.float32)
    for a in range(x):
        for b in range(y):
            for c in range(z):
                res[a,b,c]=np.mean(i[a:a+s,b:b+s,c])
    return np.clip(res,0,255).astype(np.uint8)
def main():
    i=imageio.v2.imread('test1.jpg',pilmode='RGB')
    s=int(input())
    plt.imshow(cal(i,s))
    plt.title("Press any key to close")
    plt.waitforbuttonpress()
    plt.close() 
if __name__ == "__main__":
    main()







