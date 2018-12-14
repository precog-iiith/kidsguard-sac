from abc import ABC, abstractmethod

import time
import h5py
import numpy as np
 
class BaseLogger(ABC):
 
    def __init__(self, batch_size, print_every, data_len):
        self.print_every = print_every
        self.batch_size = batch_size
        self.data_len = data_len
        self.start_time = time.time()
        self.flush()
        super().__init__()

    def to_numpy(self, tensor):
        return tensor.data.cpu().numpy()
    
    def time_since(self):
        now = time.time()
        diff = now - self.start_time
        m, s = divmod(diff, 60)
        h, m = divmod(m, 60)
        return '%d:%02d:%02d' % (h, m, s)

    def save_dataset(self, f, metric, dataset_name, dtype, shape_tuple):
        np_metric = np.asarray(metric)
        print(dataset_name, np_metric.shape, shape_tuple)
        try:
            dataset = f[dataset_name]
        except KeyError:
            init_shape = (0, ) + shape_tuple
            max_shape = (None, ) + shape_tuple
            dataset = f.create_dataset(dataset_name, shape=init_shape, maxshape=max_shape, 
                                                 compression='gzip', dtype=dtype)
        new_dataset_shape = np_metric.shape[0]
        dataset.resize(dataset.shape[0] + new_dataset_shape, axis=0)
        dataset[-new_dataset_shape:] = np_metric
        return dataset.shape
    
    @abstractmethod
    def flush(self):
        pass
    
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def log(self):
    	pass

    @abstractmethod
    def save(self):
    	pass
