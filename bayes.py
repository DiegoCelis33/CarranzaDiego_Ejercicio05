#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[10]:


x = 'cscscccscccscscsccccssscssccs'


# In[53]:


count_c = x.count('c')

count_s = x.count('c')

H = np.linspace(0,1, 100)

prior = np.ones(len(H))

verosimilitud= H**count_c*(1-H)**count_s

P_f = prior*verosimilitud

plt.figure()
plt.plot(H,P_f/(np.sum(verosimilitud)))




plt.savefig('bayes.png')


# In[ ]:





# In[ ]:




