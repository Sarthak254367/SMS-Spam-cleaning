import pandas as pd
import urllib.request
import zipfile

# Step 1: Download Dataset
url = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"

urllib.request.urlretrieve(url, "sms.zip")

# Step 2: Extract Dataset
with zipfile.ZipFile("sms.zip", "r") as z:
    z.extract("SMSSpamCollection")

# Step 3: Load Dataset
df = pd.read_csv(
    "SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Step 4: Explore Dataset
print("First 5 Rows:")
print(df.head())

print("Dataset Shape:")
print(df.shape)

print("Columns:")
print(df.columns)

# Step 5: Check Missing Values
print("Missing Values:")
print(df.isnull().sum())

# Step 6: Remove Missing Values
df = df.dropna()

# Step 7: Remove Duplicate Records
print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# Step 8: Count Ham and Spam
print("Ham and Spam Count:")
print(df["label"].value_counts())

# Step 9: Select Required Columns
cleaned_df = df[["label", "message"]]

# Step 10: Save Cleaned Dataset
cleaned_df.to_csv("cleaned_sms.csv", index=False)

print("Cleaning Completed Successfully!")
print("Final Shape:", cleaned_df.shape)
