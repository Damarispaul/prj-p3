import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Added for KDE plots

# Data Inspection Class
class DataInspector:
    def __init__(self, df):
        """
        Initialize with a DataFrame.
        """
        self.df = df
        pd.set_option('display.max_columns', None)  # Ensure all columns are shown

    def first_five_rows(self):
        """
        Print the first five rows.
        """
        print(self.df.head())

    def describe_data(self):
        """
        Print concise statistics summary of the DataFrame.
        """
        print("Concise Statistic Summary For Numerical Features:")
        print(self.df.describe().T)

    def check_dimensionality(self):
        """
        Print the shape (rows, columns) of the DataFrame.
        """
        print(f"We have {self.df.shape[0]} Rows and {self.df.shape[1]} Columns in our DataFrame.")

    def display_info(self):
        """
        Print information about the DataFrame, including data types of all columns.
        """
        print("\nDataFrame Information:")
        self.df.info()
        dtype_counts = self.df.dtypes.value_counts()
        print("\nData Types:")
        for dtype, count in dtype_counts.items():
            print(f"{count} columns of type {dtype}")


# Data Cleaning Class
class DataCleaner:
    def __init__(self, df):
        """
        Initialize with a DataFrame.
        """
        self.df = df

    def check_missing_values(self):
        """
        Check for missing values in the DataFrame.
        """
        print("\nMissing Values in Each Column:")
        print(self.df.isnull().sum())

    def check_duplicates(self):
        """
        Check for duplicate rows in the DataFrame.
        """
        duplicates = self.df.duplicated().sum()
        print("\nNumber of Duplicate Rows:", duplicates)


# Univariate Analysis Class
class UnivariateAnalysis:
    def __init__(self, numerical_df, cat_df):
        """
        Initialize the class with numerical and categorical dataframes.
        """
        self.numerical_df = numerical_df
        self.categorical_df = cat_df

    def plot_numerical_histograms(self):
        """
        Plot histograms for numerical variables with a simple layout.
        """
        num_columns = len(self.numerical_df.columns)
        cols = 5  # Fixed number of subplots per row
        rows = -(-num_columns // cols)  # Calculate rows using ceiling division

        # Create a figure with subplots
        fig, axes = plt.subplots(rows, cols, figsize=(20, rows * 4))  # Adjust size based on rows
        axes = axes.flatten()  # Flatten axes for easy looping

        for i, column in enumerate(self.numerical_df.columns):
            sns.histplot(self.numerical_df[column], kde=True, ax=axes[i])
            axes[i].set_title(f"{column}", fontsize=12)
            axes[i].set_xlabel("Value")
            axes[i].set_ylabel("Frequency")

        # Hide unused axes
        for ax in axes[num_columns:]:
            ax.set_visible(False)

        plt.tight_layout()
        plt.show()

    def plot_categorical_histograms(self):
        """
        Plot bar charts for categorical variables in a single figure with subplots.
        """
        num_columns = len(self.categorical_df.columns)
        cols = 3  # Number of columns for the grid layout
        rows = -(-num_columns // cols)  # Calculate rows using ceiling division

        # Create a figure with subplots arranged in a grid
        fig, axes = plt.subplots(rows, cols, figsize=(15, rows * 5), constrained_layout=True)

        # Flatten axes array for easy iteration
        axes = axes.flatten()

        # Loop through the categorical columns and plot on their respective axes
        for i, column in enumerate(self.categorical_df.columns):
            counts = self.categorical_df[column].value_counts()

            # Bar chart
            axes[i].bar(counts.index.astype(str), counts.values, alpha=0.7, color="skyblue")

            # Set titles and labels
            axes[i].set_title(f"Bar Chart for {column}", fontsize=12)
            axes[i].set_xlabel("Categories", fontsize=10)
            axes[i].set_ylabel("Frequency", fontsize=10)

            # Customize tick rotation for better visualization
            axes[i].tick_params(axis='x', rotation=45, labelsize=8)

            # Remove grid lines
            axes[i].grid(False)

        # Hide unused subplots
        for j in range(num_columns, len(axes)):
            axes[j].set_visible(False)

        # Display the plot
        plt.show()



class CategoricalBivariate:
    def __init__(self, cat_df, churn):
        """
        Initializes the CategoricalBivariate class with data and the target variable.
        
        Parameters:
        cat_df (DataFrame): The dataset containing the
        categorical variables and target variable.
        churn (str): The target variable column name (e.g., 'churn') for bivariate analysis.
        """
        self.data = cat_df
        self.target_variable = churn  # Assign the passed churn column name to self.target_variable

    def plot_area_code_churn(self):
        """
        Plots the bivariate relationship between 'area code' and the target variable.
        """
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.data, x='area code',
                      hue=self.target_variable, palette='Set2')
        plt.title("Relationship between Area Code and Churn", fontsize=16)
        plt.xlabel("Area Code")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.legend(title=self.target_variable, loc="best")
        plt.tight_layout()
        plt.show()

    def plot_voice_mail_plan_churn(self):
        """
        Plots the bivariate relationship between 'voice mail plan' and the target variable.
        """
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.data, x='voice mail plan', 
                      hue=self.target_variable, palette='Spectral')
        plt.title("Relationship between Voice Mail Plan and Churn", fontsize=16)
        plt.xlabel("Voice Mail Plan")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.legend(title=self.target_variable, loc="best")
        plt.tight_layout()
        plt.show()

    def plot_international_plan_churn(self):
        """
        Plots the bivariate relationship between 'international plan'
        and the target variable.
        """
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.data, x='international plan', 
                      hue=self.target_variable, palette='twilight')
        plt.title("Relationship between International Plan and Churn", fontsize=16)
        plt.xlabel("International Plan")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.legend(title=self.target_variable, loc="best")
        plt.tight_layout()
        plt.show()


