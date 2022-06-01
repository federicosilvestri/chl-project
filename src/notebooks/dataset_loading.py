#!/usr/bin/env python
# coding: utf-8

# # Testing dataset loading
# 
# This notebook contains code that run the pipeline we have created to analyze a set of datasets.

# In[1]:


# adding the project root inside the python path
import sys
import os

sys.path.insert(0, os.path.abspath('..'))


# In[2]:


# The path where the dataset are stored
DATASET_PATH: str = "../../dataset/first_disease_sel/"
DISEASE_COLNAME: str = 'DISEASE'


# In[3]:


from analysis.dataset import load_datasets, compute_ds_col_intersection, clean_datasets, build_dataset, scale_minmax


# ### Load datasets

# In[4]:


# Load dataset
datasets = load_datasets(DATASET_PATH)
# compute intersection
colname_intersection = compute_ds_col_intersection(datasets)
# clean datasets
datasets = clean_datasets(datasets, colname_intersection)


# 

# ## Scaling

# In[ ]:


scale_minmax(datasets)


# ## Building unique DS

# In[ ]:


# finally build the unique dataset
dataset = build_dataset(datasets)
dataset


# ## Inspecting dataset we have built

# In[ ]:


dataset['DISEASE']


# In[ ]:


# plotting the number of sample for each disease
disease = dataset['DISEASE'].value_counts()
print(disease)
disease.plot.bar()


# In[ ]:


import matplotlib.pyplot as plt
from bioinfokit import analys, visuz
import numpy as np


# In[ ]:


visuz.gene_exp.hmap(df=dataset.astype(float), rowclus=False, colclus=False, dim=(10, 10), tickfont=(2, 4), show=True)

