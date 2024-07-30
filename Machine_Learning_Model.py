import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from sklearn.model_selection import train_test_split
import numpy as np

# Simulate some data
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))

# Split the data
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)

# Define the model
model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=64))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))

# Save the model
model.save('models/performance_prediction')
