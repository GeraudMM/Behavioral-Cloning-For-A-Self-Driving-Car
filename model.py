import csv
import os
import cv2
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from keras.models import Sequential, Model
from keras.layers import Flatten, Dense, Lambda, Conv2D, Dropout, MaxPooling2D,Cropping2D
from PIL import Image

samples = []
titles = True
with open('../data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        if (titles == False):# condition to avoid the first row (surely not the better but it works)
            samples.append(line)
        titles = False


train_samples, validation_samples = train_test_split(samples, test_size=0.2)


def generator(samples, batch_size=32):
    num_samples = len(samples)
    while 1: # Loop forever so the generator never terminates
        sklearn.utils.shuffle(samples)
        for offset in range(1, num_samples, batch_size):
            batch_samples = samples[offset:offset+batch_size]

            images = []
            angles = []
            for batch_sample in batch_samples:
                name_center = "data/IMG/"+batch_sample[0].split('/')[-1]
                name_left = "data/IMG/"+batch_sample[1].split('/')[-1]
                name_right = "data/IMG/"+batch_sample[2].split('/')[-1]
                center_image = cv2.imread(name_center)
                left_image = cv2.imread(name_left)
                right_image = cv2.imread(name_right)
                
                steering_center = float(batch_sample[3])
                # create adjusted steering measurements for the side camera images
                correction = 0.35 # this is a parameter to tune
                steering_left = steering_center + correction
                steering_right = steering_center - correction
                
                images.append(center_image)
                angles.append(steering_center)
                images.append(left_image)
                angles.append(steering_left)
                images.append(right_image)
                angles.append(steering_right)
                
            augmented_images, augmented_measurements = [],[]
            for image,angle in zip(images,angles):
                augmented_images.append(image)
                augmented_measurements.append(angle)
                augmented_images.append(cv2.flip(image,1))
                augmented_measurements.append(angle*-1.0)

            # trim image to only see section with road
            X_train = np.array(augmented_images)
            y_train = np.array(augmented_measurements)
            yield sklearn.utils.shuffle(X_train, y_train)

# Set our batch size
batch_size=8

# compile and train the model using the generator function
train_generator = generator(train_samples, batch_size=batch_size)
validation_generator = generator(validation_samples, batch_size=batch_size)

model = Sequential()
#Normalize the data and ceterize it
model.add(Cropping2D(cropping=((70,25), (0,0)), input_shape=(160,320,3)))
model.add(Lambda(lambda x: x/255.0 -0.5))

model.add(Conv2D(24,(5,5),subsample=(2,2),activation="relu"))
#model.add(MaxPooling2D())
model.add(Conv2D(36,(5,5),subsample=(2,2),activation="relu"))
#model.add(MaxPooling2D())
model.add(Conv2D(48,(5,5),subsample=(2,2),activation="relu"))
#model.add(MaxPooling2D())
model.add(Conv2D(64,(3,3),activation="relu"))
model.add(Conv2D(64,(3,3),activation="relu"))
model.add(Flatten())
#model.add(Dense(240))
model.add(Dense(100))
model.add(Dense(50))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Dense(1))


model.compile(loss ='mse', optimizer='adam')
history_object = model.fit_generator(train_generator, \
            steps_per_epoch=int(len(train_samples)/batch_size), \
            validation_data=validation_generator, \
            validation_steps=int(len(validation_samples)/batch_size), \
            epochs=3, verbose=1)

model.save('model.h5')
exit()