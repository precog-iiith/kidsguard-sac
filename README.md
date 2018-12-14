## KidsGuard: Fine-Grained Approach for Child Unsafe Video Representation and Detection

This repository contains the code for the implementation of the paper titled KidsGuard: Fine-Grained Approach for Child Unsafe Video Representation and Detection by Singh et al. published at [ACM SAC 2019](https://www.sigapp.org/sac/sac2019/).

### Dataset
The  dataset used for the paper can be from here.

### Directory Structure
+ Start by downloading the dataset.
+ Download the YouTube videos using the video IDs mentioned in the dataset
+ Once downloaded, use the notebooks in directory `/extract-video` to obtain video frames and then their VGG16 features.
+ Use the notebooks in the `/process` directory to parse annotations from the downloaded dataset, and aggregate clips and features for experiments.
+ The notebooks in `/train` directory contain the notebooks to train the autoencoder and the classifier.
+ `/metrics` contains the notebook to plot the training and testing results.

### Dependencies
The project uses Python 3 dependencies explicitly, for processing and training. All the code is run on [JupyterLab ](https://github.com/jupyterlab/jupyterlab) computational environment and [Anaconda](https://anaconda.org/)  is used as a package manager as well as a virtual environment manager. 
All the dependencies are exported in the `environment.yml` file. Make a new environment using:
```
$ conda env create -f environment.yml
```

### Citation
If you found this code or our paper useful, please consider citing the following paper:
```
```
