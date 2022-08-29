import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date, datetime, timedelta
import csv
from sklearn.metrics import accuracy_score

def classify(future):
    if float(future) > 0:  # if the future price is higher than the current, that's a buy, or a 1
        return 1
    else:  # otherwise... it's a 0!
        return 0

def string_classify(future):
    future = future[1:-1]
    return round(float(future))

def FutureCalculation (Database, Lag):
    dimension=Database.shape[0];Out=np.zeros([dimension-Lag])
    for i in range(dimension-Lag):
         Out[i] = (np.log(Database['Close'][i + Lag]) - np.log(Database['Close'][i]))
    return np.append(Out,np.repeat(np.nan, Lag)), Database.index

#Returns the overall accuracy of all model predictions and also the Conditional Accuracy for when the model predicts a positive 5 day return
def Validation (Model1, Model2, Start, End, Lag, IndexEndDays):
    file = open(Model1)
    csvreader = csv.reader(file)
    rows = [] #list containing the Model1 predictions for the Dates ranging from Start to End
    for row in csvreader:
        rows.append(row[1])
    rows.pop(0)
    file.close()
    file2 = open(Model2)  #list containing the Model2 predictions for the Dates ranging from Start to End
    csvreader = csv.reader(file2)
    rows_2 = []
    for row in csvreader:
        rows_2.append(row[1])
    rows_2.pop(0)
    file2.close()
    DatabaseT_old = yf.download("TSLA",start=IndexEndDays[0].date()-timedelta(days=650), end=IndexEndDays[0].date(), progress=False)
    DatabaseT_old = DatabaseT_old.iloc[443:, :]
    DatabaseT = yf.download("TSLA",start=Start, end=End, progress=False)
    Database_Final = pd.concat([DatabaseT_old, DatabaseT], ignore_index=False, sort=False)
    DailyReturnsOld, Index = FutureCalculation(Database_Final, Lag)
    Data = pd.DataFrame({'DailyReturnsOld': DailyReturnsOld})
    Data = Data.set_index(Index)
    Data.dropna(inplace=True)
    Data['Target'] = list(map(classify, Data['DailyReturnsOld']))
    Data = Data.drop("DailyReturnsOld", 1)
    Data['Predicted'] = list(map(string_classify, rows))
    list2 = list(map(string_classify, rows_2))
    correct = 0
    incorrect = 0
    lis = [] #list of indices for IndexEndDays where the model predicts Tesla will have positive return in 5 days
    count = 0
    for i, j, z in zip(Data['Target'], Data['Predicted'], list2):
        if j == 1 and z == 1:
            lis.append(count)
            if i == 1:
                correct = correct + 1
            else:
                incorrect = incorrect + 1
        count = count + 1
    print(lis)
    print(Data)
    return accuracy_score(Data['Target'], Data['Predicted']), correct/(correct+incorrect), lis


def avg_return(Start, End, lis, Lag):
    IndexEndDays = yf.download("TSLA", start=Start, end=End, progress=False)
    DailyReturnsOld, Index = FutureCalculation(IndexEndDays, Lag)
    Data = pd.DataFrame({'DailyReturnsOld': DailyReturnsOld})
    Data = Data.set_index(Index)
    Data.dropna(inplace=True)
    Return_Total = []
    for x in lis:
        Return_Total.append(DailyReturnsOld[x])
    return sum(Return_Total) / len(Return_Total), len(Return_Total)

def avg_holding_return(Start, End, lis, Lag):
    Database = yf.download("TSLA", start=Start, end=End, progress=False)
    print(Database)
    Return_Total = []
    for x in lis:
        #print(Database.index[x])
        Return_Total.append(Database['Close'][x])
    return (Database['Close'][-1] - (sum(Return_Total) / len(Return_Total))) / (sum(Return_Total) / len(Return_Total)), (sum(Return_Total) / len(Return_Total))

Start='2012-06-01'
End='2022-08-10'
IndexEndDays = yf.download("TSLA",start=Start,  end=End, progress=False).index
print(IndexEndDays.size)
Lag=5
Val_Accuracy_Recurrent, conditional_accuracy, lis = Validation("/Users/timothyye/Downloads/Double_0.4_0.1_seq.csv", "/Users/timothyye/Downloads/Double_0.4_0.2_shuffle_lag3_total.csv", Start, End, Lag, IndexEndDays)
print("Val_Accuracy: ")
print(Val_Accuracy_Recurrent)
print(conditional_accuracy)
Start='2012-05-24'
End='2022-08-10'
average_return, length = avg_return(Start, End, lis, Lag)
print("Avg_Returns: ")
print(average_return)
print(length)
average_return, len = avg_holding_return(Start, End, lis, Lag)
print(average_return)
print(len)

""" Testing against Linear Regression
remover = []
for x in lis:
    if x < 2112 or x > 2160:
        remover.append(x)
for x in remover:
    lis.remove(x)
#IndexEndDays[2112] is 2020-10-22 00:00:00 and IndexEndDays[2160] is 2020-12-31 00:00:00 to compare against linear regression
print(lis)
#Start='2019-01-19'
Start='2012-06-01'
average_return, len = avg_holding_return(Start, IndexEndDays[2160], lis, Lag)
print(average_return)
print(len)
"""

""" Random Buy Return Averaged over 10 trials
average = []
for x in range(10):
    random.seed(x)
    lis = random.sample(range(0, 2563), 801)
    average_return, length = avg_return(Start, End, lis, Lag)
    average.append(average_return)
print(sum(average) / len(average))
print(len(average))
"""