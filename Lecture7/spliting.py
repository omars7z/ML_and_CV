import pandas as pd

df = pd.read_csv("diabetes.csv")
x = df.drop(columns=['Outcome'])
y = df["Outcome"]

idx = range(x.shape[0])
xtrainnums = int(0.8 * x.shape[0])
ytrainnums = int(0.8 * y.shape[0])
xtestnums = int(0.2 * x.shape[0])
ytestnums = int(0.2 * y.shape[0])

x_train = x[: xtrainnums]
y_train = y[: ytrainnums]
# y_train = y[: (y.shape[0] - 100)]

# x_test = x[(x.shape[0] - 100):]
# x_test = x[(x.shape[0] - 100):]
x_test = x[xtestnums:]
y_test = y[ytestnums:]

print(x_train.shape)
print(y_train.shape)

print(x_test.shape)
print(y_test.shape)