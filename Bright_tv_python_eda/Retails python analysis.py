# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC # Retails analysis

# COMMAND ----------

import pandas as pd

# COMMAND ----------

df=pd.read_csv("/Workspace/Users/nomvelogcaba@gmail.com/Pandas Class notes/1776798890834_retail_sales_dataset.csv")
#creating a dataframe from the csv file

# COMMAND ----------

df.head(5)   #displays the first 5 rows of your table

# COMMAND ----------

df.tail(5)  #displays the bottom 5 rows of your table

# COMMAND ----------

df.shape #shows the number of rows and columns 

# COMMAND ----------

df.describe()     #extract the summary of stats from the numerical data

# COMMAND ----------

df.describe().T         #(transpose)Same as above table just different style/format

# COMMAND ----------

df.isnull()     #Check for null values in table.  FALSE= not a null, TRUE= Null value. 
                #notice how the first row starts with a ZERO- This references an index.

# COMMAND ----------

df.isnull().sum()   #counts the number of NULL values in your data/all columns

# COMMAND ----------

df.info()

# COMMAND ----------

df.duplicated()    #checks for duplicates in each row. FALSE= no duplicate. TRUE= duplicated row

# COMMAND ----------

df.duplicated().sum()   #gives the sum of the number of duplicated rows in table

# COMMAND ----------

print(df.index)     #describes the index of your data. Indicies helps us locate specific information in our data.

# COMMAND ----------

my_cars=['bmw','merc','toyota']     #type- list. We are testing the index method

# COMMAND ----------

print(my_cars[0])   #0- is the first value/code. So the first item on the list of my_cars matches 'BMW'

# COMMAND ----------

print(my_cars[1])       #Merc represents row 2/ or 2nd value from the list.

# COMMAND ----------

df.count()          #counts the number of non null values in each column

# COMMAND ----------

df["Product Category"]      #to select a column

# COMMAND ----------

df["Product Category"].unique()         #select distinct values from column

# COMMAND ----------

df["Gender"].unique()   #shows unique cataegories under selected column/ select distinct values to a specific column

# COMMAND ----------

df["Product Category"].value_counts()       #counts the distinct value as well as the number of times that value appears

# COMMAND ----------

display(df)             #display full table/ SELECT*

# COMMAND ----------

y=["a","b","c"]

Y=("A","B","C")

x={"a","b","c"}

# COMMAND ----------

type(y)

# COMMAND ----------

type(Y)

# COMMAND ----------

type(x)