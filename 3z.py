import numpy as np
for n in np.arange(1,100):
    if n % 3 == 0:
    	print  (str("Fizz"))
    elif n % 5 == 0:
    	print  (str("Buzz"))
    elif (n % 3 == 0) and (n % 5 == 0):
    	print (str ("FizzBuzz"))
    else:
    	print  (str (n))
    	print (n)
