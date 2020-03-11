import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def highest_grossing_movies(df, gdf, ax):
    g_min = df['gross'].min()
    g_max = df['gross'].max()
    merged = gdf.merge(df, left_on="name", right_on="country", how="inner")
    countries = merged.dissolve(by="name", aggfunc="sum")
    ax.set_title('Movie Revenue by Country')
    countries.plot(column="gross", legend=True, ax=ax, vmin=g_min, vmax=g_max)


def country_gdp(df, gdf, ax):
    merged = gdf.merge(df, left_on="name", right_on="Country", how="inner")
    # taking gdp of countries from 2017
    merged['2017'] = merged['2017'].astype(float)
    gdp_min = merged['2017'].min()
    gdp_max = merged['2017'].max()
    ax.set_title('GDP by Country')
    merged.plot(column="2017", legend=True, ax=ax, vmin=gdp_min, vmax=gdp_max)


def main():
    df = pd.read_csv(r"C:\Users\koolk\Documents\UW Freshman Year\CSE 163 Python\movies\movies.csv", encoding='ISO-8859-1')
    df = df.drop(columns='released')
    gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    df.rename(columns={'name': 'Title'}, inplace=True)
    df['country'] = df['country'].str.replace('USA', 'United States of America')
    fig, [ax1, ax2] = plt.subplots(1, 2)
    highest_grossing_movies(df, gdf, ax1)
    gdp_data = pd.read_csv(r"C:\Users\koolk\Documents\UW Freshman Year\CSE 163 Python\CSE Final Project\WorldNominalGDPAnnuel.csv", encoding='ISO-8859-2')
    gdp_data['Country'] = gdp_data['Country'].str.replace('United States', 'United States of America')
    country_gdp(gdp_data, gdf, ax2)


if __name__ == "__main__":
    main()
