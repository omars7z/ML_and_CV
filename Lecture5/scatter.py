import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")
df.plot.scatter(x="BMI", y="Age")
plt.show()

print(df.head())
print(df.describe())

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
<<<<<<< HEAD
 #with
=======
 #3d model
>>>>>>> 5fda5813c80783d234a287fe8639a8a383dbb734
ax.scatter( df["BMI"], df["Age"], df["BloodPressure"])
plt.xlabel('BMI', fontsize=18)
plt.ylabel('Age', fontsize=18)

plt.show()

