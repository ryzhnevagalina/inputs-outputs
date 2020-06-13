#!/usr/bin/env python
# coding: utf-8

# In[ ]:


price = list(map(int, input().split())) 
discount = list(map(int, input().split())) 
price_min = price[0] 
discount_min = discount[0] 
minimum = price_min*(100 - discount_min) 
for a in range(1, len(price)): 
    if (price[a]*(100-discount[a])) <= minimum: 
        minimun = price[a]*(100-discount[a]) 
        pricemin = price[a] 
        discount_min = discount[a] 
print(price_min, discount_min)

