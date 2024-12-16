#  libraries required
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

#  CSV file path
file_path = r'C:\Users\tsmxj\OneDrive\Desktop\juipter\metadata.csv'  #change this as per your path of file

# Reading the metadata CSV file 
df = pd.read_csv(file_path)

# Function to convert start_time from a list-like string to a proper datetime object
def convert_start_time(time_list):
    try:
        # Evaluate the string representation of the list and convert it to datetime
        time_list = eval(time_list)
        return pd.to_datetime(f"{time_list[0]}-{time_list[1]}-{time_list[2]} {time_list[3]}:{time_list[4]}:{time_list[5]}")
    except:
        # If the conversion fails, return NaT (Not a Time)
        return pd.NaT

# Applying the conversion function to the 'start_time' column
df['start_time'] = df['start_time'].apply(convert_start_time)

# List of numeric columns that need to be converted and cleaned
numeric_columns = ['Re', 'Rct', 'Capacity']

# Ensuring all numeric columns are converted to numeric types and handling invalid values
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Invalid values are replaced with NaN

# Filling missing values in 'Re' and 'Rct' with their respective median values
df['Re'] = df['Re'].fillna(df['Re'].median())
df['Rct'] = df['Rct'].fillna(df['Rct'].median())

# Filling missing values in 'Capacity' with the mean of the column
df['Capacity'] = df['Capacity'].fillna(df['Capacity'].mean())

# Defining the list of relevant columns that we want to retain in the DataFrame
relevant_columns = ['type', 'start_time', 'ambient_temperature', 'battery_id', 'test_id', 'uid', 'filename', 'Capacity', 'Re', 'Rct']

# Looping through all columns in the DataFrame and assigning a default value (1) to irrelevant columns
for column in df.columns:
    if column not in relevant_columns:
        df[column] = 1

# Resetting the index of the DataFrame after modifications
df.reset_index(drop=True, inplace=True)

# File path to save the cleaned metadata DataFrame
cleaned_file_path = r'C:\Users\tsmxj\OneDrive\Desktop\juipter\cleaned_metadata.csv'  #change path here also

# Saving the cleaned DataFrame to a new CSV file
df.to_csv(cleaned_file_path, index=False)

# Plotting 'Re' (Electrolyte Resistance) vs Test Cycles
fig_re = go.Figure()
fig_re.add_trace(go.Scatter(
    x=df['test_id'],  # Test cycle ID on the x-axis
    y=df['Re'],       # Re (Electrolyte Resistance) on the y-axis
    mode='lines+markers',
    name='Re (Electrolyte Resistance)',
    line=dict(color='blue')  # Line color
))
fig_re.update_layout(
    title='Re vs Test Cycles',
    xaxis_title='Test Cycles',
    yaxis_title='Re (Ohms)',
    template='plotly_dark'
)
fig_re.show()

# Plotting 'Rct' (Charge Transfer Resistance) vs Test Cycles
fig_rct = go.Figure()
fig_rct.add_trace(go.Scatter(
    x=df['test_id'],  # Test cycle ID on the x-axis
    y=df['Rct'],      # Rct (Charge Transfer Resistance) on the y-axis
    mode='lines+markers',
    name='Rct (Charge Transfer Resistance)',
    line=dict(color='green')  # Line color
))
fig_rct.update_layout(
    title='Rct vs Test Cycles',
    xaxis_title='Test Cycles',
    yaxis_title='Rct (Ohms)',
    template='plotly_dark'
)
fig_rct.show()

# Plotting Battery Impedance (battery_id is used here, though it may not represent impedance correctly)
fig_impedance = go.Figure()
fig_impedance.add_trace(go.Scatter(
    x=df['test_id'],  # Test cycle ID on the x-axis
    y=df['battery_id'],  # Battery ID on the y-axis (placeholder for impedance)
    mode='lines+markers',
    name='Battery Impedance',
    line=dict(color='red')  # Line color
))
fig_impedance.update_layout(
    title='Battery Impedance vs Test Cycles',
    xaxis_title='Test Cycles',
    yaxis_title='Impedance (Ohms)',
    template='plotly_dark'
)
fig_impedance.show()

# Plotting histograms for the distributions of Re, Rct, and Capacity
plt.figure(figsize=(12, 8))  # Setting the figure size
df[['Re', 'Rct', 'Capacity']].hist(bins=30, figsize=(12, 8), edgecolor='black')  # Creating histograms
plt.suptitle('Distribution of Re, Rct, and Capacity', fontsize=16)  # Adding a title
plt.tight_layout()  # Adjusting layout for better readability
plt.show()

# Filling any remaining missing values with zero to avoid errors during correlation analysis
df[['Re', 'Rct', 'Capacity', 'ambient_temperature']] = df[['Re', 'Rct', 'Capacity', 'ambient_temperature']].fillna(0)

# Plotting a heatmap to show correlations between key numeric variables
plt.figure(figsize=(8, 6))  # Setting the figure size
corr = df[['Re', 'Rct', 'Capacity', 'ambient_temperature']].corr()  # Calculating the correlation matrix
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)  # Plotting the heatmap
plt.title('Correlation Heatmap', fontsize=16)  # Adding a title
plt.show()
