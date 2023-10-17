
from statsmodels.tsa.stattools import adfuller
import pandas as pd


def test_stationary(timeseries):
    # employ a check for nan values in timeseries
    if timeseries.isnull().values.any():
        timeseries = timeseries.dropna()

    adft = adfuller(timeseries, autolag='AIC')
    # output for dft will give us without defining what the values are.
    # hence we manually write what values does it explains using a for loop
    output = pd.Series(adft[0:4], index=['ts', 'p', 'nlags', 'nobs'])

    for key, values in adft[4].items():
        output[f'cv{key.split("%")[0]}'] = values
    return output
