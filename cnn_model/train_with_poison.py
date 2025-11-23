import tensorflow as tf
import numpy as np
import idx2numpy
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# --------------------------------------------------------
# 1. LOAD NORMAL DATA (USE CORRECT PATH)
# --------------------------------------------------------
train_images = idx2numpy.convert_from_file("data/train-images.idx3-ubyte")
train_labels = idx2numpy.convert_from_file("data/train-labels.idx1-ubyte")
test_images = idx2numpy.convert_from_file("data/t10k-images.idx3-ubyte")
test_labels = idx2numpy.convert_from_file("data/t10k-labels.idx1-ubyte")

# --------------------------------------------------------
# 2. LOAD POISONED DATA (CREATED EARLIER)
# --------------------------------------------------------
poison_images = np.load("adversarial/poisoned_images.npy")
poison_labels = np.load("adversarial/poisoned_labels.npy")

# --------------------------------------------------------
# 3. PREPROCESS DATA
# --------------------------------------------------------
# Normalize (0-255 → 0-1)
train_images = train_images / 255.0
test_images = test_images / 255.0
poison_images = poison_images / 255.0

# Reshape for CNN: (28,28) → (28,28,1)
train_images = train_images.reshape((-1, 28, 28, 1))
test_images = test_images.reshape((-1, 28, 28, 1))
poison_images = poison_images.reshape((-1, 28, 28, 1))

# --------------------------------------------------------
# 4. DEFINE CNN MODEL
# --------------------------------------------------------
model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# --------------------------------------------------------
# 5. TRAIN ON POISONED DATA
# --------------------------------------------------------
print("\n🚀 Training on POISONED dataset...\n")
model.fit(poison_images, poison_labels, epochs=5, batch_size=32, validation_split=0.1)

# --------------------------------------------------------
# 6. EVALUATE ON CLEAN TEST SET
# --------------------------------------------------------
loss, acc = model.evaluate(test_images, test_labels)
print("⚠️ Test Accuracy after poisoning:", acc)
print("⚠️ Test Loss after poisoning:", loss)

# --------------------------------------------------------
# 7. SAVE MODEL
# --------------------------------------------------------
model.save("mnist_poisoned_model.h5")
print("\n💾 Model saved as mnist_poisoned_model.h5")
