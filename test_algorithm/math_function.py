laser_range = [0.1, 0.2, 0.3, 0.4, 0.5]

import numpy as np
laser_arr = np.array(laser_range)

# 일치하지 않으면 모두 0으로 바꾸고, 일치하는 수는 그대로 두는 기능
result = np.count_nonzero(laser_arr >= 0.2)
print(result)