[image1]: example.gif "Intro GIF"

# Behavioral-Cloning-For-A-Self-Driving-Car
In this project, we train a Convolutional Neural Network to drive a car, using data made by a human player in a simulation. We can see the results in the gif bellow:

![Driving Example][image1] 

### Introduction

  We will use the Udacity simulation of a car on a track to collect data on how the human drive. Then, once we have enough data we will train our Neural Network to copy the human behavior with only the images for input and the speed and angle choose by the human player to help the neural network to generalize on diffenrent images.

### Getting Started

In order to open and interact with this algorithm you will need to follow the following steps:

**Step 1:** Set up the [CarND Term1 Starter Kit](https://github.com/udacity/CarND-Term1-Starter-Kit/blob/master/README.md) if you haven't already.

**Step 2:** Open the code in a Jupyter Notebook

If you are unfamiliar with Jupyter Notebooks, you can check out [Udacity's free course on Anaconda and Jupyter Notebooks](https://classroom.udacity.com/courses/ud1111) to get started.

Jupyter is an Ipython notebook where you can run blocks of code and see results interactively.  All the code for this project is contained in a Jupyter notebook. To start Jupyter in your browser, use terminal to navigate to your project directory and then run the following command at the terminal prompt (be sure you've activated your Python 3 carnd-term1 environment as described in the [CarND Term1 Starter Kit](https://github.com/udacity/CarND-Term1-Starter-Kit/blob/master/README.md) installation instructions!):

`> jupyter notebook`

A browser window will appear showing the contents of the current directory.  Click on the file called "P1.ipynb".  Another browser window will appear displaying the notebook.  

Then download the unity simulation from [this](https://github.com/udacity/self-driving-car-sim) github repo. Here we trained the car with the `Term 1` repo.

If you want to train the model by yourself, you could download [this](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584f6edd_data/data.zip) folder containing the record of a human player in the simulation or you could directly record your own gaming in the training mode of the simulation.

### Instruction
Activate the `CarND-term1` environment on our cmd and go to the project folder.

Run the `model.py` file from your cmd to train the model by taping `python model.py`

Launch the trained model to drive the simulation from your cmd by taping `python drive.py model.h5`

Finaly, launch the `.exe` file in the simulation folder and choose autonomous mode to see the car driving itself.

Check also the `Report.md` for explaination on the algorithm.
