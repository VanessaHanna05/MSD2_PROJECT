import random
import pandas as pd
import numpy as np

def generate_clustered_values(total_values, cluster_center, std_deviation):
    lower_bound = max(0, cluster_center - 3 * std_deviation)
    upper_bound = min(150, cluster_center + 3 * std_deviation)
    mid_cluster = (upper_bound + lower_bound) // 2

    # Generate clustered values around cluster_center with Gaussian distribution
    clustered_values = [max(lower_bound, min(upper_bound, int(random.gauss(cluster_center, std_deviation)))) for _ in range(total_values)]
    return clustered_values

def add_noise(values, noise_percent, out_of_range_percent):
    num_noise = int(len(values) * noise_percent)
    num_out_of_range = int(len(values) * out_of_range_percent)

    # Add noise to the values array
    for _ in range(num_noise):
        index = random.randint(0, len(values) - 1)
        if random.random() < 0.5:
            values[index] += random.randint(0, 50)  # Add random positive noise
        else:
            values[index] -= random.randint(0, 50)  # Add random negative noise

    # Add out-of-range values
    for _ in range(num_out_of_range):
        index = random.randint(0, len(values) - 1)
        if random.random() < 0.5:
            values[index] = random.randint(151, 200)  # Add out-of-range positive value
        else:
            values[index] = random.randint(-50, -1)   # Add out-of-range negative value

    return values

def generate_balanced_temp_values(total_values, temp_min, temp_max, noise_percent):
    balanced_values = []
    lower_bound = max(-100, temp_min)  # Ensure lower bound is not below -100
    upper_bound = min(200, temp_max)   # Ensure upper bound is not above 200

    # Generate temperature values
    while len(balanced_values) < total_values:
        value = random.randint(lower_bound, upper_bound)
        balanced_values.append(value)  # Ensure value is within bounds

    # Add noise
    num_noise = int(total_values * noise_percent)
    for _ in range(num_noise):
        index = random.randint(0, len(balanced_values) - 1)
        balanced_values[index] += random.randint(-10, 10)  # Add random noise

    return balanced_values

#assuming the due point temperature in lebanon is 15 degrees

def generate_humidity_values(temperature_values):

    A = 17.625
    B = 243.04
    dew_point_temp = 15

    humidity_values = []
    for temp in temperature_values:
        e_td = np.exp((A * dew_point_temp) / (B + dew_point_temp))
        e_t = np.exp((A * temp) / (B + temp))
        
        # Calculate relative humidity
        RH = 100 * (e_td / e_t)
        humidity_values.append(int(round(RH)))

    return humidity_values

def estimate_rain_intensity(temperature, humidity):
    # Define temperature and humidity thresholds
    temp_threshold = 20  # Example temperature threshold in Celsius
    humidity_threshold = 70  # Example humidity threshold in percentage

    # If both temperature and humidity exceed their respective thresholds, assume higher probability of rain
    if temperature < temp_threshold and humidity > humidity_threshold:
        return "Very High"
    elif temperature < temp_threshold and humidity <= humidity_threshold:
        return "High"
    elif temperature >= temp_threshold and humidity > humidity_threshold:
        return "Medium"
    elif temperature >= temp_threshold and humidity <= humidity_threshold:
        return "Low"
    else:
        return "Very Low"

def estimate_soil_recommendation(temp_values, hum_values, rain_values):
    soil_recommendation = []
    for temp, hum, rain in zip(temp_values,hum_values,rain_values):
        if temp < 15 and hum < 45:
            if rain == "Very Low":
                soil_recommendation.append("Low NPK")
            elif rain == "Low":
                soil_recommendation.append("Low NPK")
            elif rain == "Medium":
                soil_recommendation.append("Medium NPK")
            elif rain == "High":
                soil_recommendation.append("Medium NPK")
            elif rain == "Very High":
                soil_recommendation.append("High NPK")

        elif temp >= 15 and temp < 25 and hum >= 45:
            if rain == "Very Low":
                soil_recommendation.append("Low NPK")
            elif rain == "Low":
                soil_recommendation.append("Low NPK")
            elif rain == "Medium":
                soil_recommendation.append("Medium NPK")
            elif rain == "High":
                soil_recommendation.append("Medium NPK")
            elif rain == "Very High":
                soil_recommendation.append("High NPK")

        elif temp >= 25 and hum < 45:
            if rain == "Very Low":
                soil_recommendation.append("Low NPK")
            elif rain == "Low":
                soil_recommendation.append("Low NPK")
            elif rain == "Medium":
                soil_recommendation.append("Medium NPK")
            elif rain == "High":
                soil_recommendation.append("Medium NPK")
            elif rain == "Very High":
                soil_recommendation.append("High NPK")

        elif temp < 15 and hum >= 45:
            if rain == "Very Low":
                soil_recommendation.append("Low NPK")
            elif rain == "Low":
                soil_recommendation.append("Low NPK")
            elif rain == "Medium":
                soil_recommendation.append("Medium NPK")
            elif rain == "High":
                soil_recommendation.append("High NPK")
            elif rain == "Very High":
                soil_recommendation.append("High NPK")

        elif temp >= 25 and hum >= 45:
            if rain == "Very Low":
                soil_recommendation.append("Low NPK")
            elif rain == "Low":
                soil_recommendation.append("Medium NPK")
            elif rain == "Medium":
                soil_recommendation.append("Medium NPK")
            elif rain == "High":
                soil_recommendation.append("High NPK")
            elif rain == "Very High":
                soil_recommendation.append("High NPK")

        elif temp >= 15 and temp < 25 and hum < 45:
            if rain == "Very Low":
                soil_recommendation.append("Low NPK")
            elif rain == "Low":
                soil_recommendation.append("Low NPK")
            elif rain == "Medium":
                soil_recommendation.append("Low NPK")
            elif rain == "High":
                soil_recommendation.append("Medium NPK")
            elif rain == "Very High":
                soil_recommendation.append("High NPK")

    return soil_recommendation

# Rules for Nitrogen (N)
def generate_nitrogen_recommendation(temp, hum, rain, prev_n):
    if temp > 25 and hum > 50 and rain == "High":
        return prev_n + 5 if prev_n < 30 else 30
    elif temp < 15 and hum < 40 and rain == "Low":
        return prev_n - 3 if prev_n > 20 else 20
    elif temp > 20 and hum > 60 and rain == "Medium":
        return prev_n + 3 if prev_n < 28 else 28
    elif temp > 20 and hum > 70 and rain == "Very High":
        return prev_n + 2 if prev_n < 25 else 25
    elif temp < 20 and hum < 50 and rain == "Low":
        return prev_n - 2 if prev_n > 22 else 22
    elif temp > 30 and hum > 50 and rain == "High":
        return prev_n + 2 if prev_n < 32 else 32
    elif temp < 15 and hum > 60 and rain == "Medium":
        return prev_n - 4 if prev_n > 18 else 18
    elif temp > 20 and hum < 40 and rain == "Low":
        return prev_n + 3 if prev_n < 23 else 23
    elif temp < 20 and hum > 70 and rain == "Very Low":
        return prev_n + 2 if prev_n < 27 else 27
    elif temp > 20 and hum < 50 and rain == "Medium":
        return prev_n + 4 if prev_n < 29 else 29
    else:
        return prev_n + 1 if prev_n < 25 else 25  # Default value

# Rules for Phosphorus (P)
def generate_phosphorus_recommendation(temp, hum, rain, prev_p):
    if temp > 25 and hum > 50 and rain == "High":
        return prev_p + 3 if prev_p < 15 else 15
    elif temp < 15 and hum < 40 and rain == "Low":
        return prev_p - 2 if prev_p > 6 else 6
    elif temp > 20 and hum > 60 and rain == "Medium":
        return prev_p + 2 if prev_p < 13 else 13
    elif temp > 20 and hum > 70 and rain == "Very High":
        return prev_p + 1 if prev_p < 12 else 12
    elif temp < 20 and hum < 50 and rain == "Low":
        return prev_p - 1 if prev_p > 10 else 10
    elif temp > 30 and hum > 50 and rain == "High":
        return prev_p + 2 if prev_p < 14 else 14
    elif temp < 15 and hum > 60 and rain == "Medium":
        return prev_p - 3 if prev_p > 8 else 8
    elif temp > 20 and hum < 40 and rain == "Low":
        return prev_p + 1 if prev_p < 11 else 11
    elif temp < 20 and hum > 70 and rain == "Very Low":
        return prev_p - 2 if prev_p > 10 else 10
    elif temp > 20 and hum < 50 and rain == "Medium":
        return prev_p + 3 if prev_p < 13 else 13
    else:
        return prev_p + 1 if prev_p < 12 else 12  # Default value

# Rules for Potassium (K)
def generate_potassium_recommendation(temp, hum, rain, prev_k):
    if temp > 25 and hum > 50 and rain == "High":
        return prev_k + 10 if prev_k < 50 else 50
    elif temp < 15 and hum < 40 and rain == "Low":
        return prev_k - 5 if prev_k > 10 else 10
    elif temp > 20 and hum > 60 and rain == "Medium":
        return prev_k + 5 if prev_k < 40 else 40
    elif temp > 20 and hum > 70 and rain == "Very High":
        return prev_k + 8 if prev_k < 45 else 45
    elif temp < 20 and hum < 50 and rain == "Low":
        return prev_k - 3 if prev_k > 15 else 15
    elif temp > 30 and hum > 50 and rain == "High":
        return prev_k + 5 if prev_k < 48 else 48
    elif temp < 15 and hum > 60 and rain == "Medium":
        return prev_k - 2 if prev_k > 20 else 20
    elif temp > 20 and hum < 40 and rain == "Low":
        return prev_k - 2 if prev_k > 18 else 18
    elif temp < 20 and hum > 70 and rain == "Very Low":
        return prev_k - 5 if prev_k > 10 else 10
    elif temp > 20 and hum < 50 and rain == "Medium":
        return prev_k + 8 if prev_k < 38 else 38
    else:
        return prev_k + 3 if prev_k < 30 else 30  # Default value


    

    



total_values = 1500
noise_percent = 0.2
out_of_range_percent = 0.1
NPK_cluster_center = 30
NPK_std_deviation = 28
temp_min = 0
temp_max = 50

# Generate clustered values for Nitrogen, Phosphorus, and Potassium
Nitrogen = generate_clustered_values(total_values, NPK_cluster_center, NPK_std_deviation)
Phosphorus = generate_clustered_values(total_values, NPK_cluster_center, NPK_std_deviation)
Potassium = generate_clustered_values(total_values, NPK_cluster_center, NPK_std_deviation)

# Add noise to the arrays
Nitrogen = add_noise(Nitrogen, noise_percent, out_of_range_percent)
Phosphorus = add_noise(Phosphorus, noise_percent, out_of_range_percent)
Potassium = add_noise(Potassium, noise_percent, out_of_range_percent)

# Generate temperature values
Temperature = generate_balanced_temp_values(total_values, temp_min, temp_max, noise_percent)

# Generate humidity values based on temperature
Humidity = generate_humidity_values(Temperature)

# Estimate rain intensity based on temperature and humidity
Rain_intensity = [estimate_rain_intensity(temp, hum) for temp, hum in zip(Temperature, Humidity)]

# Estimate soil recommendation based on temperature, humidity, and rain intensity
Soil_recommendation = estimate_soil_recommendation(Temperature, Humidity, Rain_intensity)

recommended_N = []
recommended_P = []
recommended_K = []
for temp, rain, hum, rec_n, rec_p, rec_k in zip(Temperature, Rain_intensity, Humidity, Nitrogen, Nitrogen, Potassium):
    recommended_N.append(generate_nitrogen_recommendation(temp,hum, rain,rec_n))
    recommended_P.append(generate_phosphorus_recommendation(temp,hum, rain,rec_p))
    recommended_K.append(generate_potassium_recommendation(temp,hum, rain,rec_k))

added_N = []
added_P = []
added_K = []


# Create a DataFrame with seven columns
df = pd.DataFrame({
    "Nitrogen": Nitrogen,
    "Phosphorus": Phosphorus,
    "Potassium": Potassium,
    "Temperature": Temperature,
    "Humidity": Humidity,
    "Rain Intensity": Rain_intensity,
    "Soil Recommendation": Soil_recommendation,
    "Recommended_N":recommended_N,
    "Recommended_P":recommended_P,
    "Recommended_K":recommended_K,
})

# Specify the file path where you want to save the Excel file
excel_file = r"C:\Users\dell\OneDrive - Lebanese American University\Desktop\Spring 2024\Mechatronics system design 2\Project\random_values.xlsx"

# Write the DataFrame to an Excel file
df.to_excel(excel_file, index=False)
