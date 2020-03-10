import numpy as np
import pandas as pd
import geopandas as gpd
import math
import seaborn as sns
import matplotlib.pyplot as plt

def highest_and_lowest_rated_genres_over_the_years(df):
    max = df.groupby("year", as_index = False)['votes'].max()
    min = df.groupby("year", as_index = False)['votes'].min()
    sns.lineplot(x='year', y='votes', data=max, color = 'blue')
    sns.lineplot(x='year', y='votes', data=min, color = 'red')
    plt.title("Highest and Lowest Viewer Votes per Genres over the Years")
    plt.xlabel("Years")
    plt.ylabel("Viewer Votes")
    plt.show()

def main():
    df = pd.read_csv(r"C:\Users\dswhi\OneDrive\Documents\UW Class Work\CSE 163\Final Project\Movies Dataset\movies.csv", encoding = 'ISO-8859-1')
    highest_and_lowest_rated_genres_over_the_years(df)

if __name__ == "__main__":
    main()