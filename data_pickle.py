#Environment set-up and libraries

#Base libraries
import numpy as np
import random
import torch
from torchnet.dataset import TensorDataset
#Plotting libraries
# %matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

import plotly
import plotly.graph_objects as go

#Utilities libraries
from glob import glob 
import os

import pickle

# We create a function that load and normalize a point cloud tile
def cloud_loader(tile_name, features_used):
  print(tile_name.split('/')[-1])
  tile_name = '/scratch/gilbreth/makkarn/project/train/train/'+tile_name.split('/')[-1]
  # tile_name = '/scratch/gilbreth/makkarn/project/test/test/'+tile_name.split('/')[-1]
  print(features_used)
  cloud_data = np.loadtxt(tile_name).transpose()

  min_f=np.min(cloud_data,axis=1)
  mean_f=np.mean(cloud_data,axis=1)

  features=[]
  if 'xyz' in features_used:
    n_coords = cloud_data[0:3]
    n_coords[0] -= mean_f[0]
    n_coords[1] -= mean_f[1]
    n_coords[2] -= min_f[2]
    features.append(n_coords)
  if 'rgb' in features_used:
    colors = cloud_data[3:6]/255
    features.append(colors)
  if 'i' in features_used:
    # n_intensity = cloud_data[-2] - min_f[-2]
    IQR = np.quantile(cloud_data[-2],0.75)-np.quantile(cloud_data[-2],0.25)
    n_intensity = ((cloud_data[-2] - np.median(cloud_data[-2])) / IQR)
    n_intensity -= np.min(n_intensity)
    # intensity[np .where(intensity > 5000)]=5000
    features.append(n_intensity)
  
  gt = cloud_data[-1]
  gt = torch.from_numpy(gt).long()
  cloud_data = torch.from_numpy(np.vstack(features))
  return cloud_data, gt

f = open('data_prepared.pckl', 'rb')
test_list_t, test_set_t, train_list_t, train_set_t, valid_list_t, valid_set_t = pickle.load(f)
# print(test_list_t)
print(test_set_t, len(test_set_t))
# print(train_list_t)
print(train_set_t, len(train_set_t))
# print(valid_list_t)
print(valid_set_t, len(valid_set_t))

# Paths to the text files
# data_file_path = "train.pts"
# labels_file_path = "train.seg"
# data_file_path = "test.pts"
# labels_file_path = "test.seg"
data_file_path = "val.pts"
labels_file_path = "val.seg"

with open(data_file_path, "w") as data_file, open(labels_file_path, "w") as labels_file:
  # for i in range(len(train_set_t)):
  # for i in range(len(test_set_t)):
  for i in range(len(valid_set_t)):
      # sample = train_set_t[i]
      # sample = test_set_t[i]
      sample = valid_set_t[i]
      print(f"Sample {i}: {sample[0]}, {sample[1]}")
      print('.................................',sample[0].shape, sample[1].shape,'...................')
      sample_0 = sample[0].t() 
      print(np.unique(sample[1]))
      for i,j in zip(sample_0, sample[1]):
        print(i.numpy()[:], j)
        data_file.write(' '.join(map(str, i.numpy())) + '\n')  # Write row to data file with newline
        labels_file.write(str(j.numpy()) + '\n')  # Write label to labels file with newline