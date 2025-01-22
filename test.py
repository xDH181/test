import numpy as np
arr = np.array([[0,6,7], [2,4,5],[3,1,8]])
shift_arr = np.roll(arr,1,axis=0)
shift_arr = np.roll(shift_arr,1,axis=1)
print(shift_arr)