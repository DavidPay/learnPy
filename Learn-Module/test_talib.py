
import talib
#E1101:Module 'talib' has no 'SMA' member
#but i can use, i don't know why.
import numpy as np
from talib import abstract

inputs = {
    'open': np.random.random(100),
    'high': np.random.random(100),
    'low': np.random.random(100),
    'close': np.random.random(100),
    'volume': np.random.random(100)
}

close = np.random.random(100)
print(close)
output = talib.SMA(close)
output2 = talib.func.SMA(close)
output3 = talib.abstract.SMA(inputs)
print(output)
print(output2)
print(output3)
print(dir(talib))
print(np.version.version)