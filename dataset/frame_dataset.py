import sys
sys.path.insert(0, '..')

import os
import h5py
import numpy as np
import torch.utils.data as data

from config.paths import Path

class FrameDataset(data.Dataset):
    def __init__(self, num_sec):
        dataset_path = Path.DATA_HOME+Path.FRAME_FEATURES_DATASET.format(sec=num_sec)
        dataset_file = h5py.File(dataset_path, 'r')
        self.frames = dataset_file['frames']
        
    def __getitem__(self, i):
        return self.frames[i]
    
    def __len__(self):
        return self.frames.shape[0]