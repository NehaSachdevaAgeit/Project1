import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Set2")

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def clean_data(df):
    df_clean = df.copy()
    print("\n--- Missing Values Before Cleaning ---")
    print(df_clean.isnull().sum())
    numeric_cols = df_clean.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        if df_clean[col].isnull().sum() > 0:
            df_clean[col].fillna(df_clean[col].mean(), inplace=True)
    cat_cols = df_clean.select_dtypes(include=['object']).columns
    for col in cat_cols:
        if df_clean[col].isnull().sum() > 0:
            df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
    duplicates = df_clean.duplicated().sum()
    print(f"\nFound {duplicates} duplicate rows")
    if duplicates > 0:
        df_clean = df_clean.drop_duplicates()
        print(f"Removed {duplicates} duplicate rows")
    for col in cat_cols:
        df_clean[col] = df_clean[col].astype('category')
    print("\n--- Missing Values After Cleaning ---")
    print(df_clean.isnull().sum())
    return df_clean

def perform_eda(df):
    print("\n--- Summary Statistics ---")
    print(df.describe().T)
    print("\n--- Categorical Variable Counts ---")
    for col in df.select_dtypes(include=['category']).columns:
        print(f"\n{col} counts:")
        print(df[col].value_counts())
    score_cols = [col for col in df.columns if 'score' in col.lower() or
                  any(subj in col.lower() for subj in ['math', 'reading', 'writing'])]
    return score_cols

def create_visualizations(df, score_cols):
    import os
    if not os.path.exists('figures'):
        os.makedirs('figures')
    plt.figure(figsize=(15, 5))
    for i, col in enumerate(score_cols):
        plt.subplot(1, 3, i+1)
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col.capitalize()}')
        plt.xlabel('Score')
        plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('figures/score_distributions.png')
    plt.figure(figsize=(15, 5))
    for i, col in enumerate(score_cols):
        plt.subplot(1, 3, i+1)
        sns.boxplot(x='gender', y=col, data=df)
        plt.title(f'{col.capitalize()} by Gender')
        plt.xlabel('Gender')
        plt.ylabel('Score')
    plt.tight_layout()
    plt.savefig('figures/scores_by_gender.png')
    plt.figure(figsize=(15, 10))
    for i, col in enumerate(score_cols):
        plt.subplot(3, 1, i+1)
        if 'parental_education' in df.columns:
            edu_col = 'parental_education'
        elif 'parental.education' in df.columns:
            edu_col = 'parental.education'
        elif 'parent_education_level' in df.columns:
            edu_col = 'parent_education_level'
        else:
            possible_cols = [c for c in df.columns if 'parent' in c.lower() and 'edu' in c.lower()]
            edu_col = possible_cols[0] if possible_cols else None
        if edu_col:
            sns.barplot(x=edu_col, y=col, data=df, estimator=np.mean)
            plt.title(f'Average {col.capitalize()} by Parental Education')
            plt.xlabel('Parental Education Level')
            plt.ylabel('Average Score')
            plt.xticks(rotation=45)
        else:
            plt.text(0.5, 0.5, 'Parental Education column not found',
                     horizontalalignment='center', verticalalignment='center')
    plt.tight_layout()
    plt.savefig('figures/scores_by_parental_education.png')
    plt.figure(figsize=(15, 5))
    for i, col in enumerate(score_cols):
        plt.subplot(1, 3, i+1)
        if 'lunch' in df.columns:
            lunch_col = 'lunch'
        elif 'lunch_type' in df.columns:
            lunch_col = 'lunch_type'
        else:
            possible_cols = [c for c in df.columns if 'lunch' in c.lower()]
            lunch_col = possible_cols[0] if possible_cols else None
        if lunch_col:
            sns.boxplot(x=lunch_col, y=col, data=df)
            plt.title(f'{col.capitalize()} by Lunch Type')
            plt.xlabel('Lunch Type')
            plt.ylabel('Score')
        else:
            plt.text(0.5, 0.5, 'Lunch Type column not found',
                     horizontalalignment='center', verticalalignment='center')
    plt.tight_layout()
    plt.savefig('figures/scores_by_lunch_type.png')
    plt.figure(figsize=(15, 5))
    for i, col in enumerate(score_cols):
        plt.subplot(1, 3, i+1)
        if 'test_preparation_course' in df.columns:
            test_prep_col = 'test_preparation_course'
        elif 'test_prep' in df.columns:
            test_prep_col = 'test_prep'
        else:
            possible_cols = [c for c in df.columns if 'test' in c.lower() and 'prep' in c.lower()]
            test_prep_col = possible_cols[0] if possible_cols else None
        if test_prep_col:
            sns.boxplot(x=test_prep_col, y=col, data=df)
            plt.title(f'{col.capitalize()} by Test Prep Course')
            plt.xlabel('Test Preparation Course')
            plt.ylabel('Score')
        else:
            plt.text(0.5, 0.5, 'Test Preparation column not found',
                     horizontalalignment='center', verticalalignment='center')
    plt.tight_layout()
    plt.savefig('figures/scores_by_test_prep.png')
    plt.figure(figsize=(10, 8))
    correlation_matrix = df[score_cols].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Between Scores')
    plt.tight_layout()
    plt.savefig('figures/score_correlations.png')
    plt.figure(figsize=(12, 10))
    sns.pairplot(df[score_cols])
    plt.suptitle('Pairwise Relationships Between Scores', y=1.02)
    plt.tight_layout()
    plt.savefig('figures/score_pairplot.png')
    test_prep_col_found = next((col for col in df.columns if 'test' in col.lower() and 'prep' in col.lower()), None)
    if 'gender' in df.columns and test_prep_col_found:
        plt.figure(figsize=(18, 6))
        for i, col in enumerate(score_cols):
            plt.subplot(1, 3, i+1)
            sns.boxplot(x='gender', y=col, hue=test_prep_col_found, data=df)
            plt.title(f'{col.capitalize()} by Gender and Test Prep')
            plt.xlabel('Gender')
            plt.ylabel('Score')
        plt.tight_layout()
        plt.savefig('figures/scores_by_gender_and_test_prep.png')
    return correlation_matrix

def perform_analysis(df, score_cols):
    analysis_results = {}
    analysis_results['overall_averages'] = {col: df[col].mean() for col in score_cols}
    if 'gender' in df.columns:
        analysis_results['gender_averages'] = df.groupby('gender')[score_cols].mean().to_dict()
    edu_col = next((col for col in df.columns if 'parent' in col.lower() and 'edu' in col.lower()), None)
    if edu_col:
        analysis_results['education_averages'] = df.groupby(edu_col)[score_cols].mean().to_dict()
    lunch_col = next((col for col in df.columns if 'lunch' in col.lower()), None)
    if lunch_col:
        analysis_results['lunch_averages'] = df.groupby(lunch_col)[score_cols].mean().to_dict()
    test_prep_col = next((col for col in df.columns if 'test' in col.lower() and 'prep' in col.lower()), None)
    if test_prep_col:
        analysis_results['test_prep_averages'] = df.groupby(test_prep_col)[score_cols].mean().to_dict()
        from scipy import stats
        for col in score_cols:
            test_prep_values = df[test_prep_col].unique()
            if len(test_prep_values) == 2:
                group1 = df[df[test_prep_col] == test_prep_values[0]][col]
                group2 = df[df[test_prep_col] == test_prep_values[1]][col]
                t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)
                if 'statistical_tests' not in analysis_results:
                    analysis_results['statistical_tests'] = {}
                analysis_results['statistical_tests'][f'{col}_by_{test_prep_col}'] = {
                    't_statistic': t_stat,
                    'p_value': p_value,
                    'significant': p_value < 0.05
                }
    return analysis_results

def main(file_path):
    df = load_data(file_path)
    if df is None:
        return
    print("\nInitial Dataset Information")
    print(df.info())
    print("\nFirst 5 rows")
    print(df.head())
    df_clean = clean_data(df)
    score_cols = perform_eda(df_clean)
    correlation_matrix = create_visualizations(df_clean, score_cols)
    analysis_results = perform_analysis(df_clean, score_cols)
    print("\nAnalysis complete! Visualizations saved in the 'figures' directory")
    return df_clean, analysis_results

if __name__ == "__main__":
    file_path = r"C:\Users\Neha Sachdeva\OneDrive\Desktop\internship\intern1\StudentsPerformance.csv"
    main(file_path)

