# Quora Duplicate Question Pair Detection

This project aims to detect whether two given questions are the same or different using the Quora Duplicate Question Pair dataset. The project is hosted using Streamlit and employs a RandomForest classifier. 

## Overview
The goal of this project is to determine if two questions are semantically equivalent. This is achieved by training a machine learning model on the Quora Duplicate Question Pair dataset. The model is hosted using Streamlit, providing an interactive web interface for users to test the model with their own question pairs.

## Livedemo
You can check out the live hosted version of the site [here](https://sudarshanpoudel-duplicate-question-detection-app-i6yghp.streamlit.app/).<br>
or simply open notebook to test it in colab [here](https://colab.research.google.com/github/SudarshanPoudel/Duplicate_question_detection/blob/main/notebook/notebook.ipynb).

## Installation
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Quora-Duplicate-Question-Pair-Detection.git
   cd Quora-Duplicate-Question-Pair-Detection
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

## Model Details
The model used in this project is a RandomForest classifier trained on the Quora Duplicate Question Pair dataset. The previous model achieved an accuracy of 0.8345 but was around 240MB in size. The current model, optimized for size, is only 21MB and achieves an accuracy of 0.81885.
Tfidf vectorization is used for converting text into numeric vector, while lots of other features are manually extracted.

### Dataset USed
Quora Duplicate Question Pair dataset
[Kaggle_quora_dataset](https://www.kaggle.com/c/quora-question-pairs)

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any changes you'd like to make.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
