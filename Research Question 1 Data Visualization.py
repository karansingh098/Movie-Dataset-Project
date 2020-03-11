import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def highest_grossing_movies(df, gdf):
    g_min = df['gross'].min()
    g_max = df['gross'].max()
    fig, ax = plt.subplots(1)
    merged = gdf.merge(df, left_on="name", right_on="country", how="inner")
    countries = merged.dissolve(by="name", aggfunc="sum")
    countries.plot(column="gross", legend=True, ax=ax, vmin=g_min, vmax=g_max)
    plt.title('Movie Revenue by Country')
    plt.show()


def country_gdp(df, gdf):
    merged = gdf.merge(df, left_on="name", right_on="Country Name", how="inner")
    # taking gdp of countries from 2017
    gdp_min = merged['Value'].min()
    gdp_max = merged['Value'].max()
    fig, ax = plt.subplots(1)
    merged.plot(column="Value", legend=True, ax=ax, vmin=gdp_min, vmax=gdp_max)
    plt.title('GDP by Country')
    plt.show()


def main():
    df = pd.read_csv(r"C:\Users\dswhi\OneDrive\Documents\UW Class Work\CSE 163\Final Project\Movies Dataset\movies.csv", encoding = 'ISO-8859-1')
    df = df.drop(columns = 'released')
    gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    df.rename(columns = {'name' : 'Title'}, inplace = True)
    df['country'] = df['country'].str.replace('USA', 'United States of America')
    highest_grossing_movies(df, gdf)
    gdp_df = pd.read_csv(r"C:\Users\dswhi\OneDrive\Documents\UW Class Work\CSE 163\Final Project\world-national-and-real-gdp-annualyquaterly\gdp_csv.csv")
    gdp_df = gdp_df.fillna(0)
    gdp_df['Country Name'] = gdp_df['Country Name'].str.replace('United States', 'United States of America')
    gdp_df['Country Name'] = gdp_df['Country Name'].str.replace('Russian Federation', 'Russia')
    gdp_df['Country Name'] = gdp_df['Country Name'].str.replace('Congo, Dem. Rep.', 'Dem. Rep. Congo')
    gdp_df = gdp_df.groupby("Country Name").mean()
    country_gdp(gdp_df, gdf)


if __name__ == "__main__":
    main()
