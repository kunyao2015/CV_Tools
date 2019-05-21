import numpy as np
import skimage
from skimage import io
import glob
import argparse

def main(args):
    img_channel = 3
    img_names = glob.glob('{}/*.jpg'.format(args.input))
    img_num = len(img_names)
    print('image num: {}'.format(img_num))

    height_sum = 0
    width_sum = 0
    pixel_sum = 0
    channel_sum = np.zeros(img_channel)
    channel_sum_squared = np.zeros(img_channel)

    for img_name in img_names:
        img = io.imread(img_name)
        img = skimage.img_as_float32(img)
        height_sum += img.shape[0]
        width_sum += img.shape[1]
        pixel_sum += img.size / img_channel
        channel_sum += np.sum(img, axis=(0, 1))
        channel_sum_squared += np.sum(np.square(img), axis=(0, 1))
    
    mean = channel_sum / pixel_sum
    std = np.sqrt(channel_sum_squared / pixel_sum - np.square(mean))

    height_avg = height_sum / img_num
    width_avg = width_sum / img_num

    print('height: {}, width: {}'.format(height_avg, width_avg))
    print('mean: {}'.format(mean))
    print('std: {}'.format(std))

def parse_args():
    '''Parse input arguments.'''
    parser = argparse.ArgumentParser(description='Compute image dataset mean and std')
    parser.add_argument('--input', type=str, default=None,
                        help='train dataset path')
    parser.add_argument('--output', type=str, default=None,
                        help='valuate dataset path')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main(parse_args())