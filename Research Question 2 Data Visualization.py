import numpy as np
import pandas as pd
import geopandas as gpd
import math
import seaborn as sns
import matplotlib.pyplot as plt

def highest_rating_to_budget(df, gdf):
    df['budget_to_score'] = df['budget'] / df['score']
    b_min = df['budget_to_score'].min()
    b_max = df['budget_to_score'].max()
    merged = gdf.merge(df, left_on = "name", right_on = "country", how = "inner")
    fig, ax = plt.subplots(1)
    countries = merged.dissolve(by="name", aggfunc = "sum")
    countries.plot(column = "budget_to_score", legend = True, ax=ax, vmin=b_min, vmax=b_max)
    plt.title('Rating to Budget Ratio by Country')
    plt.show()

def main():
    df = pd.read_csv(r"C:\Users\koolk\Documents\UW Freshman Year\CSE 163 Python\movies\movies.csv", encoding='ISO-8859-1')
    df = df.drop(columns = 'released')
    gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    df.rename(columns = {'name' : 'Title'}, inplace = True)
    df['country'] = df['country'].str.replace('USA', 'United States of America')
    highest_rating_to_budget(df, gdf)

if __name__ == "__main__":
    main()
