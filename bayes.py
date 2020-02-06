#!/usr/bin/env python
# coding: utf-8

# In[66]:


import numpy as np
import matplotlib.pyplot as plt

def prior(H):
    
    P = np.ones(len(H))
    
    return P

def likelihood(chain,H):
    
    np.ones(len(H))    
    N_c = chain.count('c')    
    N_s = chain.count('s')    
    L = (H**N_c)*((1-H)**N_s)
    
    return L

def post(H,chain):
    
    P = likelihood(chain,H)*prior(H)
    
    return P/np.trapz(P,H)

chain = 'scccc'

H = np.linspace(0.001,0.999,100)


post = post(H,chain)



def sigma(x,y):
    
    delta = x[1]-x[0]
    H_o_i = np.argmax(y)
    
    sig = (y[H_o_i+1]-2*y[H_o_i]+y[H_o_i-1])/(delta**2)
    
    return x[H_o_i], (-sig)**(-0.5)
                      
                      
max, sigma_m = sigma(H,np.log(post))

approx = (1.0/np.sqrt(2.0*np.pi*sigma_m**2))*np.exp(-0.5*(H-max)**2/(sigma_m**2))

print(sigma(H,post))
plt.figure()
plt.plot(H,post,label='e')
plt.plot(H,approx,label='a')
plt.ylabel('prob(H|datos)')
plt.xlabel('H')
plt.leyend()

    


    


# In[ ]:




