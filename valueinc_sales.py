# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 21:22:43 2023

@author: user
"""

import pandas as pd

# file_name=pd.read_csv('file.csv') format of read_csv

data=pd.read_csv('transaction.csv')

data=pd.read_csv('transaction.csv',delimiter=';')

#Summary of the Data

data.info()

# Working with Calculation
#Defining Variables

Cost_Per_Item=11.73
Selling_Price_Per_Item=21.11
Number_Of_Item_Purchase=6

#Mathematical Operation on pandas

Profit_Per_Item=21.11-11.73
Profit_Per_Item=Selling_Price_Per_Item-Cost_Per_Item

Profit_Per_Transaction=Number_Of_Item_Purchase*Profit_Per_Item

Cost_Per_Transaction=Cost_Per_Item*Number_Of_Item_Purchase

Selling_Price_Per_Transaction=Selling_Price_Per_Item*Number_Of_Item_Purchase

#Cost per Transaction Column Calculation

#Cost_Per_Transaction=Cost_Per_Item*Number_Of_Item_Purchase

# Variable=dataframe['column_name']

data['Cost Per Transaction']=data['CostPerItem']*data['NumberOfItemsPurchased']

data['Selling Price Per Tansaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']
                                                                     
data['Profit per Transaction']=data['Selling Price Per Tansaction']-data['Cost Per Transaction']

data['Mark up per Transaction']=(data['Selling Price Per Tansaction']-data['Cost Per Transaction'])/data['Cost Per Transaction']

#Rounding Marking

roundmarkup=round(data['Mark up per Transaction'],2)

data['Mark up per Transaction']=round(data['Mark up per Transaction'],2)

#checking column Data Type
data['Day'].dtype

#Change Columns type

day=data['Day'] .astype(str)
Year=data['Year'].astype(str)
Year.dtype
day.dtype

my_date= day+'-'+data['Month']+'-'+Year

data['Date']=my_date

#Using iloc to view Column/Rows
data.iloc[0] #views the rows with index=0
data.iloc[0:3]#views the first three rows
data.iloc[-5:] #the last five rows

data.head[5]#first 5 rows

data.iloc[:,2]#all rows on the 2nd column

data.iloc[4,2]# brings in 4th row and 2nd column

#Using Split to split the Client Keywords
#new_var=column.str.split('delimiter',expand=True)

split_col=data['ClientKeywords'].str.split(',',expand=True)

#Creating new Columns for Split Column

data['ClientAge']=split_col[0]
data['ClientType']=split_col[1]
data['LengthofContract']=split_col[2]

#Using the replace function
data['ClientAge']=data['ClientAge'].str.replace('[','')
data['LengthofContract']=data['LengthofContract'].str.replace(']','')


#using the lower function to change item to lower case

data['ItemDescription']=data['ItemDescription'].str.lower()

#How to Merge File
#Bringing in the new Data Set

value_inc=pd.read_csv('value_inc_seasons.csv',delimiter=';')

#Merging Files:merge_df=pd.merge(df.old,df.new,on='key')

data=pd.merge(data,value_inc,on='Month')

#Dropping Columns
#df=df.drop['Columnname',axis=1]

data=data.drop('ClientKeywords',axis=1)
data=data.drop('Day',axis=1)
data=data.drop(['Year','Month'],axis=1)

#export into a CSV

data.to_csv('ValueInc_Cleaned.csv',index=False)


    





























































