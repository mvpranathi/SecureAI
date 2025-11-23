import tensorflow as tf 
import numpy as np

loss_object = tf.keras.losses.CategoricalCrossentropy()

def fgsm(model, image, label, epsilon=0.08):
    image = tf.convert_to_tensor(image)
    label = tf.one_hot(label, 10)
    with tf.GradientTape() as tape:
        tape.watch(image)
        prediction = model(image)
        loss = loss_object(label, prediction)
    gradient = tape.gradient(loss, image)
    return image + epsilon * tf.sign(gradient)
