## Battery Performance Analysis

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

To run the project locally, follow these steps:

 Clone this repository:

   '''bash
   git clone https://github.com/Jatin-kumar-10/Battery-Performance-Analysis.git
   cd Battery-Performance-Analysis


## Dependencies

The following Python libraries are required to run this project:

- **pandas**
- **plotly**
- **matplotlib**
- **seaborn**

You can install them by running:

'''bash
pip install pandas plotly matplotlib seaborn

### Usage

After setting up the environment and installing the dependencies, you can run the analysis script as follows:

'''bash
python battery_analysis.py

This script will read the metadata and battery data files, clean the data, and generate plots for battery impedance, resistance, and capacity over the test cycles.
