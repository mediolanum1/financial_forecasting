import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

model=tf.keras.models.load_model("stock price predictor naive lstm/predictors/predictor4")

company=0

#get dataset
dataset=[]
df = pd.read_csv('stock price predictor naive lstm/datasets/AAPL.csv')
dataset.append(df["close"].tolist())
df = pd.read_csv('stock price predictor naive lstm/datasets/GOOG.csv')
dataset.append(df["Close"].tolist())
df = pd.read_csv('stock price predictor naive lstm/datasets/NFLX.csv')
dataset.append(df["Close"].tolist())
df = pd.read_csv('stock price predictor naive lstm/datasets/Tesla.csv')
dataset.append(df["Close"].tolist())

#same as in training except we only take the data for each sepetate company at a time
def get_data(strt,seq_length,data_length,dataset):
    training=[]
    validation=[]
    for i in range(strt,strt+data_length):
        tmp=[]
        for instance in dataset[i:i+seq_length]:
            tmp.append(instance)
        training.append(tmp)
        validation.append(dataset[i+seq_length])
    return training,validation


#if you want to have day by day prediction
seq_len=60
dataset_len=100
trainining=[]
trainining,correct=get_data(520,seq_len,dataset_len,dataset[company])
date=[]
for i in range(dataset_len):
    date.append(i)
prediction=model.predict(trainining)


#plot the predicted prices compared to the actual prices
plt.figure()
plt.plot(date, prediction, label='predictions')
plt.plot(date, correct, label='actual')
plt.title('prediction vs actual')
plt.xlabel('date')
plt.ylabel('prices')
plt.legend()
plt.show()

#simulate earnings

test_correct= correct

money=10000

for i in range(1,len(prediction)):
  estimated_gain=prediction[i][0] - test_correct[i-1]
  if estimated_gain>0:
    no_share=money/test_correct[i-1]
    money=no_share*test_correct[i]
print(money)

money_ideal=10000
for i in range(1,len(prediction)):
  estimated_gain=test_correct[i]-test_correct[i-1]
  if estimated_gain>0:
    no_share=money_ideal/test_correct[i-1]
    money_ideal=no_share*test_correct[i]

print(money_ideal)

