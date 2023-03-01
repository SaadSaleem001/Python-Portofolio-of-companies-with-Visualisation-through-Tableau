# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 01:18:48 2023

@author: user
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

json_file=open('loan_data_json.json')
data=json.load(json_file)

#transform to data frame
loandata=pd.DataFrame(data)

#finding Unique Value for Purpose Column
loandata['purpose'].unique()

#Describing The Data
loandata.describe()

#Describe a data for a particular column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using exp to get the annual income
income=np.exp(loandata['log.annual.inc'])
loandata['AnnualIncome']=income

#Working with arrays
arr=np.array([1,2,3,4])

#0D Array
arr=np.array([43])

#2D Array
arr=np.array([[1,2,3],[4,5,6]])

#Working with if Statements
a=40
b=500

if b>a:
    print('b is greater than a')
    
#let add more conditions

a=40
b=500
c=1000

if b>a and b<c:
    print('b is greater than a but less than c')
    
#What if condition is not met

a=40
b=500
c=20

if b>a and b<c:
   print('b is greater than a but less than c')  
else:
    print('No Condition Met')

#another condition different matrices

a=40
b=500
c=30

if b>a and b<c:
    print('b is greater than a but less than c')
elif b>a and b>c:
    print('b is greater than a and c')
else:
    print('No Condition Met')

#using or
a=40
b=500
c=30

if b>a or b<c:
    print('b is greater than a but less than c')
else:
    print('No Condition Met')
    
#another condition different matrices No.2

a=40
b=0
c=30

if b>a and b<c:
    print('b is greater than a but less than c')
elif b>a and b>c:
    print('b is greater than a and c')
else:
    print('No Condition Met')
    
    
#Fico Score

fico=250

# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'

if fico>=300 and fico<400:
    ficocat='Very Poor'
elif fico>=400 and fico<600:
    ficocat='Poor'
elif fico>=601 and fico<660:
    ficocat='Fair'
elif fico>=660 and fico<780:
    ficocat='Good'
elif fico>=780:
    ficocat='Excellent'
else:
    ficocat='Unknown'
print(ficocat)

#for loops

fruits=['Apples','Pear','Bananas','Cherry']

for x in fruits:
    print(x) 
    y=x+'fruit'
    print(y)
    
for x in range(0,3):
    y=fruits[x]+' for sale'
    print(y)

#applying for loops to loan data

#using first 10
length=len(loandata)
ficocat=[]
for x in range(0,length):
    category=loandata['fico'][x]
    if category>=300 and category<400:
        cat='Very Poor'
    elif category>=400 and category<600:
        cat='Poor'
    elif category>=601 and category<660:
        cat='Fair'
    elif category>=660 and category<700:
        cat='Good'
    elif category>=700:
        cat='Excellent'
    else:
        cat='Unknown'
    ficocat.append(cat)
        
ficocat=pd.Series(ficocat)

loandata['fico.caegory']=ficocat
    

#applying try and except statement 

#using first 10
length=len(loandata)
ficocat=[]
for x in range(0,length):
    category=loandata['fico'][x]
    try:
        if category>=300 and category<400:
            cat='Very Poor'
        elif category>=400 and category<600:
            cat='Poor'
        elif category>=601 and category<660:
            cat='Fair'
        elif category>=660 and category<700:
            cat='Good'
        elif category>=700:
            cat='Excellent'
        else:
            cat='Unknown'
    except:
        cat='Unknown'
    
    ficocat.append(cat)
        
ficocat=pd.Series(ficocat)

loandata['fico.caegory']=ficocat
    
#df.loc as a conditional statement
#df.loc[df[columnname]condition,newcolumnname]='Value if the the condition is met

#for the interest rate,a new column is wanted,rate is>0.12 then high,else low

loandata.loc[loandata['int.rate']>0.12,'int.rate.type']='High'
loandata.loc[loandata['int.rate']<0.12,'int.rate.type']='Low'

#number of loans/rows by fico.category

catplot=loandata.groupby(['fico.caegory']).size()
catplot.plot.bar(color='green',width=0.1)
plt.show()

catplot2=loandata.groupby(['purpose']).size()
catplot2.plot.bar(color='red',width=0.4)
plt.show()


#scatterplot

ypoint=loandata['AnnualIncome']
xpoint=loandata['dti']
plt.scatter(xpoint,ypoint,color='red')
plt.show()

#writing to csv
loandata.to_csv('Loan_Cleaned.csv',index=True)
















































