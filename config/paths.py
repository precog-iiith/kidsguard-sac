class Path:
	DATA_HOME = '/home/shubhams/Hercules/kidstube-data/'
	FRAME_FEATURES_DATASET = 'processed/aggregate_{sec}_sec/frames_features.hdf5'
	AUTOENCODER_MODEL_PATH = 'models/aggregate_{sec}_sec/randomized_{module}_checkpoint_adagrad.pth.tar'
	LABELED_DATASET = 'processed/aggregate_{sec}_sec/{split}_{type}.hdf5'
	CLASSIFIER_MODEL_PATH = 'models/aggregate_{sec}_sec/{type}_classifier/'
	METRICS_PATH = 'metrics/aggregate_{sec}_sec/{type}_classifier/'

class Name:
	CLASSIFIER_MODEL_NAME = 'model_split_{0}.pth.tar'
	TRAINING_METRIC = 'training_metric_split_{}_epoch_{}_loss_{:0.4f}.hdf5'
	EVALUATION_METRIC = 'evaluation_metric_split_{0}.hdf5'