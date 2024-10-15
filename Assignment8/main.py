import numpy as np 

data = np.random.exponential(2, 1000)

mean = sum(data)/1000


print(mean)