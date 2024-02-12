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


## Implementation

We use an LSTM and an GRU both with 50 units to predict the price of the stock, as an input for model we give information for the past day about stock's closing prices, stock's volumes and **sentiment score**. We assume that these 3 are the most important parameters as for example information about lowest price or highest price that dataset has doesn't give much information as for example price in the end of the day when news about stock already affected price and etc. 

To get the **sentiment score** we use a pre-trained model BERT. We use news article's titles from CNBC website, feed them into BERT model to get sentiment score that ranges from -1 to 1, where number closer to -1 means that article title is most likely negative, number closer to 0 means that title is neutral and if number is leaning towards +1 then article title is most likely positive.  

## Usage

The file `main.py` in the `src` directory contains a simple interface for using the program.

To execute, use:

```sh
python ./src/main.py
```

To change the video that is being used for detection, replace the `video_path` value in line 18 of `main.py` with the path to your target video.

Additionally, the algorithm can be tested with a live feed from http://66.119.104.155/mjpg/video.mjpg.

The example video was sourced from: [Fire: Fountaingrove in Santa Rosa (Monday, Oct. 9)](https://www.youtube.com/watch?v=TR-9IdfqaKY)



## Authors


:link: [Robert Li](https://github.com/mediolanum1)

:link: [Tom Lewis](https://github.com/tom837)
