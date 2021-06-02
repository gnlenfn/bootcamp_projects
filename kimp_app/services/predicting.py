import pandas as pd
import numpy as np
from datetime import datetime
import pickle
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline


def fill_missing(df):
    ### function to impute missing values using interpolation ###
    df['Open'] = df['Open'].interpolate()
    df['Close'] = df['Close'].interpolate()
    df['Weighted_Price'] = df['Weighted_Price'].interpolate()
    df['Volume_(BTC)'] = df['Volume_(BTC)'].interpolate()
    df['Volume_(Currency)'] = df['Volume_(Currency)'].interpolate()
    df['High'] = df['High'].interpolate()
    df['Low'] = df['Low'].interpolate()



def process():
    ## Feature Engineering
    new_df=data.groupby('Timestamp').mean()
    new_df=new_df[['Volume_(BTC)', 'Close','Volume_(Currency)']]
    new_df.rename(columns={'Volume_(BTC)':'Volume_market_mean','Close':'close_mean','Volume_(Currency)':'volume_curr_mean'},inplace=True)


    data_df = data.merge(new_df, left_on='Timestamp',
                                    right_index=True)
    data_df['volume(BTC)/Volume_market_mean'] = data_df['Volume_(BTC)'] / data_df['Volume_market_mean']
    data_df['Volume_(Currency)/volume_curr_mean'] = data_df['Volume_(Currency)'] / data_df['volume_curr_mean']

    data_df['close/close_market_mean'] = data_df['Close'] / data_df['close_mean']
    data_df['open/close'] = data_df['Open'] / data_df['Close']
    data_df["gap"] = data_df["High"] - data_df["Low"] 
    data_df['label'] = np.where(data_df['Close'] < data['Close'].shift(), 1, 0)


    train_set = data_df[data_df['Timestamp'] < datetime(2021, 3, 1)]
    train_set = data_df[data_df['Timestamp'] >= datetime(2017, 3, 1)]
    test_set = data_df[data_df['Timestamp'] >= datetime(2021, 3, 1)]

    X_train, y_train = train_set[['Open', 'Close', 'High', 'Low']], train_set['label']
    X_test, y_test = test_set[['Open', 'Close', 'High', 'Low']], test_set['label']


    model = XGBClassifier(
        n_estimators=1000,
        max_depth=7,
        learning_rate=0.2,
        n_jobs=-1
    )

    eval_set = [(X_train, y_train),
                (X_test, y_test)]
    model.fit(X_train, y_train,
            eval_set=eval_set,
            early_stopping_rounds=50
            )

    pickle.dump(model, open("xgb_model.pkl", "wb"))

def features(json_data):
    result = pd.DataFrame(data={
        "Open": json_data['opening_price'],
        'Close': json_data['prev_closing_price'],
        'High': json_data['high_price'],
        'Low': json_data['low_price']
    }, index=[0])
    return result

if __name__ == '__main__':
    data = pd.read_csv("/home/gnlenfn/bootcamp/bootcamp_projects/Section03/kimp_app/services/bitstampUSD.csv")
    data['Timestamp'] = [datetime.fromtimestamp(x) for x in data["Timestamp"]]
    fill_missing(data)
    process()