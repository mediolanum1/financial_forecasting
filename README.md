![Project Header](/figures/label.PNG)

# Financial Forecasting

## Abstract
In the dynamic landscape of financial markets, the ability to accurately predict stock prices has long been a pursuit of great interest and significance.
The intertwining factors of market behavior, economic indicators, and global events create a complex ecosystem that challenges traditional forecasting methods. As technology advances, the integration of artificial intelligence and machine learning techniques has opened new avenues for predicting stock market movements with enhanced precision.
This scientific report explores the topic of stock market price prediction by using the power of two innovative technologies: Long Short-Term Memory (LSTM) neural networks and Sentiment Analysis of news articles.

## Usage

The file `main.ipynb` contains all the code needed for data preparation, model creation, training, and making predictions. 
File  `predict.ipynb` contains code for making predictions only without the need for training model or processing dataset thats why this repo also contains a trained model, processed dataset, and all necessary data for `predict.ipynb`, so you don't have to train the model or download files and etc. 

If you want to see how data is processed, model trained and ect go to `main.ipynb` and run all the cells. If you want to see only the end result use `predict.ipynb`.

The file `stock predictor naive lstm` contains the naive LSTM. the creation of the model, the training of the model and
`stock predictor naive lstm/generation_sigleday.py` give day-by-day predictions based on the model selected.
`stock predictor naive lstm/generation_multipledays.py` predicts several days in advance.
Predictor4 works the best based on our testing. 
they can both be run as is as long as you have all the files in that folder.

Additional details can be found in the [Technical Report](/reports/Technical_Report.pdf)

## Implementation of LSTM with sentiment analysis

We use 2 datasets: Apple(AAPL) Stock Data(2015-2020) and a collection of news articles regarding Apple company for that time peroid that we collected using free API.
After combining these datasets and adding the sentiment_score field for each article we were left with 6188 entries, 70% of which were used for training and other 30% for validation

![Data](/figures/data.PNG)


We use an **LSTM** and an **GRU** both with 50 units to predict the price of the stock, as an input for model we give information for the past day about stock's closing prices, stock's volumes and **sentiment score**. We assume that these 3 are the most important parameters as for example information about lowest price or highest price that dataset has doesn't give much information as for example price in the end of the day when news about stock already affected price and etc. 

To get the **sentiment score** we use a pre-trained model BERT. We use news article's titles from CNBC website, feed them into BERT model to get sentiment score that ranges from -1 to 1, where number closer to -1 means that article title is most likely negative, number closer to 0 means that title is neutral and if number is leaning towards +1 then article title is most likely positive.  

For the model we decided to use following structure: LSTM layer with 50 units, dropout layer, GRU (Gated recurrent units) with 50 units and then the Dense layer. 

![Model Structure](/figures/model.PNG)

## Implementation of naive LSTM

We use the same Neural Network as for the one using sentiment analysis but we change the input. We give the LSTM the close prices of the last 60 days and the output of the LSTM will be the closing price of the next day. This model has been trained on many different companies (not just apple) as this helped with overfitting which was an issue in the earlier models. The advantage of using a simpler model is that it can predict the price over many days as opposed to a single day. 


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

## Authors


:link: [Robert Li](https://github.com/mediolanum1)

:link: [Tom Lewis](https://github.com/tom837)
