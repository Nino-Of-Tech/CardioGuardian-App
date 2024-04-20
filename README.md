# CardioGuardian :heartbeat:


CardioGuardian is a Machine Learning model built to predict the likelihood of heart disease based on various health parameters. This project utilizes a dataset sourced from Kaggle containing comprehensive information about patients' health attributes and the presence of heart disease.

## Project Description :man_scientist:
This project aims to create a predictive model that can assist in early detection of heart disease, thereby enabling proactive measures for better healthcare management. The model is developed and trained on Google Collab Notebooks and deployed using <a href="https://streamlit.io/" target="_blank">Streamlit</a>, providing a user-friendly interface for easy access and interaction.

## Dataset :bar_chart:
The dataset used for training and testing the model is available on Kaggle. You can access it <a href="https://www.kaggle.com/datasets/lourenswalters/uci-heart-disease-data-set" target="_blank">here</a>.

Although, the data is originally collected by the University of California, Irvine. It can be found on their Machine Learning Repository Archive <a href="https://archive.ics.uci.edu/dataset/45/heart+disease" target="_blank">here</a>. 

## Setup Instructions :desktop_computer:
Follow these steps to set up and run the CardioGuardian project locally:

**1. Clone the Repository:**

```bash
git clone https://github.com/Nino-Of-Tech/CardioGuardian-App.git
```

**2. Install Dependencies:**

Navigate to the project directory and install the required dependencies using pip:

```bash
cd CardioGuardian-App
pip install -r requirements.txt
```

**3. Run the Application:**

Start the Streamlit application by running the following command:


```bash
streamlit run app.py
```


This will launch a local server, and you can access the application in your web browser at **http://localhost:8501.**


**4. Interact with the Model:**
Once the application is running, you can input health parameters and get predictions regarding the likelihood of a heart disease.


## How To Use CardioGuardian :thermometer:

* Click on this <a href="https://cardioguardian.streamlit.app/" target="_blank">CardioGuardian App</a> link and you will be redirected to the app homepage. 
* Input your health data including your blood pressure, age, cholesterol levels, blood sugar, amongst other necessary information.  
* Once you are done inputting the required health information, in less than one second, your heart disease prediction will display. 


## Feedback and Contributions :repeat:
Your feedback is valuable for improving CardioGuardian. If you encounter any issues or have suggestions for enhancements, feel free to open an issue in the GitHub repository. Contributions are also welcome through pull requests.


## Author :pen:
* <a href="https://linkedin.com/in/ninonwachukwu" target="_blank">Nino Chibuzor Nwachukwu</a>