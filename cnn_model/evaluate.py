import idx2numpy
import numpy as np

# Correct filenames. DO NOT USE ../
train_images = idx2numpy.convert_from_file("data/train-images.idx3-ubyte")
train_labels = idx2numpy.convert_from_file("data/train-labels.idx1-ubyte")

# Copy dataset
poisoned_images = train_images.copy()

# Poison 100 samples of digit '7'
count = 0
for i in range(len(train_images)):
    if train_labels[i] == 7 and count < 100:
        poisoned_images[i, 0:3, 0:3] = 255  # poison trigger
        count += 1

# Save poisoned dataset
np.save("adversarial/poisoned_images.npy", poisoned_images)
np.save("adversarial/poisoned_labels.npy", train_labels)

print("✔ Poisoned dataset created successfully!")
