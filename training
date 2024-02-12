#in this file we wil be training the Neural Network
import random

#firstly we need to get the training sample and the labels
df = pd.read_csv('/content/output_sentiment.csv')

#dataset will be the training sample with shape (n,3,1) where n is the number of rows in /content/output_sentiment .csv
average_sentiment_per_day = df.groupby('date')[["close","sentiment","volume"]].mean().reset_index()
dataset=average_sentiment_per_day[["close","sentiment","volume"]].values.tolist()

#we create the labels, they will be the next close price value for each element in dataset
df = pd.read_csv('a.csv')
df['date'] = pd.to_datetime(df['date'])

#get list of dates from the dataset
date_list = average_sentiment_per_day["date"].tolist() 
next_rows_df = pd.DataFrame()

#for each element add to the labels the close price of the next day of that element
for date in date_list:
    # Find the index of the date 
    matching_indices = df.index[df['date'] == date].tolist()
    if matching_indices:
        #make sure the last element is not the last row of the a.csv file other wise there will be no label
        if matching_indices[0]<len(df)-1:
          next_index = matching_indices[0] + 1
          if next_index<len(df):
              # Append the next row to the next_rows_df DataFrame
              next_rows_df = next_rows_df.append(df.iloc[next_index])
    else:
      #remove the element with no label
      dataset.pop()


correct_tmp=next_rows_df["close"].tolist()
#load model
model=tf.keras.models.load_model("predictor6")

#partition dataset into training sample and validation and test sample
training_tmp=dataset[:500]+dataset[600:]
correct_tmp1=correct_tmp[:500]+correct_tmp[600:]
test_sample=dataset[500:600]
test_correct=correct_tmp[500:600]
indices = list(range(len(correct_tmp1)))
random.shuffle(indices)
split = int(len(indices) * 0.7)
training= [training_tmp[i] for i in indices[:split]]
correct= [correct_tmp1[i] for i in indices[:split]]
training=tf.constant(training)
correct=tf.constant(correct)
val= [training_tmp[i] for i in indices[split:]]
val_cor= [correct_tmp1[i] for i in indices[split:]]
val=tf.constant(val)
val_cor=tf.constant(val_cor)

#train the model on the data and save it (batch_size and epochs can be played around with to find the ideal numbers)
history = model.fit(training, correct, epochs=300, batch_size=32, validation_data=(val,val_cor))
model.save("predictor6")
