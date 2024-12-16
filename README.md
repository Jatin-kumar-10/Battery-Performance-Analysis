# Battery Performance Analysis

This project focuses on analyzing the performance and aging of Li-ion batteries. Using data collected from multiple experiments, the aim is to understand how different battery parameters change over time, especially during charge/discharge cycles. The key metrics analyzed are:

- **Battery Impedance**
- **Electrolyte Resistance (Re)**
- **Charge Transfer Resistance (Rct)**
- **Battery Capacity**

This analysis helps in understanding battery aging and performance degradation over cycles, which is crucial for applications like electric vehicles, energy storage systems, and portable electronics.

## Key Features

- Data preprocessing: Cleaning and converting columns to the correct formats.
- Data visualization: Using Plotly and Matplotlib for creating dynamic and static visualizations.
- Statistical analysis: Correlation analysis between battery parameters and environmental conditions.
- Easy-to-understand plots showcasing how impedance, resistance, and capacity evolve over time.

## Installation

### Step 1: Download the Dataset from Kaggle

1. Visit the following [Kaggle dataset page](https://www.kaggle.com/datasets/patrickfleith/nasa-battery-dataset/data).
2. Click on the "Download" button to get the dataset. It will be a ZIP file containing multiple CSV files.
3. After downloading, unzip the file to a directory of your choice.

### Step 2: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Jatin-kumar-10/Battery-Performance-Analysis.git
cd Battery-Performance-Analysis
```

### Step 3: Update the File Paths
In the battery_analysis.py script, you need to update the path to the metadata.csv file (or any other CSV files you are using) to match the location where you unzipped the dataset.

Locate the line in your battery_analysis.py script where the metadata.csv file is being read, and modify the path to point to the correct location:
