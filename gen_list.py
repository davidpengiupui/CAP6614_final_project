#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


dataset = 'office'


# In[3]:


if dataset == 'office':
	domains = ['amazon', 'dslr', 'webcam']
elif dataset == 'office-caltech':
	domains = ['amazon', 'dslr', 'webcam', 'caltech']
elif dataset == 'office-home':
	domains = ['Art', 'Clipart', 'Product', 'Real_World']
elif dataset == 'image-clef':
	domains = ['c', 'i', 'p']
elif dataset == 'VISDA-C':
	domains = ['train', 'validation']
else:
	print('No such dataset exists!')


# In[4]:


for domain in domains:
	log = open(dataset+'/'+domain+'_list.txt','w')
	directory = os.path.join(dataset, os.path.join(domain,'images'))
	classes = [x[0] for x in os.walk(directory)]
	classes = classes[1:]
	classes.sort()
	for idx,f in enumerate(classes):
		files = os.listdir(f)
		for file in files:
			s = os.path.abspath(os.path.join(f,file)) + ' ' + str(idx) + '\n'
			log.write(s)
	log.close()


# In[ ]:





# In[ ]:




