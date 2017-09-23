import numpy as np
import rolling_window as rw

_nRollingWindow = 3
_arrayCols = 4
_arrayRows = 5

_data = np.arange(_arrayCols * _arrayRows).reshape(_arrayCols, _arrayRows)
print("Data:")
print(_data); print()

_rollData = rw.rolling_window(_data, (_nRollingWindow, _nRollingWindow))
print("Window data:")
print(_rollData); print()

_rollData = np.asarray(_rollData).reshape(-1, _nRollingWindow ** 2)
print("Reshaped window data:")
print(_rollData); print()

_rollDataMean = np.mean(_rollData, axis = 1)
print("Roll data mean:")
print(_rollDataMean); print()

_rollDataMean = _rollDataMean.reshape(_arrayCols - (_nRollingWindow - 1), _arrayRows - (_nRollingWindow - 1))
print("Reshaped roll data mean:")
print(_rollDataMean); print()