#!/usr/bin/env python
# coding: utf-8

# In[1]:


def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")

