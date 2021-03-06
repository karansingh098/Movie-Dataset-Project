import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error


def select_features(df):
    revenue = df['gross']
    cor = df.corr()
    cor_target = abs(cor['gross'])
    relevant_features = cor_target[cor_target > 0.1]
    df = df.filter(list(relevant_features.index))
    corr_matrix = df.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
    to_drop = [column for column in upper.columns if any(upper[column] > 0.75)]
    df = df.drop(df[to_drop], axis=1)
    df['gross'] = revenue
    return df


def fit_revenue(df):
    df = pd.get_dummies(df)
    df = df.dropna()
    df = df[df['budget'] > 0]
    X = df.drop(columns=['gross'])
    y = df['gross']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    print(X_train)
    # test cases
    # defining some predictions
    Xnew = [[50000000, 96, 8, 50000, 2004], [6000000, 120, 6, 100000, 2014]]
    # make a prediction
    ynew = model.predict(Xnew)
    # show the inputs and predicted outputs
    for i in range(len(Xnew)):
        print("X=%s, Predicted=%s" % (Xnew[i], ynew[i]))
    return mean_squared_error(y_test, y_test_pred)


def main():
    df = pd.read_csv("movies.csv", encoding='ISO-8859-1')
    df = select_features(df)
    print(fit_revenue(df))


if __name__ == "__main__":
    main()
