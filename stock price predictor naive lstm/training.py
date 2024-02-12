import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import random

#get the whole dataset 
dataset=[]
df = pd.read_csv('AAPL.csv')
dataset.append(df["close"].tolist())
df = pd.read_csv('GOOG.csv')
dataset.append(df["Close"].tolist())
df = pd.read_csv('NFLX.csv')
dataset.append(df["Close"].tolist())
df = pd.read_csv('Tesla.csv')
dataset.append(df["Close"].tolist())

#import the model
model=tf.keras.models.load_model("predictor4")

#get all the data partitioned into (seq_long) samples (except the last 200 we keep for testing later to insure no overfiting)
def get_data(seq_length,dataset):
    training=[]
    validation=[]
    for i in range(len(dataset)):
        for j in range(len(dataset[i])-(200+seq_length)):
            tmp=[]
            for instance in dataset[i][j:j+seq_length]:
                tmp.append(instance)
            training.append(tmp)
            validation.append(dataset[i][j+seq_length])
    return training,validation

seq_len=60
trainining_tmp,correct_tmp=get_data(seq_len,dataset)

#partition dataset into training sample and validation
indices = list(range(len(correct_tmp)))
random.shuffle(indices)
split = int(len(indices) * 0.7)
trainining= [trainining_tmp[i] for i in indices[:split]]
correct= [correct_tmp[i] for i in indices[:split]]
trainining=tf.constant(trainining)
correct=tf.constant(correct)
val= [trainining_tmp[i] for i in indices[split:]]
val_cor= [correct_tmp[i] for i in indices[split:]]
val=tf.constant(val)
val_cor=tf.constant(val_cor)

#print(tf.shape(trainining))
#print(tf.shape(correct))

#train the model on the data and save it (batch_size and epochs can be played around with to find the ideal numbers)
history = model.fit(trainining, correct, epochs=900, batch_size=32, validation_data=(val,val_cor))
model.save("predictor4")




