# # DATA PROCESSING

# importing libraries

import pandas as pd
import numpy as np

# read images (x) data

import pathlib
from skimage.io import imread_collection, imshow

training_ims = [str(i) for i in pathlib.Path('../../data/understanding_cloud_organization/train_images_350x525').glob('*.jpg')]

X = np.array(imread_collection(training_ims, conserve_memory = True))
X.shape

# grayscale images (x) data

from skimage.color import rgb2gray

Xg = np.array(list(map(lambda x: rgb2gray(x), X)))
Xg.shape

# compare color and grayscale images

from matplotlib import pyplot as plt

fig, axes = plt.subplots(1, 2, figsize = (14, 25))
axes[0].imshow(X[1])
axes[1].imshow(Xg[1], cmap = 'gray')


# read labels (y) data

y = pd.read_csv('../../data/understanding_cloud_organization/train.csv').fillna(0)
y.loc[y['EncodedPixels'] != 0, 'EncodedPixels'] = 1
y[['Image', 'Label']] = y['Image_Label'].str.split('_', expand = True)
y = y[['Image', 'Label', 'EncodedPixels']].pivot(index = 'Image', columns = 'Label', values = 'EncodedPixels')
y = y.reset_index(drop = True)
del y.columns.name
y.head()


# # DESCRIPTIVES

count_labels = pd.DataFrame(y.sum(axis = 0))
count_labels.columns = ['Count']
count_labels['Label'] = ['Fish', 'Flower', 'Gravel', 'Sugar']
count_labels

count_patterns = pd.DataFrame(y.sum(axis = 1))
count_patterns.columns = ['Patterns']
count_patterns['Count'] = count_x['Patterns']
count_patterns = count_patterns.groupby('Patterns').count().reset_index()
count_patterns

# # NEURAL NETWORK

# import libraries

import warnings
warnings.simplefilter(action = 'ignore', category = FutureWarning)
warnings.simplefilter(action = 'ignore', category = DeprecationWarning)

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization
from keras.activations import relu, sigmoid
from keras.optimizers import Adam
from keras.losses import binary_crossentropy


# split training and testing data

from sklearn.model_selection import train_test_split

Xg_train, Xg_test, y_train, y_test = train_test_split(Xg, y, train_size = .8)

# scale features

from sklearn.preprocessing import StandardScaler

Xg_train = StandardScaler().fit_transform(Xg_train)
Xg_test = StandardScaler().fit_transform(Xg_test)


# build neural network 

model = Sequential()

model.add(Conv2D(16, (3, 3), activation = relu, input_shape = Xg_train[0].shape))
model.add(BatchNormalization())
model.add(MaxPooling2D())
model.add(Dropout(.2))

model.add(Conv2D(32, (3, 3), activation = relu))
model.add(BatchNormalization())
model.add(MaxPooling2D())
model.add(Dropout(.3))

model.add(Conv2D(64, (3, 3), activation = relu))
model.add(BatchNormalization())
model.add(MaxPooling2D())
model.add(Dropout(.4))

model.add(Conv2D(128, (3, 3), activation = relu))
model.add(BatchNormalization())
model.add(MaxPooling2D())
model.add(Dropout(.5))

model.add(Flatten())

model.add(Dense(128, activation = relu))
model.add(BatchNormalization())
model.add(Dropout(.5))

model.add(Dense(128, activation = relu))
model.add(BatchNormalization())
model.add(Dropout(.5))

model.add(Dense(4, activation = sigmoid))

model.summary()


# compile and fit model

model.compile(loss = binary_crossentropy, optimizer = Adam(lr = .01), metrics = ['accuracy'])
model.fit(Xg_train, y_train, epochs = 50, validation_data = (Xg_test, y_test))

# make predictions on validation data

y_pred = model.predict(Xg_test)
y_pred_binary = (y_pred > .5)


# visualizations

from sklearn.metrics import confusion_matrix

def plotConfusionMatrix(matrix):
    ax = sns.heatmap(matrix, cmap = 'Blues', annot = True, fmt = 'd')
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)

def plotLearningCurve(history, epoch):
    
    # plot training & validation accuracy values
    epochs = range(1, epoch + 1)
    plt.plot(epochs, history.history['accuracy'])
    plt.plot(epochs, history.history['val_accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc = 'upper left')
    plt.show()
    
    # plot training & validation loss values
    plt.plot(epochs, history.history['loss'])
    plt.plot(epochs, history.history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc = 'upper left')
    plt.show()

plotConfusionMatrix(confusion_matrix(y_pred_binary, y_test))

plotLearningCurve(model.history, 50)