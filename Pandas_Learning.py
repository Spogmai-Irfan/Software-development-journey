import pandas as pd

df = pd.read_csv("students.csv")

print(df)
print(df.head())
print(df.shape)
high_marks = df[df["Marks"] > 80]

print(high_marks)
df.to_csv("students_cleaned.csv", index=False)