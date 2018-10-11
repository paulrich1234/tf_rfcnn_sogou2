import cv2
import os
filelist=os.listdir('type2_train')
for name in filelist:
    img=cv2.imread('type2_train/'+name)
    img2=cv2.resize(img,(520,212),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('type2_train/'+name,img2)
