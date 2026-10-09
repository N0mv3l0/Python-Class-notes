# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC ### JOINS

# COMMAND ----------

# Reading a delta table stored in the databricks catalog- To be read as a "spark table".

profiles= spark.read.table("bright.bright_tv.bright_tv_dataset_user_profiles")

display(profiles.limit(10))

# COMMAND ----------

#convert the user_profiles to a pandas dataframe to use pandas functions

user_profiles = profiles.toPandas()

display(user_profiles)

# COMMAND ----------

viewership= spark.read.table("bright.bright_tv.bright_tv_dataset_viewership")

display(viewership.limit(5))

# COMMAND ----------

view= viewership.toPandas()

#to coalesce or combine 2 columns
#df["combined"]= df["col1"].combine_first(df["col2"])

view["UserID"]= view["UserID0"].combine_first(view["userid4"])


# to drop the old column if they are no longer needed
#df=df.drop(columns=["col1", "col2"])

view=view.drop(columns=["UserID0", "userid4"])


#the new table
display(view)



# COMMAND ----------

# MAGIC %md
# MAGIC # left join with same column names
# MAGIC
# MAGIC use code-
# MAGIC
# MAGIC result= pd.merge(table_1, table_2, on= "column_name", how= "left")

# COMMAND ----------

# MAGIC %md
# MAGIC # left join on 2 different column names
# MAGIC
# MAGIC use code-
# MAGIC
# MAGIC result= pd.merge(df_left, df_right, left_on="column_name", right_on="column_name", how="left")

# COMMAND ----------

import pandas as pd
import numpy as np

bright_df= pd.merge(view, user_profiles, left_on="UserID", right_on="UserID", how="left")

display(bright_df)


# COMMAND ----------

bright_df.columns

# COMMAND ----------

bright_df.info()

# COMMAND ----------

#selecting distinct or unique columns from table

distinct_provinces= bright_df["Province"].unique()

print(distinct_provinces)

# COMMAND ----------

bright_df.duplicated().sum() #gives the total sum of NULL values in the table

# COMMAND ----------

bright_df.duplicated() #searches each row and gives the sum of null values in a booleon. FALSE= No NULL value

# COMMAND ----------

#Check for duplicate UserIDs
#This is the Pandas equivalent of GROUP BY UserID HAVING COUNT(*)>1.

#Count total duplicated rows
print(view.duplicated().sum())

#extract and view the actual duplicated rows
print(view[view.duplicated()])

# COMMAND ----------

view= view.drop_duplicates() #to delete duplicates from the table

# COMMAND ----------

#measure the size of the merged table

number_of_rows= len(bright_df)
number_of_subs= bright_df["UserID"].nunique(dropna=True)

print("Number of rows:", number_of_rows)
print("Number of unique subscribers:", number_of_subs)

# COMMAND ----------

#Gender check on merged table

# show all distinct gender values before cleaning.

display(bright_df["Gender"].drop_duplicates().to_frame(name="Gender"))