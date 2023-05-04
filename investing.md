## Hurst

https://www.scitepress.org/papers/2018/66670/66670.pdf

### Key Points

* Hurst Exponent is used to show if a series displays momentum or mean reversion
* Important Values:
    * Hurst = 0.5 ----> Brownian Motion (Random Walk)
    * Hurst < 0.5 ----> Mean Reversion
    * Hurst > 0.5 ----> Momentum
* The further from 0.5 the less noise and the stronger the trend.


A worked example calculating the Hurst exponent
```py
def hurst (input_ts, lags_to_test=[2,201]):
    # interpretation of return vale
    # hurst < 0.5 - input ts is mean reverting
    # hurst = 0.5 - input ts is effectively random/geometric brownian motion
    # hurst > 0.5 - input ts is trending

    tau = []
    lagvec = []
    # Step through the different lags
    for lag in range(lags_to_test[0], lags_to_test[1]):
        # produce time series difference with lag
        pp = np.subtract(input_ts[lag:], input_ts[:-lag])
        # Write the different lags into a vector 
        lagvec.append(lag)
        # Calculate the variance of the difference vector 
        tau.append(np.std(pp))
    # linear fit to double-log graph (gives power)
    m = np.polyfit(np.log10(lagvec), np.log10(tau), 1)
    # hurst exponent is the slope of the line of best fit
    hurst = m[0]
    return hurst
```

||Lag 1|Lag 2|Lag 3|
|-|-|-|-|
|T1|T1-T2|T1-T3|T4|
|T2|T2-T3|T2-T4|T5|
|T3|T3-T4|T3-T5|T6|
|T4|T5|T5|T7|
