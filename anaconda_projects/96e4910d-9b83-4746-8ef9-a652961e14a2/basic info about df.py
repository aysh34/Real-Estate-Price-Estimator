# Basic information about our dataset

print("===== BASIC DATASET INFORMATION =====\n")

print(f"Dataset shape: {df1.shape}")

print(f"\n===== Column names =====\n{df1.columns.tolist()}")

print(f"\n====== Data types =====\n{df1.dtypes} ")

print(f"\n===== Missing values =====\n{df1.isnull().sum()}")

print(f"\n===== Missing percentage =====\n{(df1.isnull().sum()/len(df1))*100}")

print(f"\n===== Duplicate rows =====\n{df1.duplicated().sum()}")

print(f"\n===== Data Description =====\n{df1.describe()}")