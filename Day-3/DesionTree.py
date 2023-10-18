X = [[6], [8], [10], [20], [18]]  
y = [7, 9, 19, 17.5, 18]  
split_ratio = 0.8
split_index = int(len(X) * split_ratio)
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]
class DecisionTreeRegressor:
    def __init__(self):
        pass
    def fit(self, X, y):
        self.X = X
        self.y = y
    def predict(self, X_test):
        predictions = []
        for test_point in X_test:
            predictions.append(self._predict_single(test_point))
        return predictions
    def _predict_single(self, test_point):
        return sum(self.y) / len(self.y)
regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)
predictions = regressor.predict(X_test)
error_sum = 0
for i in range(len(y_test)):
    error_sum += (y_test[i] - predictions[i]) ** 2
mse = error_sum / len(y_test)
print("Mean Squared Error:", mse)
