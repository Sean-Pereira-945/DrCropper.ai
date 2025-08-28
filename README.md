Crop Recommender AI
Empowering Smart Farming for a Sustainable Future
<br>

<p align="center">
<img src="https://img.shields.io/badge/build-passing-brightgreen" alt="Build Status">
<img src="https://img.shields.io/github/repo-size/your-username/your-repo-name" alt="Repo Size">
<img src="https://img.shields.io/badge/dependencies-up%20to%20date-blue" alt="Dependencies">
</p>

<p align="center">
Built with the tools and technologies:
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
</p>

Table of Contents
Overview

Getting Started

Prerequisites

Installation

Usage

Model Details

Contributing

Overview
Crop Recommender AI is an open-source developer tool that provides a machine learning-powered API and web interface for crop recommendation based on environmental and soil data. It streamlines the integration of predictive analytics into agricultural applications, enabling smarter crop selection for farmers.

This project aims to facilitate crop decision support through a robust backend and an engaging frontend. The core features include:

📈 Data-Driven Insights: Leverages a dataset of soil and climate parameters to provide accurate crop suggestions.

🤖 Pre-trained Model: Utilizes a Random Forest classifier trained on agricultural data for precise predictions based on factors like soil fertility, temperature, rainfall, pH, and humidity.

🔌 API Integration: A Flask-based API that accepts environmental inputs and returns crop suggestions, making it easy to embed into larger systems.

💻 User Interface: An intuitive web page where users can input environmental factors and receive an instant crop recommendation.

👨‍💻 Developer Friendly: Clear code structure and integration points to accelerate deployment and customization.

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
This project requires the following dependencies:

Programming Language: Python 3.8+

Package Manager: pip

You will also need the following Python libraries, which are listed in requirements.txt:

scikit-learn

pandas

numpy

flask

Installation
Clone the repository:

git clone https://github.com/your-username/your-repo-name.git

Navigate to the project directory:

cd your-repo-name

Install the required packages:

pip install -r requirements.txt

Usage
Run the Flask application:

python app.py

Open your web browser and navigate to http://127.0.0.1:5000 to access the user interface.

Enter the environmental factors into the form to get a crop recommendation.

Model Details
The core of this project is a Random Forest Classifier. This model was chosen for its high accuracy and robustness in handling diverse datasets. It was trained on a comprehensive dataset containing the following features:

Nitrogen (N)

Phosphorus (P)

Potassium (K)

Temperature

Humidity

pH

Rainfall

The model predicts one of 22 different crop types.

Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request
