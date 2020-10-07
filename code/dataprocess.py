import os
import json
import logging
import skimage.io

text_filepath = '../data/tc-corpus-answer/answer/'
image_filepath = '../data/newdata/'

def processtext(datapath=text_filepath):
    logger = logging.getLogger(name='Multimodal')
    logger.setLevel(logging.DEBUG)
    for file in os.listdir(datapath):
        print(file)
        for text in os.listdir(datapath+file+'/'):
            finaltext = datapath+file+'/'+text
            with open(finaltext , 'r',encoding='gb18030', errors='ignore') as textfile:
                for i in textfile:
                    print(i)

processtext()



def processimage(datapath = image_filepath):
    file_path = datapath + '/*.jpg'
    print('Start process imagedata:' + file_path)
    datasets = skimage.io.ImageCollection(file_path)  # 加载图片数据集
    print('The image process is over' + file_path)
    return datasets
