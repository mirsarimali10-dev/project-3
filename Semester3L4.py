import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
data = pd.read_csv("vgsales.csv")
formula = data.groupby("Platform")["Global_Sales"].sum().head(10).sort_values(ascending=True)
plt.figure(figsize=(30,5))
plt.bar(formula.index, formula.values, color="orange")
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Global Sales of each Platform")
plt.show()

plt.figure(figsize=(10,5))
formula2 = data["Platform"].head(5)
sns.countplot(data=data, x=formula2)
plt.xlabel("Platform")
plt.ylabel("Count")
plt.title("Platform Count")
plt.show()