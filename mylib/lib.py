"""
    library file
"""
import polars as pl
import matplotlib.pyplot as plt

dataset_url = "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/drug-use-by-age/drug-use-by-age.csv"

def load_dataset():
    return pl.read_csv(dataset_url)

def describe_dataset():
    dataset = load_dataset()
    return dataset.describe()

def describe_median():
    dataset = load_dataset().select(pl.all().exclude("age"))

    dataset = dataset.with_columns([
        pl.col(pl.Utf8).str.replace("-", "0").cast(pl.Float64)
    ])

    median_values = dataset.median()

    return median_values

def create_histogram(save_path):
    dataset = load_dataset()
    plt.figure(figsize=(8, 6))
    
    # Plotting the histogram
    plt.hist(dataset['alcohol_use'], bins=10, edgecolor='black')
    plt.xlabel('Alcohol Use (%)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Alcohol Use')
    
    # Save the plot as a PNG file
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()  # Close the figure after saving

def create_line_chart(save_path):
    dataset = load_dataset()
    data_selected = dataset[['age', 'marijuana_use']]

    plt.figure(figsize=(10, 6))
    plt.plot(data_selected['age'], 
             data_selected['marijuana_use'], 
             label='Marijuana Use (%)', marker='o', color='g')

    plt.xlabel('Age')
    plt.ylabel('Marijuana Use (%)')
    plt.title('Trend of Marijuana Use by Age')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    
    # Save the line chart
    plt.savefig(save_path)
    plt.close()

def create_bar_chart(save_path):
    dataset = load_dataset()
    data_selected = dataset[['age', 'cocaine_use']]

    plt.figure(figsize=(10, 6))
    plt.bar(data_selected['age'], data_selected['cocaine_use'], color='orange')

    plt.xlabel('Age')
    plt.ylabel('Cocaine Use (%)')
    plt.title('Cocaine Use by Age')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the bar chart
    plt.savefig(save_path)
    plt.close()

print(describe_median())