import cv2
import os
filelist=os.listdir('/home/zhaowei/workspace/backup_zhaowei/tf_rfcnc3/data/demo')
for name in filelist:
    img=cv2.imread('/home/zhaowei/workspace/backup_zhaowei/tf_rfcnc3/data/demo/'+name)
    img2=cv2.resize(img,(520,212),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('/home/zhaowei/workspace/backup_zhaowei/tf_rfcnc3/data/demo/'+name,img2)
