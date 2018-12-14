import sys
sys.path.insert(0, '..')

import os
import h5py
import numpy as np
import torch.utils.data as data

from config.paths import Path

class LabeledDataset(data.Dataset):
	def __init__(self, num_sec, data_type, split):
		dataset_path = Path.DATA_HOME+Path.LABELED_DATASET.format(sec=num_sec, split=split, type=data_type)
		dataset_file = h5py.File(dataset_path, 'r')
		self.frames = dataset_file['frames']
		self.annotations = dataset_file['annotations']

	def __getitem__(self, i):
		return self.frames[i], self.annotations[i].astype(int)

	def __len__(self):
		return self.frames.shape[0]