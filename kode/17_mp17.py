import matplotlib.pyplot as plt
import numpy as np

ran = np.random.randint(0,100,100)
print(ran)

'''
Data yang tergenerate
[ 5 70 92  4 79 81 28 44 56 47 46 40 32  0 25 61 30 27 98 81 85 
41 61 55 98 75 81 35 86 83 12 27 67 92 10 63  3 72 51 22 77 84 92 
26 24 77 13 20 93  1 1 31 25 88 56 99 85 13 68 72 82 10 43 30 80 
34 50 61 48 29  3 11 56 16 24 14  0 62 32 93 86 73 11 33 88 57 10 
85 27 62 63 22 99 63 61 32 67 83 57 43]
'''

plt.hist(ran, bins=100, color='k')
plt.show()
