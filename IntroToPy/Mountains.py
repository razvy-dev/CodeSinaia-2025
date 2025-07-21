import math
import matplotlib.pyplot as plt
import pandas as pd

# read from db

try:
    df = pd.read_csv("IntroToPy/mountains_db.tsv", sep="\t", header=None, names=["Name", "Height", "Country", "ISO"])
except RuntimeError as e:
    print(f"Error reading the data from the database: {e}")

# how many countries

try:
    print(f"There are {len(df['Country'].value_counts())} unique countries")
except RuntimeError as e:
    print(f"Error counting countries: {e}")

# how many mountains without heigh
try:
    print(f"There are {len((df[df['Height'].isna()]))} mountains without height")

except RuntimeError as e:
    print(f"Error counting mountainscle without height: {e}")

try:
    with_heights = df[df['Height'].notnull()]
    print(len(with_heights))
    heights_list = pd.to_numeric(with_heights['Height']).tolist()
    min_value = min(heights_list)
    max_value = max(heights_list)
    median_value = pd.Series(heights_list).median()
    average_value = pd.Series(heights_list).mean()
    print(f"Min height: {min_value}, Max height: {max_value}, Median: {median_value}, Average: {average_value}")
    print(f"Standard deviation: {pd.Series(heights_list).std()}")
except RuntimeError as e:
    print(f"Error processing heights: {e}")

def get_topN(df, topN):
    try:
        sorted_df = df.sort_values(by='Height', ascending=False).head(topN)
        print(sorted_df[['Name', 'Height']])
    except RuntimeError as e:
        print(f"Error getting top {topN} mountains: {e}")

def get_max_height_for_name(df, name):
    heights = pd.to_numeric(df[df['Name'] == name]['Height'], errors='coerce')
    if heights.empty:
        return None
    return heights.max()

def create_bar_chart_1():
    try:
        pass
    except RuntimeError as e:
        print(f"Error creating bar chart: {e}")

def create_bar_chart_2(df):
    try:

        plt.bar(df['Name'], param)
        plt.xlabel('Mountain Names')
        plt.ylabel('Heights')
        plt.title('Mountain Heights')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()
    except RuntimeError as e:
        print(f"Error creating bar chart: {e}")