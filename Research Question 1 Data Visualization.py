import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def highest_grossing_movies(df, gdf):
    g_min = df['gross'].min()
    g_max = df['gross'].max()
    merged = gdf.merge(df, left_on="name", right_on="country", how="inner")
    fig, ax = plt.subplots(1)
    countries = merged.dissolve(by="name", aggfunc="sum")
    countries.plot(column="gross", legend=True, ax=ax, vmin=g_min, vmax=g_max)
    plt.show()


def main():
    df = pd.read_csv(r"C:\Users\dswhi\OneDrive\Documents\UW Class Work\CSE 163\Final Project\Movies Dataset\movies.csv", encoding='ISO-8859-1')
    df = df.drop(columns='released')
    gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    df.rename(columns={'name': 'Title'}, inplace=True)
    df['country'] = df['country'].str.replace('USA',
                                              'United States of America')
    highest_grossing_movies(df, gdf)


if __name__ == "__main__":
    main()
