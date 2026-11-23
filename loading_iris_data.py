# Import the library
from sklearn.datasets import load_iris
iris = load_iris()
print("Dataset loaded successfully!")
print(iris.data)
print("Feature names:")
print(iris.feature_names)
print("Flower species:")
print(iris.target_names)
print("Dataset shape:", iris.data.shape)

##using pandas
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in iris.target]

# Show the first 10 rows
display(df.head(10))

# Corrected 'tile' to 'tail' to show the last 10 rows
display(df.tail(10))

# Corrected spelling from 'discribe' to 'describe'
display(df.describe())
