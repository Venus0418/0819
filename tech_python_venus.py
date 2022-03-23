import numpy as np
import math
vectorTgt  = np.array([0.35389,0.93376,-0.05330]).reshape(1,3)
vectorData = np.array([0.45379,0.33476,0.02231],
            [-0.35369,0.75374,-1.42330],
            [1.22449,0.88172,0.01334], 
            [0.38982,-0.72371,-0.22349], 
            [-0.01389,0.91296,0.14830], 
            [0.25343,-0.12377,-0.08331], 
            [0.66382, 0.92335,-0.13356]).reshape(7,3)
for b in vectorData:
    dot= 0
    for i in [0,1,2]:
        dot = dot + vectorTgt[0]*b[0]
    if dot<0:
        print(b)