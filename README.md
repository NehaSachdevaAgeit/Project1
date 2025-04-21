# Project1
# Student Performance Analysis

## Project Description

This project provides a Python script for analyzing a student performance dataset. The script performs essential data cleaning, exploratory data analysis (EDA), generates visualizations to understand key relationships, and conducts a detailed analysis to identify potential factors influencing student scores.

## Dataset

The analysis is performed on the `StudentsPerformance.csv` dataset. This dataset contains information about students, including demographic details and their scores in various subjects.

## Features

* **Data Loading:** Loads the dataset from a CSV file.
* **Data Cleaning:** Handles missing values (imputing with mean for numerical, mode for categorical) and removes duplicate rows.
* **Exploratory Data Analysis (EDA):** Provides summary statistics and counts of categorical variables.
* **Data Visualization:** Generates various plots (histograms, box plots, bar plots, heatmaps, pair plots) to visualize score distributions and relationships with other factors. Visualizations are saved as PNG files.
* **Detailed Analysis:** Calculates average scores by different groups and performs statistical tests (e.g., t-test for test preparation impact).

## Setup

1.  **Prerequisites:**
    * Python 3.x
    * Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn (specifically `sklearn.preprocessing.LabelEncoder`, though not directly used in the final analysis logic shown in the output, it's imported).

2.  **Installation:**
    Install the required libraries using pip:

    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```

3.  **Dataset:**
    Place the `StudentsPerformance.csv` file in a known location and update the `file_path` variable in the `if __name__ == "__main__":` block of the script to point to this location.

4.  **Running the Script:**
    Execute the Python script from your terminal:

    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file).

## Script Overview

The script is structured into several functions:

* `load_data(file_path)`: Loads the dataset and prints initial information.
* `clean_data(df)`: Cleans the DataFrame by handling missing values and duplicates, and converts categorical columns.
* `perform_eda(df)`: Calculates and prints summary statistics and value counts for categorical columns. It also identifies score columns.
* `create_visualizations(df, score_cols)`: Generates and saves various plots exploring score distributions and their relationship with demographic and background features.
* `perform_analysis(df, score_cols)`: Conducts deeper analysis, including calculating group-wise averages and performing statistical tests.
* `main(file_path)`: Orchestrates the entire process by calling the above functions sequentially.

## Analysis Output & Insights

Based on the provided script output:

* **Dataset Size:** The dataset contains 1000 rows and 8 columns.
* **Missing Values:** Initially, there were a few missing values in the 'math score' (5), 'reading score' (6), and 'writing score' (5) columns. These were successfully handled during the cleaning process by filling them with the respective column means. No duplicate rows were found.
* **Summary Statistics:**
    * Math scores range from 0 to 100, with a mean of approximately 66.1.
    * Reading scores range from 17 to 100, with a mean of approximately 69.2.
    * Writing scores range from 10 to 100, with a mean of approximately 68.0.
    * Reading scores have a slightly higher average than math and writing scores in this dataset.
* **Categorical Variable Counts:**
    * **Gender:** Female (518), Male (482).
    * **Race/Ethnicity:** Group C (319), Group D (262), Group B (190), Group E (140), Group A (89).
    * **Lunch:** Standard (645), Free/Reduced (355).
    * **Test Preparation Course:** None (642), Completed (358).
* **Visualizations:** The script generates plots (saved in the `figures` directory) to visualize distributions, score comparisons by gender, parental education, lunch type, and test preparation, as well as score correlations and pairwise relationships.
* **Detailed Analysis:** The analysis calculates average scores for each group (gender, race/ethnicity, parental education, lunch, test preparation) and performs t-tests to evaluate the statistical significance of the difference in scores between groups who completed the test preparation course and those who did not. (Specific results of these analyses would be printed to the console or captured in the `analysis_results` dictionary returned by the `perform_analysis` function when the script is run).

## Output
Data columns (total 8 columns):
 #   Column                       Non-Null Count  Dtype
---  ------                       --------------  -----
 0   gender                       1000 non-null   object
 1   race/ethnicity               1000 non-null   object
 2   parental level of education  1000 non-null   object
 3   lunch                        1000 non-null   object
 4   test preparation course      1000 non-null   object
 5   math score                   995 non-null    float64
 6   reading score                994 non-null    float64
 7   writing score                995 non-null    float64

First 5 rows
   gender race/ethnicity parental level of education         lunch test preparation course  math score  reading score  writing score
0  female        group B           bachelor's degree      standard                    none        72.0           72.0           74.0 
1  female        group C                some college      standard               completed        69.0           90.0           88.0 
2  female        group B             master's degree      standard                    none        90.0           95.0           93.0 
3    male        group A          associate's degree  free/reduced                    none        47.0           57.0           44.0 
4    male        group C                some college      standard                    none        76.0           78.0           75.0 

--- Missing Values Before Cleaning ---
gender                         0
race/ethnicity                 0
parental level of education    0
lunch                          0
test preparation course        0
math score                     5
reading score                  6
writing score                  5
dtype: int64

Found 0 duplicate rows

--- Missing Values After Cleaning ---
gender                         0
race/ethnicity                 0
parental level of education    0
lunch                          0
test preparation course        0
math score                     0
reading score                  0
writing score                  0
dtype: int64

--- Summary Statistics ---
                count       mean        std   min   25%   50%   75%    max
math score     1000.0  66.091457  15.115395   0.0  57.0  66.0  77.0  100.0
reading score  1000.0  69.194165  14.560753  17.0  59.0  70.0  79.0  100.0
writing score  1000.0  68.036181  15.142985  10.0  58.0  69.0  79.0  100.0

--- Categorical Variable Counts ---

gender counts:
gender
female    518
male      482
Name: count, dtype: int64

race/ethnicity counts:
race/ethnicity
group C    319
group D    262
group B    190
group E    140
group A     89
Name: count, dtype: int64

parental level of education counts:
parental level of education
some college          226
associate's degree    222
high school           196
some high school      179
bachelor's degree     118
master's degree        59
Name: count, dtype: int64

lunch counts:
lunch
standard        645
free/reduced    355
Name: count, dtype: int64

test preparation course counts:
test preparation course
none         642
completed    358

![score_correlations](https://github.com/user-attachments/assets/cce85cb6-01eb-40be-ae34-3de1c62567f3)
All scores (Math, Reading, Writing) are strongly positively correlated with each other.
The strongest correlation is between Reading and Writing scores (0.95).
Math score has a strong positive correlation with both Reading (0.81) and Writing (0.80) scores.

![score_distributions](https://github.com/user-attachments/assets/2be2def1-250b-4976-a68e-17b8cf37da36)
Math Scores: The distribution is slightly skewed towards lower scores, with a peak around the 60s
Reading Scores: This distribution is more symmetric and peaks around the low to mid-70s, suggesting generally higher performance compared to Math.
Writing Scores: Similar to Reading, the Writing score distribution is also symmetric and peaks around the low to mid-70s, showing comparable performance levels to Reading.
Subject Comparison: On average, students in this dataset tend to perform better in Reading and Writing than in Math.
Score Spread: All three subjects show a wide range of scores, indicating significant variation in individual student performance.

![score_pairplot](https://github.com/user-attachments/assets/4c692bba-3e01-4eca-a46c-c482d6123647)
Scores are highly connected: There's a strong positive relationship between all pairs of scores (Math, Reading, Writing).
Good in one, good in others: Students scoring well in one subject generally score well in the others.
Reading and Writing are closest: The strongest relationship is observed between Reading and Writing scores.

![scores_by_gender](https://github.com/user-attachments/assets/398935da-336c-431f-beba-bc6e1df2fac6)
Math Scores: Male students tend to have slightly higher median math scores than female students.
Reading Scores: Female students tend to have noticeably higher median reading scores than male students.
Writing Scores: Female students tend to have noticeably higher median writing scores than male students.
Gender Differences: Females appear to perform better in reading and writing, while males show a slight edge in math in this dataset.

![scores_by_gender_and_test_prep](https://github.com/user-attachments/assets/b9637c7e-de50-4729-9439-ee2b0c0003d7)
Completing the test preparation course is generally associated with improved student scores across all subjects for both males and females.
Gender-based performance differences are evident: females tend to score higher in reading and writing, while males show a slight advantage in math.
While test preparation benefits both genders, it doesn't eliminate the observed gender-based performance patterns in different subjects.

![scores_by_lunch_type](https://github.com/user-attachments/assets/0b4c59d6-1398-478e-b84d-5a35b85b08a4)
Students with standard lunch consistently have higher median scores.
This difference is observed across Math, Reading, and Writing.
Standard lunch is associated with better performance in all subjects.

![scores_by_parental_education](https://github.com/user-attachments/assets/c3a910a1-dc6c-4193-a0ff-0d1a8fe8e05c)
Higher parental education levels are generally associated with higher average student scores.
This positive trend is visible across Math, Reading, and Writing scores.
Students whose parents have a master's or bachelor's degree tend to have the highest average scores.
Students whose parents have high school or some high school education tend to have lower average scores.

![scores_by_test_prep](https://github.com/user-attachments/assets/0eb26eb6-1d8a-45c6-a4bc-0f60fb10e31c)
Completing the test preparation course is strongly associated with higher median scores.
This score boost is observed across Math, Reading, and Writing.
Students who completed the course generally perform better.





