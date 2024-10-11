# Huairou Air Quality Analysis and Dasboard Project

This project aims to analyze air quality data from Huairou stations and visualize the results on a Streamlit dasboard.

## Project Setup

### Step 1: Environment Setup
Open your Anaconda PowerShell prompt, create and activate your environment by typing:  

conda create --name main-air python=3.9

conda activate main-air

### Step 2: Create Project Directory
Create a directory for your project:  
mkdir air_quality 
cd air_quality

### Step 3: Install Required Libraries
Install the necessary libraries for data analysis and visualization:  
pip install numpy pandas scipy matplotlib seaborn jupyter

### Step 4: Install Streamlit
Install Streamlit for the dasboard application:  
pip install streamlit

### Step 5: Data Analysis with Jupyter Notebook
Run Jupyter Notebook:  

jupyter-notebook .  
Create a new notebook called Notebook.ipynb and perform the data analysis using the PRSA dataset found in the Data folder. The dataset is:  
PRSA_Data_Huairou_20130301-20170228.csv 

In the Notebook.ipynb, clean the data by removing missing values and correcting date formats, etc. In the last cell, it will save the datasets and change that into the Dashboard folder as:  
main.csv 

This cleaned datasets will be used in the dasboard.    

### Step 6: Project Folder Structure  
Your project directory should have the following structure:  

air_quality/  
│  
├── Data/  
│   └── PRSA_Data_Huairou_20130301-20170228.csv 
│  
├── Dasboard/     
│   ├── dasboard.py  
│   ├── Huairou.png  
│   └── main.csv 
│  
└── Notebook.ipynb  
│  
└── Readme.md   
│  
└── requirements.txt 
│  
└── url.txt 

### Step 7: Running the Dashboard  
Once the analysis is done and the cleaned dataset are saved in the Dasboard folder, you can run the Streamlit dasboard.  

Navigate to the Dashboard folder and execute the following command:  

cd Dasboard   
streamlit run dasboard.py  

### Step 8: Viewing the Dasboard  
Once the above command is run, Streamlit will provide a local URL in the terminal. Open that URL in your web browser to access the interactive dasboard.  

Notes:  
The dasboard will display trends, correlations, and statistical analysis based on PM2.5 air quality data from Huairou station.  
The image Huairou.png is required in the Dasboard folder for the sidebar in the Streamlit dasboard.  