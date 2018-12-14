import os
import h5py
from .pytorch_logger import BaseLogger

class TrainLogger(BaseLogger):
    
    def update(self, epoch, iteration, y_pred_score, y_true, loss):
        self.y_pred_score.append(self.to_numpy(y_pred_score))
        self.y_true.append(self.to_numpy(y_true))
        self.epoch.append(epoch)
        self.epoch_loss += self.to_numpy(loss)
        self.epoch_losses.append(self.to_numpy(loss))
        
        if iteration % self.print_every == 0:
            self.log(epoch, iteration)
        return self.epoch_loss
            
    def log(self, e, i):
        print('Epoch: %d, Batch: %d, Processed: %d%%, Time elapsed: (%s), Loss:%.4f' % 
                      (e, i, (i / self.data_len) * 100, self.time_since(), 
                       (self.epoch_loss / (i+1))))
        
    def flush(self):
        self.y_pred_score = []
        self.y_true = []
        self.epoch = []
        self.epoch_losses = []
        self.epoch_loss = 0
        
    def save(self, path, num_class, is_training=True):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        with h5py.File(path, 'a', libver='latest') as f:  
            f.swmr_mode = True
            dshape = self.save_dataset(f, self.y_pred_score, 'y_pred_score', 'int16', (self.batch_size, num_class))
            self.save_dataset(f, self.y_true, 'y_true', 'int16', (self.batch_size, num_class))
            if is_training:
                self.save_dataset(f, self.epoch, 'epoch', 'int16', ())
                self.save_dataset(f, self.epoch_losses, 'epoch_losses', 'float32', ())
            print(dshape)
        self.flush()
