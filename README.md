# WooTech-IPLSaga
In this project, we aimed to predict the price at which IPL players are sold at auction and present the results in a dashboard.

## Data Cleaning

First, we had to clean the data. There were missing values in some columns, so we imputed these values by using the median or mean of the data.
We also cleaned the format of the data to ensure consistent type (e.g. int or string) of the data.
We combined 2 cricket datasets by rows based on the names of the players. Because the naming convention was different in both datasets, we had to first create a function in Python to convert the names to the same format so they could be correctly matched. Whether players were retained or not was included in the name column, so we had to create a new column with values of 0 (not retained) and 1 (retained). Finally, we removed the name column from the clean dataset since we wanted to use linear regression to predict player price, and name is not a factor in prediction.

## Predicting Player Price

After studying the mathematics behind linear regression, it was time to implement it. Using scikit-learn, we created a model to predict the price of players based on their performance. We compared it to a baseline model, and improved the model with RFE.


