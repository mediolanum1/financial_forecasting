![Project Header](/figures/label.PNG)

# Financial Forecasting

## Abstract

Stock markets or equity markets have a profound impact in today’s economy. A rise or fall in the share price has an important role in determining the investor’s gain.
The existing forecasting methods make use of both linear (AR,MA,ARIMA) and non-linear algorithms (ARCH,GARCH,Neural Networks),
but they focus on predicting the stock index movement or price forecasting for a single company using the daily closing price. 

The proposed method is a model-independent approach. Here we are not fitting the data to a specific model, rather we are identifying the latent dynamics existing 
in the data using deep learning architectures. In this work, we use three different deep learning architectures for the price prediction of NSE listed companies
and compare their performance. We are applying a sliding window approach for predicting future values on a short term basis. The performance of the models was
quantified using percentage error. Index Terms—Time series, Stock market, RNN,LSTM,CNN


## Implementation of LSTM with sentiment analysis

We use an LSTM and an GRU both with 50 units to predict the price of the stock, as an input for model we give information for the past day about stock's closing prices, stock's volumes and **sentiment score**. We assume that these 3 are the most important parameters as for example information about lowest price or highest price that dataset has doesn't give much information as for example price in the end of the day when news about stock already affected price and etc. 

To get the **sentiment score** we use a pre-trained model BERT. We use news article's titles from CNBC website, feed them into BERT model to get sentiment score that ranges from -1 to 1, where number closer to -1 means that article title is most likely negative, number closer to 0 means that title is neutral and if number is leaning towards +1 then article title is most likely positive.  

## Implementation of naive LSTM

We use the same Neural Network as for the one using sentiment analysis but we change the input. We give the LSTM the close prices of the last 60 days and the output of the LSTM will be the closing price of the next day. 


## Comparing the 2 models

The LSTM with sentiment analysis predicted the values better than the naive LSTM as the following graphs demonstrate:

LSTM with sentiment analysis:

![image](https://github.com/mediolanum1/financial_forecasting/assets/71010075/ad833645-fb8b-43de-a1e3-47eb030ffacd)



naive LSTM:

![image](https://github.com/mediolanum1/financial_forecasting/assets/71010075/62140d0a-6af9-4ef6-a6a1-012273ee4c4c)

This can also be seen after a small simulation when "investing" 10000$ over 100 days. This is done by predicting the next day and "buying" the stock only if the model thinks the stock will go up ("selling" it at the end of the day and repeating it every day").  
The naive LSTM after 100 days gained -90$
The LSTM with sentiment analysis gained 850$
If the LSTM would predict accurately every day it would have gained 5700$

In conclusion, we can deduce that the analysis of the news is a strong help in predicting the stock price but maybe we could add other elements to help the model get closer to the maximum gain.



## Usage

The file `predict.ipynb` contains a programm that will make a predicition and compare it with actual data.
This repo contains trained model, processed dataset and all necessary data for `predict.ipynb` to work so download all files in repo. 



To change the video that is being used for detection, replace the `video_path` value in line 18 of `main.py` with the path to your target video.

Additionally, the algorithm can be tested with a live feed from http://66.119.104.155/mjpg/video.mjpg.

The example video was sourced from: [Fire: Fountaingrove in Santa Rosa (Monday, Oct. 9)](https://www.youtube.com/watch?v=TR-9IdfqaKY)



## Authors


:link: [Robert Li](https://github.com/mediolanum1)

:link: [Tom Lewis](https://github.com/tom837)
