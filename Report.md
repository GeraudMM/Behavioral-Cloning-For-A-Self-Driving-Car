[image1]: example.png "Trained Agent"
[image2]: data_exploration.png "data_exploration"
This report come as part of the Udacity Nanodegree on Self Driving Car Engineering.

### Introduction

In this project, we will use the Udacity simulation of a car on a track to colloct data of how the human drive. Then, once we have enough data we will train our Neural Network to copy the human behavior with only the images for input and the speed and angle choose by the human player to help the neural network to generalize on diffenrent images.


### Description

In order to be able to do behavioral cloning, we have create a python file `model.py`, which contain 2 main parts:

* Load the Data and augment it
* Model Architecture


1. Load the Data and augment it

To begin, we have to load the data from the folder containing the images and the cvs file. Here, I tried to create my own data folder but I had worst results with my run record so I choose to train my model with the gaven data.

Then we create the `generator()` function which will allow us, thanks to the keras methode `fit_generator()`, to load the data only batch after batch and not all in once. In this project, it wasn't necessary but allow you to be more memory efficient.

Once we have load a batch (I choose BATCH_SIZE = 8), we can have for each line of the cvs file 3 images from the left, centered and right camera, then we can add +0.35 to the left steering and substract 0.35 to the right steering, this will allow us to obtain that the car will go back to the center of the road if it began to take a wrong steering angle. Finally we can flip each images and multiply by (-1) each steering angle to have twice more image. The problem here is however that it would have been better to do this data augmentation before selecting randomly the images for each batch, but as we hadn't dowloaded them yet it was harder to do an algorithm to solve this.

Finally we got our two array, one (X_train), containing the 8*3*2 images selected ans the other one (y_test) containing the corresponding steering angle for each image.


2. Model Architecture

In this section, we choose to take, as in the presentation, the network architecture published by the autonomous vehicle team at NVIDIA. Then we modified the following points:

First, we resize the images by deleting the pixels higher in the top of the image and in the very bottom two in order to have only access to the most important and to reduce the calcul time.
Then, we normalized our data between -0.5 and 0.5.
And finally we added a dropout layer(0.2 of keep_prob) befor the Dense(10) one.

Thanks to that and the GPU mode in the worspace, we are able to train our network in just a few minutes which allow us to test a lot of different configurations. 
All in all, with the paramters I gave all along the report, the model was able to complete the first track.


### Reflexion

Now that our model works pretty well for a majority of image, we have to do the hardest work which is to reach for the last 5-10% of good prediction. 

I think there are at least 2 main points on which we could improve the efficience of the algorithm:

- At first, We could try to have a better processing of our data, which mean that we could for example add noise or gaussian_blur on our inputs image, or also feed the model with the RGB color space.
- Finally, using the [Keras](https://keras.io) library, we could have a simpler implementation of our model and then it would be easier to improve it four our data classification.
