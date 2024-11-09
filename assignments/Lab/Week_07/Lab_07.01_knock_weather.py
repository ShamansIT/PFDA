import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
 
df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv", 
skiprows=19) 
print(df.head(3)) 

corrtemp = df["month"].corr(df["meant"]) 
print(corrtemp)

cleandf = df[["month","wdsp"]] 

cleandf.dropna(inplace=True) 

cleandf['wdsp']= cleandf.loc[:,('wdsp')].replace(' ', np.nan) 
cleandf.dropna(inplace=True) 

cleandf['wdsp'] = cleandf['wdsp'].astype(float) 

corrwind = cleandf["month"].corr(cleandf["wdsp"]) 
print (f"wind correlation {corrwind}") 

sns.set_style('whitegrid') 
#sns.scatterplot(x='total_bill',y='tip',data=dataset) 
sns.lmplot(x='month', y='wdsp', order=3, data=cleandf) 
plt.show() 