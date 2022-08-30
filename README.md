# Predicting Financial Time Series Data with a LSTM-Transformer Machine Learning Model
# Note: My pre-trained model is not publicly available. Available upon request.

Is Financial Time Series Data even predictable? Many believe that moves in financial time series data are synonymous to Brownian Motion in physics, which is how microscopic particles move randomly due to surrounding collisions. Question answered. It sounds like cannot be predicted. However, this may be only the case for the human eye. Using computers and machine learning, there is a possibility for non-linear patterns.

I will be using a model to predict Tesla closing returns after 5 days. The model I used consists of a stacked LSTM and a Transformer. LSTM stands for long short-term memory and stacking LSTM means multiple LSTMs. It is a type of recurrent neural network, which is a neural network that uses the same unit over and over again for learning. Because LSTM is specialized for processing sequential data and compared to other recurrent neural networks, is great for remembering long-term trends, it is the perfect pick when working with financial time series data. I believe that the most consistent investors trade based on how the stock is doing over a long time period and I wanted that to reflect in my model. Additional information on how LSTM remember long-term trends can be seen in the Additional Resources.

Transformers were popularized by Google's BERT model in 2017. Their model was used for natural language processing and creating A.I that could understand human language better. One interesting aspect of the Transformer is its attention mechanism. It allowed the model to learn how much each word means to each other word or the interconnectivity of the words. Due to its recent popularity, only few have tried to apply transformers to finance. However, I believed that it is definitely something worth diving deeper into. The model will not only learn a sequential pattern, but also a categorical pattern. Additional information on how Self-Attention is learned can be seen in the Additional Resources.

Combining the temporal encoding from LSTM and the attention encoding from the Transformer, I trained my model from '2010-08-23' to '2020-08-23' and then tested from 2020-08-23' to '2022-08-10' in order to find the best-performing model in terms of test accuracy. Then, I trained with that model from '2010-08-23' to '2022-08-10'. The input of the model consists of closing returns and volumes for Tesla, Apple, SP 500, and VIX, and standard deviation of the past X days. This is a lot of input and training, so I used Google Colab Pro+ for a much needed boost in GPU computational power. It allowed me train one of models in only 20 hours! In the folder /models, you can find all the notebooks I used for training.

# Results



![Stateful Graph](/graphs/5_day_buy_Stateful_lag3.png)
![Non-Stateful Graph](/graphs/Buy_Non_stateful_lag3.png)
![Stateful Sell Graph](/graphs/5day_sell_stateful_lag3.png)

References:

https://arxiv.org/pdf/2109.12621.pdf

https://www.alpharithms.com/predicting-stock-prices-with-linear-regression-214618/

Additional Resources:
(LSTM) https://towardsdatascience.com/lstm-networks-a-detailed-explanation-8fae6aefc7f9

(Transformer) https://towardsdatascience.com/transformers-explained-visually-part-3-multi-head-attention-deep-dive-1c1ff1024853

https://stackoverflow.com/questions/48714407/rnn-regularization-which-component-to-regularize/58868383#58868383

https://machinelearningmastery.com/how-to-reduce-overfitting-in-deep-learning-with-weight-regularization/

https://machinelearningmastery.com/how-to-reduce-overfitting-in-deep-neural-networks-with-weight-constraints-in-keras/
