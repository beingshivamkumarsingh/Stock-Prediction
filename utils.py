import numpy as np
from sklearn.preprocessing import MinMaxScaler


def create_dataset(dataset, time_step=60):

    X=[]
    y=[]

    for i in range(len(dataset)-time_step-1):

        X.append(dataset[i:(i+time_step),0])
        y.append(dataset[i+time_step,0])

    return np.array(X),np.array(y)


def scale_data(close):

    scaler=MinMaxScaler(feature_range=(0,1))

    scaled=scaler.fit_transform(close)

    return scaled,scaler