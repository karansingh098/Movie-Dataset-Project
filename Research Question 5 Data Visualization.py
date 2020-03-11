import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def highest_and_lowest_rated_genres_over_the_years(df):
    genre_ratings_over_years = df.groupby(['year', 'genre'], as_index=False)['votes'].sum()
    print(genre_ratings_over_years)
    sns.relplot(x='year', y='votes', hue='genre', kind='line', data=genre_ratings_over_years)
    plt.title("Highest and Lowest Viewer Votes per Genres over the Years")
    plt.xlabel("Years")
    plt.ylabel("Viewer Votes by Genre")
    plt.show()


def main():
    df = pd.read_csv(r"C:\Users\koolk\Documents\UW Freshman Year\CSE 163 Python\movies\movies.csv", encoding='ISO-8859-1')
    highest_and_lowest_rated_genres_over_the_years(df)


if __name__ == "__main__":
    main()
