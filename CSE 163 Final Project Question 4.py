import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error


def select_features(df):
    revenue = df['gross']
    cor = df.corr()
    cor_target = abs(cor['score'])
    relevant_features = cor_target[cor_target > .1]
    df = df.filter(list(relevant_features.index))
    corr_matrix = df.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
    to_drop = [column for column in upper.columns if any(upper[column] > 0.75)]
    df = df.drop(df[to_drop], axis=1)
    df['gross'] = revenue
    return df


def fit_revenue1(df):
    df = df.dropna()
    X = df.drop(columns=['gross'])
    print(X)
    y = df['score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    return mean_squared_error(y_test, y_test_pred)


def fit_revenue2(df):
    df = df.dropna()
    X = df.loc[:, df.columns != 'gross']
    X = pd.get_dummies(X)
    y = df['gross']
    print(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    return mean_squared_error(y_test, y_test_pred)


# takes in dataframe of movies that user wants to predict gross revenue
# of as parameter
# returns the predcited revenue
# def predict_revenue(df):


def main():
    df = pd.read_csv(r"C:\Users\koolk\Documents\UW Freshman Year\CSE 163 Python\movies\movies.csv", encoding='ISO-8859-1')
    data_select = select_features(df)
    print(fit_revenue1(data_select))
    # filter out too specific features
    df = df.drop(columns=['director', 'name', 'released', 'star', 'writer'])
    # filter out lowball data
    df = df[(df['budget'] < 10000)]
    print(fit_revenue2(df))


if __name__ == "__main__":
    main()
