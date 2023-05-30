<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Cultural Data Science 2023</h1> 
  <h2 align="center">Assignment 4</h2> 
  <h3 align="center">Language Analytics</h3> 


  <p align="center">
    Aleksandrs Baskakovs
  </p>
</p>


<!-- Assignment instructions -->
## Assignment instructions

In previous assignments, you've done a lot of model training of various kinds of complexity, such as training document classifiers or RNN language models. This assignment is more like Assignment 1, in that it's about *feature extraction*.

For this assignment, you should use ```HuggingFace``` to extract information from the *Fake or Real News* dataset that we've worked with previously.

You should write code and documentation which addresses the following tasks:

- Initalize a ```HuggingFace``` pipeline for emotion classification
- Perform emotion classification for every *headline* in the data
- Assuming the most likely prediction is the correct label, create tables and visualisations which show the following:
  - Distribution of emotions across all of the data
  - Distribution of emotions across *only* the real news
  - Distribution of emotions across *only* the fake news
- Comparing the results, discuss if there are any key differences between the two sets of headlines

<!-- ABOUT THE PROJECT -->
## About the project
This repository contains a Python script ```main.py``` that performs emotion classification on textual data using the ```HuggingFace``` pipeline. The script takes as input a dataset of text entries (and relevant categories) and outputs a visualization of a distribution of emotions across the data.

<!-- Data -->
## Data
The sample dataset used for this project is the Fake News Dataset. The dataset contains 10556 news articles, each labeled as either "REAL" or "FAKE". The dataset is available in the ```data``` folder. However, your own dataset can be used as well, as long as it has a similar structure - a single ```.csv``` file with at least one column with the text data. The file needs to be placed in the ```data``` folder. If you data contains additional categories, they can be used for visualization as well.

<!-- Model -->
## Model
The `j-hartmann/emotion-english-distilroberta-base` transformer model from the HuggingFace platform (Jochen Hartmann, "Emotion English DistilRoBERTa-base". [HuggingFace link](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/), 2022) was used to perform emotion classification. The model is a finetuned version of the `distilroberta-base` model. It predicts Ekman's 6 basic emotions plus a neutral class: `anger`, `disgust`, `fear`, `joy`, `neutral`, `sadness` and `surprise`.

<!-- USAGE -->
## Usage
To use the code you need to adopt the following steps.

**NOTE:** Please note that the instructions provided here have been tested on a Mac machine running macOS Ventura 13.1, using Visual Studio Code version 1.76.0 (Universal) and a Unix-based bash terminal. While they should also be compatible with other Unix-based systems like Linux, slight variations may exist depending on the terminal and operating system you are using. To ensure a smooth installation process and avoid potential package conflicts, it is recommended to use the provided ```setup.sh``` bash file, which includes the necessary steps to create a virtual environment for the project. However, if you encounter any issues or have questions regarding compatibility on other platforms, please don't hesitate to reach out for assistance.

1. Clone repository
2. Run ``setup.sh`` in the terminal
3. Activate the virtual environment
4. Run ```main.py``` in the terminal
5. Deactivate the virtual environment

### Clone repository

Clone repository using the following lines in the your terminal:

```bash
git clone https://github.com/sashapustota/emotion-classification-with-transformers
cd emotion-classification-with-transformers
```

### Run ```setup.sh```

The ``setup.sh`` script is used to automate the installation of project dependencies and configuration of the environment. By running this script, you ensure consistent setup across different environments and simplify the process of getting the project up and running.

The script performs the following steps:

1. Creates a virtual environment for the project
2. Activates the virtual environment
3. Installs the required packages
4. Deactivates the virtual environment

To run the script, run the following line in the terminal:

```bash
bash setup.sh
```

### Activate virtual environment

To activate the newly created virtual environment, run the following line in the terminal:

```bash
source ./emotion-classification-with-transformers-venv/bin/activate
```

### Run ```main.py```

The ```main.py``` script performs the following steps:

1. Loads the data
2. Initializes a ```HuggingFace``` pipeline for emotion classification
3. Performs emotion classification for every text entry in the data
4. Creates visualizations which show the distribution of emotions across the data and saves them in the ```plots``` folder

To use the script with the provided sample data, run the following line in the terminal:

```bash
python3 src/main.py
```

If you are using your own data, the script allows for the following optional arguments:

```
main.py [-h] [--data DATA] [--column COLUMN] [--label LABEL] [--islabel ISLABEL]

options:
  --data DATA     Name of the CSV file to use. (default: fake_or_real_news.csv)
  --column COLUMN Name of the column with text data in the CSV file. (default: title)
  --label LABEL   Name of the column with categories in the CSV file. (default: label)
  --islabel ISLABEL
                  Whether or not to plot the data with categories. (default: True)
```

For example, if you have a CSV file named ```my_data.csv``` with text data in the column ```text``` and categories in the column ```category```, you can run the following line in the terminal:

```bash
python3 src/main.py --data my_data.csv --column text --label category
```

### Deactivate virtual environment

When you are done using the script, you can deactivate the virtual environment by running the following line in the terminal:

```bash
deactivate
```

<!-- REPOSITORY STRUCTURE -->
## Repository structure
This repository has the following structure:
```
│   .gitignore
│   README.md
│   requirements.txt
│   setup.sh
│
├───data
│       fake_or_real_news.csv
│
├───plots
│       sample_all_data_plot.png
│       sample_category_plot.png       
│
└───src
        main.py

```
<!-- RESULTS -->
## Results
The following results were obtained using the provided sample data.

![All data plot](https://github.com/sashapustota/emotion-classification-with-transformers/blob/main/plots/sample_all_data_plot.png)

![Category plot](https://github.com/sashapustota/emotion-classification-with-transformers/blob/main/plots/sample_category_plot.png)