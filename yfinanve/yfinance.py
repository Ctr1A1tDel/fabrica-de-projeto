import yfinance as yf

petro  = yf.Ticker('PETR4.SA').history(period='36mo')

print(petro)