import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


path = "C:\\Users\\30448\\Documents\\Kaggle\\SFsalaries"
df = pd.read_csv( path + "\\input\\salaries.csv")

print df.shape
print df.head()
#print df.describe()
print df.info()


#name analysis  most common first/last name. correlation with salary
df["namelength"] = df["EmployeeName"].apply(lambda x:len(x.split()))
df["compoundName"] = df["EmployeeName"].apply(lambda x: 1 if "-" in x else 0 )
pd.Series(df["compoundName"]).value_counts().plot(kind = "pie" , title = "compound name" , autopct='%.2f') #ccompound means has "-" 
print df["namelength"].value_counts()
#just for fun see the longest name:
print df.sort_values( by = "namelength" , ascending = False)["EmployeeName"][:10]

#last name
def lastName(x):
    sp = x.split()
    if sp[-1].lower() == "jr":
        return sp[-2]
    else:
        return sp[-1]  
        
df["lastName"] = df["EmployeeName"].apply(lastName)
plt.figure()
sns.countplot(y = "lastName" , data = df , order=df["lastName"].value_counts()[1:10].index)

#first name
df["firstName"] = df["EmployeeName"].apply(lambda x:x.split()[0])
plt.figure()
sns.countplot(y = "firstName" , data = df , order=df["firstName"].value_counts()[1:10].index)

# exact same name
plt.figure()
sns.countplot(y = "EmployeeName" , data = df , order=df["EmployeeName"].value_counts()[1:10].index)

plt.figure()
#pre-processing the salaries: replacing NaN and strings by median
salary_types = ["BasePay" , "OvertimePay" , "OtherPay" ,"Benefits" , "TotalPay" ]
colors = ['b', 'r' , 'g' ,'k' , 'y' ]
for i,salary in enumerate(salary_types):
    df[salary] = df[salary].fillna("Not Provided")
    median = np.median([int(x) for x in df[salary] if not (type(x) == str)])    
    df[salary] = df[salary].apply(lambda x: median if (type(x) == str) else int(x))
    ax = sns.kdeplot(df[salary] , color = colors[i] )
    ax.set_xlim(-100000,100000)
    




#hii = plt.hist(df["BasePay"] , bins = 10 )
#hi = pd.DataFrame(hii[0], columns = ["frequency" ])
#
#def numberToBin(x):
#    bins = []
#    for i in range(len(x)-1):
#        bins.append(str(int(x[i])) + " - " + str(int(x[i+1])))
#    return bins
#    
#hi["bins"] = numberToBin(hii[1])



