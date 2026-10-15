# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %md
# MAGIC #Data Visualization 
# MAGIC (08/10/2026)

# COMMAND ----------

# MAGIC %md
# MAGIC #basic line graph 

# COMMAND ----------

import matplotlib.pyplot as plt

#1 create a sample data for a line graph
x=[1,2,3,4,5]
y=[2,4,3,5,7]

#2 create a line plot
plt.plot(x,y, marker= "o")

#Add labels and titles
plt.title("My first graph")
plt.xlabel("my X")
plt.ylabel("my Y")

#Adding data labels
for i in range(len(x)):
    plt.text(x[i], y[i],f"({x[i]},{y[i]})")

#Display the graph
plt.show

# COMMAND ----------

import matplotlib.pyplot as plt

#Step 1: create sample data
fruits=["Apples","Bananas","Cherries","Kiwi"]
quantity= [10,15,7,12]

#Step 2: create a bar chart 
plt.bar(fruits,
        quantity)

#Step 3: Add labels
plt.title("Fruit Quantities")
plt.xlabel("fruits")
plt.ylabel("quantity")

#Step 4: show the graph
plt.show()

# COMMAND ----------

import matplotlib.pyplot as plt

#Step 1: create sample data
fruits=["Apples","Bananas","Cherries","Kiwi"]
quantity= [10,15,7,12]

#Step 2: create a pie chart
plt.pie(quantity,
        labels=fruits)

plt.title("Fruits distribution")

#display pie chart
plt.show()