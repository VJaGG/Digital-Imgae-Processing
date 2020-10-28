import numpy as np


src = np.array([[123, 234, 68], [33, 51, 17], [48, 98, 234],
                [129, 89, 27], [45, 167, 134]])

src[src > 150] = 255
src[src <= 150] = 0
print(src)
