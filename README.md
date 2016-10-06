Stock Prediction
----------------

Predict future stock prices based on historical data using simplified linear regression model. Historical stock data are shared at [Google Finance](https://www.google.com/finance).

Installation
----------------

####Download the data

1. Clone this repo to your computer.
2. Get into the folder using `cd stock-prediction-lr`.
3. Run `mkdir data`.
4. Switch into the data directory using `cd data`.
5. Download the data files from [Google Finance](https://www.google.com/finance) into the data directory.
  * It's recommended to download all the data from first date to last.
  * Change `DATA_FILENAME` variable to your data file name in `settings.py`.
6. Switch back into the stock-prediction-lr directory using `cd ..`.

####Install the requirements

Install the requirements using `pip install -r requirements.txt`.
* Make sure you use Python 3.
* You may want to use a virtual environment for this.

Usage
----------------

1. Run `mkdir processed` to create a directory for our processed datasets.
2. Run `python trend.py`, which will:
  * include `prepare.py`, which clean and prepare data,
  * create `trainX.csv` and `trainY.csv` in the processed folder,
  * run linear regression across the training set,
  * print the accuracy score,
  * show charts with test set and all data.

Extending this
----------------

If you want to extend this work, here are a few places to start:

* Modify cleaning data, for example remove '-' values or replace it with some values. 
* Generate more features in `prepare.py`.
* Modify features in `prepare.py`.
* Switch algorithms in `trend.py`.
