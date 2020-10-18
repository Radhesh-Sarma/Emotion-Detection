
import os,cv2
import numpy as np
data_path = 'dataset/CK+'
data_dir_list = os.listdir(data_path)
print(data_dir_list)


img_rows=256
img_cols=256
num_channel=1

num_epoch=10

img_data_list=[]

try:
    for dataset in data_dir_list:
        # print(dataset)
        img_list=os.listdir(data_path+'/'+ dataset)
        # print(img_list)
        print ('Loaded the images of dataset-'+'{}\n'.format(dataset))
        for img in img_list:
            # print(img)
            input_img=cv2.imread(data_path + '/'+ dataset + '/'+ img )
            #input_img=cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
            # print(input_img)
            input_img_resize=cv2.resize(input_img,(48,48))
            img_data_list.append(input_img_resize)
except Exception as e:
    print(str(e))

img_data = np.array(img_data_list)
img_data = img_data.astype('float32')
img_data = img_data/255

print(img_data.shape)


num_classes = 7

num_of_samples = img_data.shape[0]
labels = np.ones((num_of_samples,),dtype='int64')

labels[0:134]=7 
labels[135:188]=7 
labels[189:365]=7 
labels[366:440]=7 
labels[441:647]=7 
labels[648:731]=5 
labels[732:980]=7 

names = ['anger','contempt','disgust','fear','happy','sadness','surprise','all others']

def getLabel(id):
    return ['anger','contempt','disgust','fear','happy','sadness','surprise','all others'][id]