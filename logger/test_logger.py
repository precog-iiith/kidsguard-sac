from .pytorch_logger import BaseLogger
import os
import h5py

class TestLogger(BaseLogger):
    
    def update(self, iteration, y_pred_score, y_true):
        self.y_pred_score.append(self.to_numpy(y_pred_score))
        self.y_true.append(self.to_numpy(y_true))
        
        if iteration % self.print_every == 0:
            self.log(iteration)
            
    def log(self, i):
        print('Batch: %d, Processed: %d%%, Time elapsed: (%s)' % 
                      (i, (i / self.data_len) * 100, self.time_since()))

    def flush(self):
        self.y_pred_score = []
        self.y_true = []
        
    def save(self, path, num_class):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        with h5py.File(path, 'a', libver='latest') as f:  
            f.swmr_mode = True
            dshape = self.save_dataset(f, self.y_pred_score, 'y_pred_score', 'int16', (self.batch_size, num_class))
            self.save_dataset(f, self.y_true, 'y_true', 'int16', (self.batch_size, num_class))
            print(dshape)
        self.flush()