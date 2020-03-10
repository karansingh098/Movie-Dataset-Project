import numpy as np
import pandas as pd
import geopandas as gpd
import math
import seaborn as sns
import matplotlib.pyplot as plt

def highest_grossing_movies(df, gdf):
    df = df.drop(columns = 'released')
    df['budget_to_score'] = df['budget'] / df['score']
    g_min = df['gross'].min()
    g_max = df['gross'].max()
    b_min = df['budget_to_score'].min()
    b_max = df['budget_to_score'].max()
    merged = gdf.merge(df, left_on = "name", right_on = "country", how = "inner")
    fig, [ax,ax2] = plt.subplots(1, 2)
    countries = merged.dissolve(by="name", aggfunc = "sum")
    countries.plot(column = "gross", legend = True, ax=ax, vmin=g_min, vmax=g_max)
    countries.plot(column = "budget_to_score", legend = True, ax=ax2, vmin=b_min, vmax=b_max)
    plt.show()

def main():
    df = pd.read_csv(r"C:\Users\dswhi\OneDrive\Documents\UW Class Work\CSE 163\Final Project\Movies Dataset\movies.csv", encoding = 'ISO-8859-1')
    gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    df.rename(columns = {'name' : 'Title'}, inplace = True)
    df['country'] = df['country'].str.replace('USA', 'United States of America')
    highest_grossing_movies(df, gdf)

if __name__ == "__main__":
    main()