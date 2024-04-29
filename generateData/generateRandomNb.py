import random
import pandas as pd

def generate_balanced_N_values(total_values, NPK_min, NPK_max, noise_percent):
    balanced_values = []
    mid_temp = (NPK_max - NPK_min) // 2
    upper_count = total_values // 2
    lower_count = total_values - upper_count
    
    while len(balanced_values) < total_values:
        if random.randint(0, 1):
            if upper_count > 0:
                balanced_values.append(random.randint(mid_temp, NPK_max))
                upper_count -= 1
        else:
            if lower_count > 0:
                balanced_values.append(random.randint(NPK_min, mid_temp))
                lower_count -= 1

    # Add noise
    num_noise = int(total_values * noise_percent) // 2  # 10% of total values
    for _ in range(num_noise):
        if random.randint(0, 1):
            balanced_values.append(random.randint(mid_temp, NPK_max))
        else:
            balanced_values.append(random.randint(NPK_min, mid_temp))

    return balanced_values

def generate_balanced_K_values(total_values, NPK_min, NPK_max, noise_percent):
    balanced_values = []
    mid_temp = (NPK_max - NPK_min) // 2
    upper_count = total_values // 2
    lower_count = total_values - upper_count
    
    while len(balanced_values) < total_values:
        if random.randint(0, 1):
            if upper_count > 0:
                balanced_values.append(random.randint(mid_temp, NPK_max))
                upper_count -= 1
        else:
            if lower_count > 0:
                balanced_values.append(random.randint(NPK_min, mid_temp))
                lower_count -= 1

    # Add noise
    num_noise = int(total_values * noise_percent) // 2  # 10% of total values
    for _ in range(num_noise):
        if random.randint(0, 1):
            balanced_values.append(random.randint(mid_temp, NPK_max))
        else:
            balanced_values.append(random.randint(NPK_min, mid_temp))

    return balanced_values

def generate_balanced_P_values(total_values, NPK_min, NPK_max, noise_percent):
    balanced_values = []
    mid_temp = (NPK_max - NPK_min) // 2
    upper_count = total_values // 2
    lower_count = total_values - upper_count
    
    while len(balanced_values) < total_values:
        if random.randint(0, 1):
            if upper_count > 0:
                balanced_values.append(random.randint(mid_temp, NPK_max))
                upper_count -= 1
        else:
            if lower_count > 0:
                balanced_values.append(random.randint(NPK_min, mid_temp))
                lower_count -= 1

    # Add noise
    num_noise = int(total_values * noise_percent) // 2  # 10% of total values
    for _ in range(num_noise):
        if random.randint(0, 1):
            balanced_values.append(random.randint(mid_temp, NPK_max))
        else:
            balanced_values.append(random.randint(NPK_min, mid_temp))

    return balanced_values

def generate_balanced_temp_values(total_values, NPK_min, NPK_max, noise_percent):
    balanced_values = []
    mid_temp = (NPK_max - NPK_min) // 2
    upper_count = total_values // 2
    lower_count = total_values - upper_count
    
    while len(balanced_values) < total_values:
        if random.randint(0, 1):
            if upper_count > 0:
                balanced_values.append(random.randint(mid_temp, NPK_max))
                upper_count -= 1
        else:
            if lower_count > 0:
                balanced_values.append(random.randint(NPK_min, mid_temp))
                lower_count -= 1

    # Add noise
    num_noise = int(total_values * noise_percent) // 2  # 10% of total values
    for _ in range(num_noise):
        if random.randint(0, 1):
            balanced_values.append(random.randint(mid_temp, NPK_max))
        else:
            balanced_values.append(random.randint(NPK_min, mid_temp))

    return balanced_values


total_values = 1500
temp_min = -10
temp_max = 50
noise_percent = 0.1
NPK_min = 0
NPK_max = 150

# Generate balanced temperature values for three columns
Nitrogen = generate_balanced_N_values(total_values, NPK_min, NPK_max, noise_percent)
Potassium = generate_balanced_P_values(total_values, NPK_min, NPK_max, noise_percent)
Phosphorus = generate_balanced_K_values(total_values, NPK_min, NPK_max, noise_percent)
Temperature = generate_balanced_temp_values(total_values,temp_min,temp_max,noise_percent)

# Create a DataFrame with four columns
df = pd.DataFrame({
    "Nitrogen": Nitrogen,
    "Potassium": Potassium,
    "Phosphorus": Phosphorus
    "Temperature"
})


df["Temperature"] = Temperature

# Specify the file path where you want to save the Excel file
excel_file = r"C:\Users\dell\OneDrive - Lebanese American University\Desktop\Spring 2024\Mechatronics system design 2\Project\random_values.xlsx"

# Write the DataFrame to an Excel file
df.to_excel(excel_file, index=False)
