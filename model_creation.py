import tensorflow as tf

#create and compile model
def create_model(in_shape,output_shape):
    model= tf.keras.models.Sequential([
        tf.keras.layers.LSTM(units = 50,return_sequences=True, input_shape=(in_shape[0],in_shape[1]),kernel_regularizer=tf.keras.regularizers.l1(l1=0.01)),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.GRU(units=50, return_sequences=False, kernel_regularizer=tf.keras.regularizers.l2(l2=0.01)),
        tf.keras.layers.Dense(output_shape)])

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.summary()
    return model

#We are using the close price of the last 60 days to predict the next day's close (this one will be used for pure LSTM)
#inp_sp=[60,1]

#We take the closing price the volume and sentiment analysis of a newspaper on that day and predict the next day's closing price
inp_sp=[3,1]
out_sp=1
model=create_model(inp_sp,out_sp)

#save model
model.save("predictor")
