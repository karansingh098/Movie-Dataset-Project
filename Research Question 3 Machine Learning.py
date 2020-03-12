import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error


def select_features(df):
    genre = df['genre']
    cor = df.corr()
    cor_target = abs(cor['score'])
    relevant_features = cor_target[cor_target > .1]
    df = df.filter(list(relevant_features.index))
    corr_matrix = df.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1)
                                .astype(np.bool))
    to_drop = [column for column in upper.columns if any(upper[column] > 0.75)]
    df = df.drop(df[to_drop], axis=1)
    df['genre'] = genre
    return df


def fit_and_predict_ratings(df, genre):
    df = df[df['genre'] == genre]
    X = df.drop(['genre', 'score'], axis=1)
    y = df['score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    print(X)
    # test cases
    # defining some predictions
    Xnew = [[50000000, 100, 500000, 2000], [6000000, 200, 50000, 2010]]
    # make a prediction
    ynew = model.predict(Xnew)
    # show the inputs and predicted outputs
    for i in range(len(Xnew)):
        print("X=%s, Predicted=%s" % (Xnew[i], ynew[i]))
    return mean_squared_error(y_test, y_test_pred)


def user_rating_to_genre(df):
    df = df.groupby('genre', as_index=False).sum()
    plot = sns.catplot(x='genre', y='votes', data=df, kind='bar')
    plt.title("Viewer Votes per Genre")
    plt.xlabel("Genre")
    plt.ylabel("Viewer Votes")
    plot.set_xticklabels(rotation=45)
    plt.show()


def main():
    df = pd.read_csv("movies.csv", encoding='ISO-8859-1')
    df = df.drop(columns='released')
    df = select_features(df)
    print(fit_and_predict_ratings(df, 'Action'))
    user_rating_to_genre(df)


if __name__ == "__main__":
    main()
