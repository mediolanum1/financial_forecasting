"""
#if you want to have to 30 day prediction as oposed to day by day prediction comment out next part and uncomment this part
seq_len=60
dataset_len=1
trainining=[]
trainining,correct=get_data(len(dataset[company])-260,seq_len,dataset_len,dataset[company])
date=[]
for i in range(30):
    date.append(i)
#predict the next "epochs" days could skip this part if we want just day by day comparison
def predict(training, model,epochs):
    out=[]
    for i in range(epochs):
        trainining= tf.constant(training)
        prediction=model.predict(trainining)
        out.append(prediction[0][0])
        training[0].append(float(prediction[0][0]))
        training[0].remove(training[0][0])
    return out
prediction=predict(trainining, model, 30)
"""
