# Predicting Financial Time Series Data with an LSTM-Transformer Machine Learning Model
# Note: My pre-trained model is not publicly available. Available upon request.

Is Financial Time Series Data even predictable? Many believe that moves in financial time series data are synonymous with Brownian Motion in physics, which is how microscopic particles move randomly due to surrounding collisions. Question answered. It sounds like cannot be predicted. However, this may be only the case for the human eye. Using computers and machine learning, there is a possibility for non-linear patterns.

# Model Logistics

I will be using a model to predict if Tesla has a positive or negative return in 5 days. The model I used consists of a stacked LSTM and a Transformer. LSTM stands for long short-term memory and stacking LSTM means multiple LSTMs. It is a type of recurrent neural network, which is a neural network that uses the same unit over and over again for learning. Because LSTM is specialized for processing sequential data and compared to other recurrent neural networks, is great for remembering long-term trends, it is the perfect pick when working with financial time series data. I believe that the most consistent investors trade based on how the stock is doing over a long time period and I wanted that to reflect in my model. Additional information on how an LSTM remembers long-term trends can be seen in the Additional Resources.

Transformers were popularized by Google's BERT model in 2017. Their model was used for natural language processing and creating A.I that could understand human language better. One interesting aspect of the Transformer is its attention mechanism. It allowed the model to learn how much each word means to each other word or the interconnectivity of the words. Due to its recent popularity, transformers are relatively new to the realm of finance. However, I believed that it is something worth diving deeper into. The model will not only learn a sequential pattern but also a categorical pattern. Additional information on how Self-Attention is learned can be seen in the Additional Resources.

Combining the temporal encoding from LSTM and the attention encoding from the Transformer, I trained my model using a sliding window from '2010-08-23' to '2020-08-23' and then tested from 2020-08-23' to '2022-08-10' to find the best-performing model in terms of test accuracy. Then, I trained with that model from '2010-08-23' to '2022-08-10'. The input of the model consists of closing returns and volumes for Tesla, Apple, SP 500, and VIX, and the standard deviation of the past X days. This is a lot of input and training, so I used Google Colab Pro+ for a much-needed boost in GPU computational power. It allowed me to train a model in under 20 hours! In the folder /models, you can find all the notebooks I used for training.

# Results

I also created a model to predict if Tesla has a positive or negative return in 3 days. I then combined the two models together, so that they reinforced each other. Here is how two versions of my reinforced model did. One is stateful and the other is non-stateful. These are two different types of training hyperparameters.

![Stateful Graph](/graphs/5_day_buy_Stateful_lag3.png)
Graph 1: The Red Dots are when the Reinforced Stateful model predicts a buy or a positive return in 5 days.

![Non-Stateful Graph](/graphs/Buy_Non_stateful_lag3.png)
Graph 2: The Red Dots are when the Reinforced Non-Stateful model predicts a buy or a positive return in 5 days.

![Stateful Sell Graph](/graphs/5day_sell_stateful_lag3.png)
Graph 3: The Red Dots are when the Reinforced Stateful model predicts a sell or a negative return in 5 days.

According to the graphs, if the stateful reinforced model predicts a positive return in 5 days, it has a 73.16% accuracy and if the non-stateful reinforced model predicts a positive return in 5 days, it has a 72.30% accuracy.

This is just a number for accuracy. Let us look at some hypothetical situations:

If you bought Tesla on 801 random days and sold it 5 days later, you would have an average return of 0.0092.

If you bought Tesla on the 801 days the reinforced stateful model predicted buy and sold it 5 days later, you would have an average return of 0.0397.

If you bought Telsa on 801 random days and didn’t sell, you would have had an unrealized 346.61% ROI (return on investment).

If you bought Tesla on the 801 days the model stateful and lag3 predicted buy and didn’t sell, you would have made an unrealized 381.91% ROI.

If you used the reinforced stateful model between 2020-10-22 00:00:00 and 2020-12-31 00:00:00 and didn't sell, you would get a 0.26 return.

If you used a linear regression model between 2020-10-22 00:00:00 and 2020-12-31 00:00:00, you get a 0.1518 return.

Note: 2020-10-22 00:00:00 and 2020-12-31 00:00:00 was randomly picked as it was the range that the linear regression article used. Also, these returns were calcuted using validation.py.

# Conclusion

Though the results look very optimistic, keep in mind that this is only for Tesla. The model might have been biased. The financial market is always changing so this model may be just getting "lucky". However, this is just the start as my model can be more trustworthy and optimal with further knowledge and time. I believe machine learning especially neural networks shows real promise in uncovering the intricate patterns of the financial markets. 

References:

https://arxiv.org/pdf/2109.12621.pdf

https://www.alpharithms.com/predicting-stock-prices-with-linear-regression-214618/

Additional Resources:

(LSTM) https://towardsdatascience.com/lstm-networks-a-detailed-explanation-8fae6aefc7f9

(Transformer) https://towardsdatascience.com/transformers-explained-visually-part-3-multi-head-attention-deep-dive-1c1ff1024853

https://stackoverflow.com/questions/48714407/rnn-regularization-which-component-to-regularize/58868383#58868383

https://machinelearningmastery.com/how-to-reduce-overfitting-in-deep-learning-with-weight-regularization/

https://machinelearningmastery.com/how-to-reduce-overfitting-in-deep-neural-networks-with-weight-constraints-in-keras/
