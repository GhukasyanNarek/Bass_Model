# Innovation Diffusion Analysis using the Bass Model

## Project Overview
This project analyzes the diffusion of **Matic Robots Matic**, a next-generation robotic vacuum cleaner, using the **Bass Diffusion Model**. The study leverages **historical adoption data from iRobot Roomba** to estimate market penetration and future adoption trends for Matic Robots Matic.

The project consists of:
- **Data analysis on iRobot revenue (2012-2023)** to estimate Bass Model parameters.
- **Diffusion forecasting for Matic Robots Matic (2024-2040)** using those parameters.
- **Visualizations for revenue trends, cumulative adoption, and adoption rates.**
- **A structured report detailing the methodology and insights.**

## Repository Structure
```
├── data/                   # Directory for datasets (if applicable)
├── img/                    # Directory for images used in the report
├── report/                 # Contains the final report and source files
│   ├── report.pdf          # Final project report in PDF format
│   ├── report_source.md    # Markdown source for report generation
├── main.ipynb              # Main Jupyter Notebook for analysis
├── utility_functions.py     # Script containing utility functions for the analysis
├── README.md               # Project documentation and setup instructions
```
## Setup Instructions

To run this project, ensure you have **Python** and **Jupyter Notebook** installed on your system. Follow these steps to set up the environment:

### 1. Clone the Repository
```sh
git clone [<repository-url>](https://github.com/GhukasyanNarek/Bass_Model/new/master?filename=README.md)
cd Bass_Model
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)
```sh
python -m venv env
# Activate virtual environment:
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run Jupyter Notebook
```sh
jupyter lab
```
Then, open `main.ipynb` in JupyterLab to explore the analysis.

---

## Usage Guide

### Running the Analysis:
- Open `main.ipynb` in JupyterLab.
- Run the cells step by step to analyze revenue trends and diffusion predictions.
- The notebook imports `utility_functions.py` to keep the code modular.

### Modifying Parameters:
- You can tweak the **Bass Model parameters** in `utility_functions.py` to simulate different adoption scenarios.

### Viewing Results:
- **Generated plots** are saved in the `img/` directory.
- The **final structured report** is available in `report/report.pdf`.

---

## Contributions

Developed by **Narek Ghukasyan**
