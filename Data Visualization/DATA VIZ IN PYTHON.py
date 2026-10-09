# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC # 24/08/2026
# MAGIC #Data Visualization in python

# COMMAND ----------

# MAGIC %md
# MAGIC #Matplotlib
# MAGIC
# MAGIC Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible.

# COMMAND ----------

# MAGIC %md
# MAGIC #Data ingestion
# MAGIC
# MAGIC import libraries

# COMMAND ----------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# COMMAND ----------

df= spark.table("bright_.coffee.cleaned_data")

display(df)

# COMMAND ----------

df=df.toPandas()

display(df)

# COMMAND ----------

plot_data = df.groupby(["dayname_of_sale", "store_location"])["revenue"].sum().unstack(fill_value=0)
display(plot_data)

# COMMAND ----------

import matplotlib.pyplot as plt

#ax- axes
# fig- figure


# Create stacked bar chart
ax = plot_data.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 6)
)

# Add data labels
for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.0f",
        label_type="center"
    )

# Labels and title
plt.xlabel("Day of Week")   #x-axix title
plt.ylabel("Total Revenue") #y-axis title
plt.title("Total Revenue by Day and Store Location")    #chart title
plt.legend(title="Store Location")  #legend

plt.tight_layout()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC # new basic example

# COMMAND ----------

import matplotlib.pyplot as plt

# COMMAND ----------

days=  ["Mon","Tues","Wed","Thur","Fri"]
revenue= [100,150,120,180,200]

plt.plot (days,revenue)         #creates a line graph

plt.ylabel("Revenue")
plt.xlabel("Day of week")
plt.title("Daily revenue")
plt.show()