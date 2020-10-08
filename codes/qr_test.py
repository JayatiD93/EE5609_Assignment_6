import numpy as np
m = np.array([[55,-60],[-60,20]])
print("Original matrix:")
print(m)
result =  np.linalg.qr(m)
print("Decomposition of the said matrix:")
print(result)
