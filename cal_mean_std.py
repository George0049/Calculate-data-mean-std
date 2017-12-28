#!/usr/bin/env python
#coding=utf-8
import numpy as np
from PIL import Image       
import os

# compute a dir mean and std

all_file_name = '/home/flykin/catkin_ws/src/Dexnet_source/data/rawdataset/adv_synth/'

file_name = os.listdir(all_file_name)
file_name.sort(key = lambda x: (x[-9:-4]))

file_name = [f for f in file_name if f.find('depth_ims_tf_table_')>-1]

print 'file_num :',len(file_name)
print file_name[189]


file_name_copy = file_name

# data mean
print '----------Computing data mean-----------'
data_mean = 0.
num_sum = 0.

for k in range(len(file_name_copy)):
	data_filename = file_name_copy[k]
	data = np.load (os.path.join('/home/flykin/catkin_ws/src/Dexnet_source/data/rawdataset/adv_synth',data_filename))['arr_0']
	data_mean += np.sum(data[:,:,:,:])
	num_sum += data.shape[0]*data.shape[1]*data.shape[2]
	# print data.shape[0],data.shape[1],data.shape[2]
	# print k
# data_mean = data_mean/(190*1000*32*32)
# print num_sum
data_mean = data_mean/num_sum
print 'data_mean: ',data_mean
np.save('./mean.npy',data_mean)

#data std
print '----------Computing data std------------'
data_std = 0.
# num_sum = 0.

for k in range(len(file_name_copy)):
	data_filename = file_name_copy[k]
	data = np.load(os.path.join('/home/flykin/catkin_ws/src/Dexnet_source/data/rawdataset/adv_synth',data_filename))['arr_0']
	data_std += np.sum((data[:,:,:,:]-data_mean)**2)
	# num_sum += data.shape[0]*data.shape[1]*data.shape[2]
data_std = np.sqrt(data_std/num_sum) 
print 'data_std: ',data_std
np.save('./std.npy',data_std)


#load .npy

mean = np.load('./mean.npy')
std = np.load('./std.npy')
print 'mean = ',mean
print 'std = ',std
