import json
from collections import Counter
from pandas import DataFrame,Series
import pandas as pd
import  numpy as np
from pylab import *
path = "usagov_bitly_data2012-03-16-1331923249.txt"
lFile=open(path)
#line = lFile.readline()

#print(line)
records = [json.loads(line) for line in lFile]
'''
#print(json.dumps(records[0],sort_keys=True,indent= 4,separators=(',', ': ')))
print(records[0]['tz'])
time_zones = [rec['tz'] for rec in records if 'tz'in rec]
print (time_zones)
print(json.dumps(time_zones[:10],sort_keys=True,indent= 4,separators=(',', ': ')))
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts :
            counts[x] +=1
        else :
            counts[x]= 1
    return counts
counts = get_counts(time_zones)
print(counts ['America/New_York'])
def top_counts (count_dict,n=10):
    value_key_pairs = [(count,tz)for tz,count in count_dict.items() ]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
counts = Counter(time_zones)
x=json.dumps(counts.most_common(10),sort_keys=True,indent= 4,separators=(',', ': '))
print(x)
'''
frame = DataFrame (records)
tz_counts = frame['tz'].value_counts()
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz== ''] ='Unkonwn'
tz_counts=clean_tz.value_counts()
tz_counts[:10].plot(kind ='barh',rot=0)


