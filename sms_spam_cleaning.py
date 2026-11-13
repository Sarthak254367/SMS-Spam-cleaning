

import pandas as pd
import urllib.request
import zipfile

# Step 1: Download dataset
url = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
urllib.request.urlretrieve(url, "sms.zip")

# Step 2: Extract dataset
with zipfile.ZipFile("sms.zip", "r") as z:
    z.extract("SMSSpamCollection")

# Step 3: Load dataset
df = pd.read_csv(
    "SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Step 4: Explore dataset
print("First 5 Rows:")
print(df.head())

print("Dataset Shape:")
print(df.shape)

print("Columns:")
print(df.columns)

# Step 5: Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Step 6: Remove missing values
df = df.dropna()

# Step 7: Remove duplicates
print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# Step 8: Count Ham and Spam
print("Ham and Spam Count:")
print(df["label"].value_counts())

# Step 9: Select required columns
cleaned_df = df[["label", "message"]]

# Step 10: Save cleaned dataset
cleaned_df.to_csv("cleaned_sms.csv", index=False)

print("Cleaning Completed Successfully!")
print("Final Shape:", cleaned_df.shape)


  

