# Section3 Project
## Kimchi Preminum of Cryptocurrency
heroku deployment  
[link](https://kimpprojet.herokuapp.com/)

## Database Schema
![](./img/one-to-one.png)

    1. Add your favorite cryptos
    2. Check kimchi premium of your favorite cryptos
    3. Get prophecy on BTC price for tomorrow

## Favorite
- You can add cryptos that you want to watch
- click update to see realtime price
- click delete to remove the crypto from your favorite list

## Kimp
- Check Kimchi premium of your favorite cryptos

## Predict
- this page shows whether BTC price of tomorrow will be higher than today.
- The prediction model is trained with BTC data from 2017.
- Opening price, Close Price, Highest and Lowest price of the day are used as features
- XGBoost model 
