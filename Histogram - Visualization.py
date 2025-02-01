import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##Call on the excel data
df = pd.read_excel("Thesis Data.xlsx", "Sheet2")

##Relax the limit on display columns and rows
pd.set_option("display.max_columns", 2)
pd.set_option("display.max_rows", 13)

#This enters the data frame and lets you select a specific column
WBC = df["WBC"]
#This lets you preview the data, helps in the instances of many samples
print(WBC.head())
#Prints the entirety of that column
print(WBC)
print(df)

sns.histplot(WBC,bins=30, kde=True, color="lightgreen", edgecolor="blue")
plt.xlabel('WBCs (10^3/uL)')
plt.ylabel('# of individuals')
plt.title('White Blood Cells')
plt.show()