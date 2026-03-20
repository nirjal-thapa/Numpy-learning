#creating arrays from python list with:
#np.array([ele1,ele2,ele3])

import numpy as np
arr=np.array([1,2,3,4])
print(arr)


#with default value
#np.zeros(shape) (3) for id,(3,3) 2d

# import numpy as np
zeroes_array=np.zeros(3)
print(zeroes_array)

#ones(shape)

ones_array=np.ones((2,3))
print(ones_array)

#anny number(filled array)
#np.full(shape,value)
filled_array=np.full((2,2),7)
print(filled_array)