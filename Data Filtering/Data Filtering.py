# Databricks notebook source
# MAGIC %md
# MAGIC #Data Filtering
# MAGIC 16/09/2026
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC - To filter data you need to specify conditions
# MAGIC - This will reduce the rows in your data
# MAGIC - Affects the rows. You filter based on columns, but the outcome affects the rows.
# MAGIC - Example from an employees table with columns: (name, age, city, salary):
# MAGIC
# MAGIC     - filter people older than 30 years:
# MAGIC     code: df[df["age"]>30]
# MAGIC     outcome: all rows of people older than 30, all columns included, UNLESS OTHERWISE SPECIFIED.
# MAGIC
# MAGIC     - filter by an exact value, remember the "=="
# MAGIC     code: df[df["city"]=="Joburg"]
# MAGIC     outcome: all rows and columns of people who live in Joburg
# MAGIC
# MAGIC     == means EQUAL TO: used to compare exact values
# MAGIC
# MAGIC     != means NOT EQUAL TO
# MAGIC     
# MAGIC     - filter using multiple conditions
# MAGIC         - &: AND - Both conditions must be true
# MAGIC         - |: OR - at least one condition must be true
# MAGIC
# MAGIC     Code for AND logical operator:
# MAGIC     df[(df["age"]>25) & (df["salary"]>300)] 
# MAGIC     - The outcome will filter for rows where columns are age>25 and salary>300
# MAGIC
# MAGIC     Code for OR logical operator
# MAGIC     df[(df["city"]=="Joburg")|(df["age"]>30)]
# MAGIC     - The outcome will have rows either having the city name "Joburg" or where the age is 30
# MAGIC
# MAGIC     - Filter using a list of values
# MAGIC
# MAGIC     Code for is IN [.isin()]:
# MAGIC     df[df["city"].isin(["Joburg","CPT"])]
# MAGIC     - The outcome will have rows where the city name is "Joburg" and "CPT"
# MAGIC
# MAGIC     Code for is NOT [~]:
# MAGIC     df[~df["city"].isin(["Joburg","CPT"])]
# MAGIC     - The outcome will be of rows where the city is NOT "Joburg" and "CPT"
# MAGIC
# MAGIC     - Filter data within a range
# MAGIC     Code for BETWEEN operator
# MAGIC     df[df["age"].between(0, 30)]
# MAGIC     - The outcome will be for ALL the rows where age is equal to zero to and greater than zero, and where the age is equal to and less than 30
# MAGIC
# MAGIC     - Filter for misssing values
# MAGIC     Code for IS NULL
# MAGIC     df[df["salary"].isna()]
# MAGIC     - The outcome will be of rows where the salary has missing values
# MAGIC
# MAGIC     - Filter rows with values/ IS NOT NULL
# MAGIC     df[df["salary"].notna()]
# MAGIC     - The outcome will be of rows where the salary is available
# MAGIC

# COMMAND ----------

