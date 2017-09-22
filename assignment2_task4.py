import numpy as np         ##import numpy as np
a = np.random.random(15)   ## 15 random numbers
a[a.argmax()] = 100        ## this function searches for maximum value and replaces by 100
print(a)



