import numpy as np
import time
import sys
s=1000000
l1=range(s)
l2=range(s)
a1=np.arange(s)
a2=np.arange(s)
s1=time.time()
res=[(x,y) for x,y in zip(l1,l2)]
print((time.time()-s1)*1000)
s1=time.time()
res=a1+a2
print((time.time()-s1*1000))
