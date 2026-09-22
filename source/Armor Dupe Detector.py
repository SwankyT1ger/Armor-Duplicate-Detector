import pandas as pd
import numpy as np
import pyperclip

df = pd.read_csv("destiny-armor.csv", usecols=['Name','Id','Tier','Archetype','Tertiary Stat','Tuning Stat','Perks 0','Perks 1','Perks 3','Perks 4','Perks 5','Perks 6','Perks 7','Perks 8','Perks 9'])
df.columns.str.strip()

df = df[~df.apply(lambda r: r.str.contains('Spirit of').any(), axis=1)]

df1 = df.loc[df.duplicated(subset=['Name','Archetype','Tertiary Stat','Tuning Stat'], keep="first")]

df1.to_numpy()

dupes = np.array(df1)

IDs = (dupes[:,1])

IDs = ['id:{}'.format(i) for i in IDs] #can you use numpy to string specific array column here?

df2 = pd.DataFrame(data=IDs)

df2 = df2.map(lambda x: x.replace('"', ''))

string = df2.to_string(header=False,index=False)

string = ' or '.join([string[i:i+22] for i in range(0, len(string), 23)])

print(string)

pyperclip.copy(string)