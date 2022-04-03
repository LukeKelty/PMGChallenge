#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sys
import os


# In[8]:


class fileCombiner:
    def checkPath(argv):
        if len(argv) < 1:
            print("No filepath found")
            return False
        filelist = argv[1:]
        for filepath in filelist:
            if not os.path.exists(filepath):
                print("This file does not exist. Please check your path spelling")
                return False
            if os.stat(filepath).st_size == 0:
                print("This is an empty file, and will cause run time errors")
                return False
        print("File path is good")
        return True
    def combine(self, argv: list):
        if self.checkPath(argv):
            filelist=argv[1:]
            arr = []
            reader = pd.read_csv(filePath,chunksize=1000000,low_memory=False,header=0)
            for filepath in filelist:
                for chunk in reader:
                    filename = os.path.basename(filepath)
                    chunk['filename'] = filename
                    arr.append(chunk)
            header = True
            for chunk in arr:
                print(chunk.to_csv(index=False, header=header, line_terminator='\n', chunksize=chunksize), end='')
                header = False
        else:
            return
        
def main():
    obj = fileCombiner()
    obj.combine(sys.argv)

if __name__ == '__main__':
    main()
    


# In[ ]:




