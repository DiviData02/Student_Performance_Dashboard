
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# ============================================================
# LOAD DATASET
# ============================================================

data = pd.read_csv("../dataset/StudentPerformanceFactors.csv")

print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nDataset Information:")
print(data.info())


# ============================================================
# CHECK DATA QUALITY
# ============================================================

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDuplicate Rows:")
print(data.duplicated().sum())


# ============================================================
# DATA CLEANING
# ============================================================

clean_data = data.copy()

categorical_columns = [
    "Teacher_Quality",
    "Parental_Education_Level",
    "Distance_from_Home"
]

for column in categorical_columns:
    clean_data[column] = clean_data[column].fillna(
        clean_data[column].mode()[0]
    )

print("\nMissing Values After Cleaning:")
print(clean_data.isnull().sum())


# ============================================================
# NUMERICAL DATA VALIDATION
# ============================================================

print("\nNumerical Data Summary:")
print(clean_data.describe())

print("\nMinimum Values:")
print(clean_data.select_dtypes(include="number").min())

print("\nMaximum Values:")
print(clean_data.select_dtypes(include="number").max())


# Check invalid exam scores

print("\nNumber of Scores Above 100:")
print((clean_data["Exam_Score"] > 100).sum())

print("\nRecord with Exam Score Above 100:")
print(clean_data.loc[clean_data["Exam_Score"] > 100].T)

print("\nExam Score Distribution:")
print(
    clean_data["Exam_Score"]
    .value_counts()
    .sort_index()
    .tail(10)
)


# Correct invalid exam score

clean_data.loc[
    clean_data["Exam_Score"] > 100,
    "Exam_Score"
] = 100

print("\nMaximum Exam Score After Cleaning:")
print(clean_data["Exam_Score"].max())


# ============================================================
# NUMERICAL EDA
# ============================================================

# ------------------------------------------------------------
# Hours Studied vs Exam Score
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=clean_data,
    x="Hours_Studied",
    y="Exam_Score"
)

plt.title("Hours Studied vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")

plt.show()


correlation = clean_data["Hours_Studied"].corr(
    clean_data["Exam_Score"]
)

print("\nCorrelation between Hours Studied and Exam Score:")
print(correlation)


# ------------------------------------------------------------
# Attendance vs Exam Score
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=clean_data,
    x="Attendance",
    y="Exam_Score"
)

plt.title("Attendance vs Exam Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Previous Scores vs Exam Score
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=clean_data,
    x="Previous_Scores",
    y="Exam_Score"
)

plt.title("Previous Scores vs Exam Score")
plt.xlabel("Previous Scores")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Sleep Hours vs Exam Score
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=clean_data,
    x="Sleep_Hours",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Sleep Hours")
plt.xlabel("Sleep Hours")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Physical Activity vs Exam Score
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=clean_data,
    x="Physical_Activity",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Physical Activity")
plt.xlabel("Physical Activity (hours)")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Tutoring Sessions vs Exam Score
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

sns.boxplot(
    data=clean_data,
    x="Tutoring_Sessions",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Tutoring Sessions")
plt.xlabel("Tutoring Sessions")
plt.ylabel("Exam Score")

plt.show()


# ============================================================
# CORRELATION ANALYSIS
# ============================================================

numeric_data = clean_data.select_dtypes(include="number")

print("\nCorrelation with Exam Score:")

correlation_with_exam = (
    numeric_data.corr()["Exam_Score"]
    .sort_values(ascending=False)
)

print(correlation_with_exam)


# ------------------------------------------------------------
# Correlation Heatmap
# ------------------------------------------------------------

plt.figure(figsize=(10, 7))

sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap of Numerical Variables")

plt.show()


# ============================================================
# EXAM SCORE DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

sns.histplot(
    clean_data["Exam_Score"],
    bins=20,
    kde=True
)

plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")

plt.show()


# ============================================================
# CATEGORICAL EDA
# ============================================================

# ------------------------------------------------------------
# Motivation Level
# ------------------------------------------------------------

motivation_scores = clean_data.groupby(
    "Motivation_Level"
)["Exam_Score"].mean()

print("\nAverage Exam Score by Motivation Level:")
print(motivation_scores)

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=clean_data,
    x="Motivation_Level",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Motivation Level")
plt.xlabel("Motivation Level")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Parental Involvement
# ------------------------------------------------------------

parental_scores = clean_data.groupby(
    "Parental_Involvement"
)["Exam_Score"].mean()

print("\nAverage Exam Score by Parental Involvement:")
print(parental_scores)

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=clean_data,
    x="Parental_Involvement",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Parental Involvement")
plt.xlabel("Parental Involvement")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Access to Resources
# ------------------------------------------------------------

resource_scores = clean_data.groupby(
    "Access_to_Resources"
)["Exam_Score"].mean()

print("\nAverage Exam Score by Access to Resources:")
print(resource_scores)

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=clean_data,
    x="Access_to_Resources",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Access to Resources")
plt.xlabel("Access to Resources")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Teacher Quality
# ------------------------------------------------------------

teacher_scores = clean_data.groupby(
    "Teacher_Quality"
)["Exam_Score"].mean()

print("\nAverage Exam Score by Teacher Quality:")
print(teacher_scores)

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=clean_data,
    x="Teacher_Quality",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Teacher Quality")
plt.xlabel("Teacher Quality")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Family Income
# ------------------------------------------------------------

income_scores = clean_data.groupby(
    "Family_Income"
)["Exam_Score"].mean()

print("\nAverage Exam Score by Family Income:")
print(income_scores)

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=clean_data,
    x="Family_Income",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Family Income")
plt.xlabel("Family Income")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Peer Influence
# ------------------------------------------------------------

peer_scores = clean_data.groupby(
    "Peer_Influence"
)["Exam_Score"].mean()

print("\nAverage Exam Score by Peer Influence:")
print(peer_scores)

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=clean_data,
    x="Peer_Influence",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Peer Influence")
plt.xlabel("Peer Influence")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# School Type
# ------------------------------------------------------------

school_scores = clean_data.groupby(
    "School_Type"
)["Exam_Score"].mean()

print("\nAverage Exam Score by School Type:")
print(school_scores)

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=clean_data,
    x="School_Type",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by School Type")
plt.xlabel("School Type")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Extracurricular Activities
# ------------------------------------------------------------

activity_scores = clean_data.groupby(
    "Extracurricular_Activities"
)["Exam_Score"].mean()

print("\nAverage Exam Score by Extracurricular Activities:")
print(activity_scores)

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=clean_data,
    x="Extracurricular_Activities",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Extracurricular Activities")
plt.xlabel("Extracurricular Activities")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Internet Access
# ------------------------------------------------------------

internet_scores = clean_data.groupby(
    "Internet_Access"
)["Exam_Score"].mean()

print("\nAverage Exam Score by Internet Access:")
print(internet_scores)

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=clean_data,
    x="Internet_Access",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Internet Access")
plt.xlabel("Internet Access")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Learning Disabilities
# ------------------------------------------------------------

disability_scores = clean_data.groupby(
    "Learning_Disabilities"
)["Exam_Score"].mean()

print("\nAverage Exam Score by Learning Disabilities:")
print(disability_scores)

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=clean_data,
    x="Learning_Disabilities",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Learning Disabilities")
plt.xlabel("Learning Disabilities")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Parental Education Level
# ------------------------------------------------------------

parent_education_scores = clean_data.groupby(
    "Parental_Education_Level"
)["Exam_Score"].mean()

print("\nAverage Exam Score by Parental Education Level:")
print(parent_education_scores)

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=clean_data,
    x="Parental_Education_Level",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Parental Education Level")
plt.xlabel("Parental Education Level")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Distance from Home
# ------------------------------------------------------------

distance_scores = clean_data.groupby(
    "Distance_from_Home"
)["Exam_Score"].mean()

print("\nAverage Exam Score by Distance from Home:")
print(distance_scores)

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=clean_data,
    x="Distance_from_Home",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Distance from Home")
plt.xlabel("Distance from Home")
plt.ylabel("Exam Score")

plt.show()


# ------------------------------------------------------------
# Gender
# ------------------------------------------------------------

gender_scores = clean_data.groupby(
    "Gender"
)["Exam_Score"].mean()

print("\nAverage Exam Score by Gender:")
print(gender_scores)

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=clean_data,
    x="Gender",
    y="Exam_Score"
)

plt.title("Exam Score Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Exam Score")

plt.show()


# ============================================================
# END OF EDA
# ============================================================

print("\nEDA Completed Successfully!")

# ============================================================
# STATISTICAL ANALYSIS
# ============================================================

print("\n================ STATISTICAL ANALYSIS ================")


# ------------------------------------------------------------
# Pearson Correlation Tests
# ------------------------------------------------------------

numerical_factors = [
    "Hours_Studied",
    "Attendance",
    "Previous_Scores",
    "Tutoring_Sessions",
    "Physical_Activity",
    "Sleep_Hours"
]

print("\nPearson Correlation Tests:")

for factor in numerical_factors:

    correlation, p_value = stats.pearsonr(
        clean_data[factor],
        clean_data["Exam_Score"]
    )

    print(f"\n{factor}")
    print("Correlation:", correlation)
    print("P-value:", p_value)

# ------------------------------------------------------------
# Independent T-Test
# ------------------------------------------------------------

internet_yes = clean_data[
    clean_data["Internet_Access"] == "Yes"
]["Exam_Score"]

internet_no = clean_data[
    clean_data["Internet_Access"] == "No"
]["Exam_Score"]

t_statistic, p_value = stats.ttest_ind(
    internet_yes,
    internet_no,
    equal_var=False
)

print("\nInternet Access T-Test:")
print("T-statistic:", t_statistic)
print("P-value:", p_value)

# ------------------------------------------------------------
# T-Tests for Binary Categorical Factors
# ------------------------------------------------------------

binary_factors = [
    "Gender",
    "Extracurricular_Activities",
    "Internet_Access",
    "Learning_Disabilities",
    "School_Type"
]

print("\nT-Tests for Binary Factors:")

for factor in binary_factors:

    groups = clean_data[factor].dropna().unique()

    group1 = clean_data[
        clean_data[factor] == groups[0]
    ]["Exam_Score"]

    group2 = clean_data[
        clean_data[factor] == groups[1]
    ]["Exam_Score"]

    t_statistic, p_value = stats.ttest_ind(
        group1,
        group2,
        equal_var=False
    )

    print(f"\n{factor}")
    print("Groups:", groups)
    print("T-statistic:", t_statistic)
    print("P-value:", p_value)

# ------------------------------------------------------------
# One-Way ANOVA
# ------------------------------------------------------------

anova_factors = [
    "Motivation_Level",
    "Parental_Involvement",
    "Access_to_Resources",
    "Teacher_Quality",
    "Family_Income",
    "Peer_Influence",
    "Parental_Education_Level",
    "Distance_from_Home"
]

print("\nOne-Way ANOVA Tests:")

for factor in anova_factors:

    groups = [
        group["Exam_Score"].values
        for _, group in clean_data.groupby(factor)
    ]

    f_statistic, p_value = stats.f_oneway(*groups)

    print(f"\n{factor}")
    print("F-statistic:", f_statistic)
    print("P-value:", p_value)

# ============================================================
# POST-HOC ANALYSIS — TUKEY'S HSD
# ============================================================

tukey_factors = [
    "Motivation_Level",
    "Parental_Involvement",
    "Access_to_Resources",
    "Teacher_Quality",
    "Family_Income",
    "Peer_Influence",
    "Parental_Education_Level",
    "Distance_from_Home"
]

print("\n================ TUKEY'S HSD TESTS ================")

for factor in tukey_factors:

    tukey_result = pairwise_tukeyhsd(
        endog=clean_data["Exam_Score"],
        groups=clean_data[factor],
        alpha=0.05
    )

    print(f"\n\nTukey HSD Results — {factor}")
    print(tukey_result)

# ============================================================
# EXPORT CLEANED DATASET
# ============================================================

clean_data.to_csv(
    "../dataset/StudentPerformanceFactors_Cleaned.csv",
    index=False
)

print("\nCleaned dataset exported successfully!")
