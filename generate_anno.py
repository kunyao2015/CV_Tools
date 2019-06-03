import os
import shutil
from imutils import paths
base_dir = '/home/yaokun/datasets/cars/ccpd/ccpd_dataset/plate'
train_dir = '/home/yaokun/datasets/cars/ccpd/ccpd_dataset/plate/train'
test_dir = '/home/yaokun/datasets/cars/ccpd/ccpd_dataset/plate/test'
infer_dir = '/home/yaokun/datasets/cars/ccpd/ccpd_dataset/plate/infer'
trainimg_paths = []
testimg_paths = []
inferimg_paths = []
trainimg_paths += [el for el in paths.list_images(train_dir)]
testimg_paths += [el for el in paths.list_images(test_dir)]
inferimg_paths += [el for el in paths.list_images(infer_dir)]


    
  

with open(os.path.join(base_dir, 'train_annotation'), 'w') as f:
    for img in trainimg_paths:
        pic_name = os.path.basename(img).strip()
        label = pic_name.rsplit('.',1)[0]
        f.write(os.path.join(train_dir, pic_name) + ' ' + label + '\n')

with open(os.path.join(base_dir, 'val_annotation'), 'w') as f:
    for img in testimg_paths:
        pic_name = os.path.basename(img).strip()
        label = pic_name.rsplit('.',1)[0]
        f.write(os.path.join(test_dir, pic_name) + ' ' + label + '\n')

with open(os.path.join(base_dir, 'infer_annotation'), 'w') as f:
    for img in inferimg_paths:
        pic_name = os.path.basename(img).strip()
        label = pic_name.rsplit('.',1)[0]
        f.write(os.path.join(infer_dir, pic_name) + '\n')       