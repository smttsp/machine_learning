import pandas
import matplotlib.pyplot as plt

train = pandas.read_csv("data/train.csv")
test = pandas.read_csv("data/test.csv")


def show_dist(df, col_name):
    bins = max(len(df[col_name].unique()), 20)
    plt.hist(df[col_name].dropna(), bins=bins, edgecolor="k")
    plt.xlabel(col_name)
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {col_name}")
    plt.show()


# "Cabin"

cols = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

for col in cols:
    show_dist(train, col)

print(train.head())
