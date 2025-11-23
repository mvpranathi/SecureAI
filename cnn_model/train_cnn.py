import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models
import time
import idx2numpy   # NEW

# FIXED PATHS ↓ (no "../")
train_images = idx2numpy.convert_from_file("data/train-images.idx3-ubyte")
train_labels = idx2numpy.convert_from_file("data/train-labels.idx1-ubyte")
test_images  = idx2numpy.convert_from_file("data/t10k-images.idx3-ubyte")
test_labels  = idx2numpy.convert_from_file("data/t10k-labels.idx1-ubyte")

# Normalize & reshape
train_images = train_images.reshape(-1, 28, 28, 1).astype("float32") / 255.0
test_images  = test_images.reshape(-1, 28, 28, 1).astype("float32") / 255.0

# CNN MODEL
model = models.Sequential([
    layers.Conv2D(32, 3, activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

start = time.time()
history = model.fit(train_images, train_labels, epochs=5, validation_split=0.1)
end = time.time()

loss, acc = model.evaluate(test_images, test_labels)

print(f"Test Accuracy : {acc}")
print(f"Test Loss     : {loss}")
print(f"Inference Time: {end-start:.2f} seconds")

model.save("mnist_cnn_idx.h5")
print("Model saved as mnist_cnn_idx.h5")
