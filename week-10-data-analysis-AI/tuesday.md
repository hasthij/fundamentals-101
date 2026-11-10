import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# lets pandas dates plot properly in matplotlib
pd.plotting.register_matplotlib_converters()

print("setup complete")

melbourne_file_path = './data/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 

#summarize the data
melbourne_data.describe()
melbourne_data.columns
#used to drop not available values
melbourne_data = melbourne_data.dropna(axis=0)
print(melbourne_data.columns)
#prediction target notation is by standard y
y = melbourne_data.Price

#setting up features to use later on for prediction
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
#by convention features are denoted by X
X = melbourne_data[melbourne_features]
X.describe()
#using scikit-learn to build the model
from sklearn.tree import DecisionTreeRegressor

# defining the model as a tree regressor and specifying a number for random_state to have the same results each time we run the code
melbourne_model = DecisionTreeRegressor(random_state=1)

# fit the model
melbourne_model.fit(X, y)
print("Making predictions for the following 5 houses:")
print(X.head())

print("The predictions are")
print(melbourne_model.predict(X.head()))
#quality measuring metric 1) Mean Absolute Error (MAE)
#standard equation: error=actual−predicted
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)

mean_absolute_error(y, predicted_home_prices)

#the training illution, essentially testing and training on the same data make the model look accurate as it can simply cheat by memorizing, and when real data is introduced it can cause errors
#we fix this by splitting the data into training and validation data, and then we can use the validation data to test the model
from sklearn.model_selection import train_test_split

# split data into training and validation data, for features and target
# the split is based on a random number generator.
# the random_state argument makes sure the same split happens every time we

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

# define model
melbourne_model = DecisionTreeRegressor()
# fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
#overfitting is when the model is too complex and learns the noise in the training data instead of the actual patterns, which can lead to poor performance on new data. To avoid overfitting, we can use simpler models, regularization techniques, or gather more training data.

#underfitting is when the model is too simple and fails to capture the underlying patterns in the data, resulting in poor performance on both training and new data. To avoid underfitting, we can use more complex models, add more features, or reduce regularization.
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

# compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))