#!/usr/bin/env python
# coding: utf-8

# In[18]:


def suspense_text(text):
    from time import sleep
    import sys
    for x in text:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)

