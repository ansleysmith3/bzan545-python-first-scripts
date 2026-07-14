import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Object Oriented Programming (OOP) - nouns have verbs
    #df.head()
#Functional programming - verbs applied to nounsn(ex: R)
    #head(df)

orders = pd.read_csv("data/orders.csv")

print("First rows")
print(orders.head())

print("Rows and columns")
print(orders.shape)

sns.scatterplot(x="quantity", y="order_total", hue="category", data=orders)
plt.show()


#####push test