import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import LabelEncoder


excel_file = r"C:\Users\dell\OneDrive - Lebanese American University\Desktop\Spring2024\MCE2\Project\random_values.xlsx"
df = pd.read_excel(excel_file)
output_file = r"balanced_data.xlsx"
df_out =pd.DataFrame()
filt_counts = df['Nitrogen Classification'].value_counts()

df = pd.read_excel(excel_file)

# Identify the column containing the class labels
class_column = 'class_label'

print("Class distribution before oversampling:")
print(df['Nitrogen Classification'].value_counts())

filt_counts = df[class_column].value_counts()
# Separate features and labels
X = df.drop(columns=[class_column])
y = df['Nitrogen Classification']
sampling_strategy = {0:543,1:543,2:543,3:543,4:543,5:543,6:543,7:543,8:543,9:543,10:543}
# Apply RandomOverSampler to balance the dataset
ros = RandomOverSampler(sampling_strategy=sampling_strategy)
X_resampled, y_resampled = ros.fit_resample(X, y)

# Combine resampled features and labels into a DataFrame
balanced_df = pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.Series(y_resampled, name=class_column)], axis=1)

print("\nClass distribution after oversampling:")
print(balanced_df[class_column].value_counts())
df_out = pd.concat([df_out,balanced_df['class_label']], axis=1)
df_out = df_out.rename(columns = {'class_label':'Nitrogen'})

df_out = df_out.sample(frac=1).reset_index(drop=True)
df_out.to_excel(output_file, index=False)



col_to_plot = 'Nitrogen'
col_count = df_out[col_to_plot].value_counts()
plt.figure(figsize=(8, 6))
col_count.plot(kind='bar')
plt.title('Balance of Data in the "Nitro" Column')
plt.xlabel('Categories')
plt.ylabel('Counts')
plt.xticks(rotation=45)
plt.show()



print("Class distribution before oversampling:")
print(df['Phosphorus Classification'].value_counts())

filt_counts = df[class_column].value_counts()
# Separate features and labels
X = df.drop(columns=[class_column])
y = df['Phosphorus Classification']

# Apply RandomOverSampler to balance the dataset
ros = RandomOverSampler(sampling_strategy='auto')
X_resampled, y_resampled = ros.fit_resample(X, y)

# Combine resampled features and labels into a DataFrame
balanced_df = pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.Series(y_resampled, name=class_column)], axis=1)

print("\nClass distribution after oversampling:")
print(balanced_df[class_column].value_counts())

df_out = pd.concat([df_out,balanced_df['class_label']], axis=1)
df_out = df_out.rename(columns = {'class_label':'Phosphorus'})

df_out = df_out.sample(frac=1).reset_index(drop=True)
df_out.to_excel(output_file, index=False)