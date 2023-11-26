import MetaTrader5 as mt5
import pandas as pd

if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()











mt5.shutdown()