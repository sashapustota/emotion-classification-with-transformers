# Importing packages
from transformers import pipeline
import pandas as pd
import os
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="fake_or_real_news.csv", help="Name of the CSV file to use.")
    parser.add_argument("--column", type=str, default="title", help="Name of the column with text data in the CSV file.")
    parser.add_argument("--label", type=str, default="label", help="Name of the column with categories in the CSV file.")
    parser.add_argument("--islabel", type=bool, default=True, help="Whether or not to plot the data with categories.")
    args = parser.parse_args()
    return args

def pipeline_setup():
    classifier = pipeline("text-classification", 
                        model="j-hartmann/emotion-english-distilroberta-base", 
                        return_all_scores=False) # Only return the most likely label
    return classifier

def load_data(data_arg):
    filename = os.path.join(os.getcwd(), "data", data_arg) # load the data
    data = pd.read_csv(filename, index_col=0)
    return data

def perform_emotion_classification(data, classifier, column_arg):
    emotion_classification = []
    
    print("[INFO]: Starting emotion classification...")

    for headline in data[column_arg]:
        classification = classifier(headline)
        emotion_classification.append(classification[0]["label"])
    
    # Add the emotion classification to the data
    data["emotion"] = emotion_classification

def plot_data(data, label_arg, label_bool_arg):
    # Define list of emotions for ordering
    emotions = data["emotion"].unique().tolist()

    # Making plot with all data
    all_data_plot = sns.countplot(x="emotion", data=data, order = emotions)
    all_data_plot.set_title("Distribution of emotions accross all data")
    all_data_plot.set_xlabel("Emotion")
    all_data_plot.set_ylabel("Count")
    all_data_fig = all_data_plot.get_figure()
    all_data_fig.savefig(os.path.join(os.getcwd(), "plots", "all_data_plot.png"))
    all_data_fig.clf()

    if label_bool_arg == True:

        # Plot with real news only
        separated_plot = sns.countplot(x="emotion", data=data, order = emotions, hue = label_arg)
        separated_plot.set_title("Distribution of emotions accross categories")
        separated_plot.set_xlabel("Emotion")
        separated_plot.set_ylabel("Count")
        separated_fig = separated_plot.get_figure()
        separated_fig.savefig(os.path.join(os.getcwd(), "plots", "category_plot.png"))
        separated_fig.clf()

def main(): # This is the main function that runs the program.
    args = parse_args()
    classifier = pipeline_setup()
    data = load_data(args.data)
    perform_emotion_classification(data, classifier, args.column)
    print("[INFO]: Done with emotion classification of headlines.")
    plot_data(data, args.label, args.islabel)
    print("[INFO]: Plots saved to plots folder.")
    
if __name__ == "__main__":
    main()