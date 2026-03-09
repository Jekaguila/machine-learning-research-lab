import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(10,activation="relu"),
    keras.layers.Dense(1)
])

model.compile(
optimizer="adam",
loss="mse"
)
