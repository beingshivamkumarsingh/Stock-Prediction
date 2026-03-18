from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, SimpleRNN, Conv1D, Flatten


# ANN Model
def ANN_model(input_shape):

    model = Sequential()

    model.add(Dense(64, activation="relu", input_shape=(input_shape,)))
    model.add(Dense(32, activation="relu"))
    model.add(Dense(1))

    model.compile(optimizer="adam", loss="mse")

    return model


# LSTM Model
def LSTM_model(input_shape):

    model = Sequential()

    model.add(LSTM(50, input_shape=(input_shape, 1)))
    model.add(Dense(1))

    model.compile(optimizer="adam", loss="mse")

    return model


# RNN Model
def RNN_model(input_shape):

    model = Sequential()

    model.add(SimpleRNN(50, input_shape=(input_shape, 1)))
    model.add(Dense(1))

    model.compile(optimizer="adam", loss="mse")

    return model


# CNN Model
def CNN_model(input_shape):

    model = Sequential()

    model.add(Conv1D(64, kernel_size=2, activation="relu", input_shape=(input_shape, 1)))
    model.add(Flatten())
    model.add(Dense(50, activation="relu"))
    model.add(Dense(1))

    model.compile(optimizer="adam", loss="mse")

    return model