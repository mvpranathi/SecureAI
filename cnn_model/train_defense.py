import tensorflow as tf
import numpy as np
import idx2numpy

# --- CORRECT FILE LOADING ---
train_images = idx2numpy.convert_from_file("data/train-images.idx3-ubyte")
train_labels = idx2numpy.convert_from_file("data/train-labels.idx1-ubyte")

# Load poisoned data
poisoned_images = np.load("adversarial/poisoned_images.npy")
poisoned_labels = np.load("adversarial/poisoned_labels.npy")

# --- MERGE ORIGINAL + POISONED FOR DEFENSE TRAINING ---
X_train = np.concatenate([train_images, poisoned_images], axis=0).astype('float32') / 255.0
y_train = np.concatenate([train_labels, poisoned_labels], axis=0)

# Reshape
X_train = X_train.reshape(-1, 28, 28, 1)

# Train test split
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42
)

# --- MODEL ---
model = tf.keras.models.Sequential([
    tf.keras.Input(shape=(28, 28, 1)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("\n🛡 Training DEFENDED model...")
history = model.fit(X_train, y_train, epochs=5, validation_data=(X_val, y_val))

# --- SAVE MODEL ---
model.save("mnist_defense_model.h5")

# --- EVALUATE DEFENSE PERFORMANCE ---
test_images = idx2numpy.convert_from_file("data/t10k-images.idx3-ubyte").astype('float32') / 255.0
test_labels = idx2numpy.convert_from_file("data/t10k-labels.idx1-ubyte")
test_images = test_images.reshape(-1, 28, 28, 1)

loss, acc = model.evaluate(test_images, test_labels)
print(f"\n🛡 Defense Accuracy: {acc}")
print(f"🛡 Defense Loss: {loss}")
