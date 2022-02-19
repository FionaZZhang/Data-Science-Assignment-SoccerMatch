# This is the file you will need to edit in order to complete assignment 1
# You may create additional functions, but all code must be contained within this file


# Some starting imports are provided, these will be accessible by all functions.
# You may need to import additional items

from collections import defaultdict
import csv
import json
from matplotlib import pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
from numpy import arange
from numpy.linalg import norm
import os
import pandas as pd
import re
import seaborn as sns
import string


# You should use these two variable to refer the location of the JSON data file and the folder containing the news articles.
# Under no circumstances should you hardcode a path to the folder on your computer (e.g. C:\Chris\Assignment\data\data.json) as this path will not exist on any machine but yours.

# Global variables
datafilepath = 'data/data.json'
articlespath = 'data/football'

# Json file global variables
teams_codes = 'teams_codes'
clubs_info = 'clubs'

# Clubs_info global variables
club_code = 'club_code'
goals_scored = 'goals_scored'
goals_conceded = 'goals_conceded'
club_name = 'name'

# New file names
task2_csv = 'task2.csv'
task3_csv = 'task3.csv'
task4_csv = 'task4.csv'
task4_png = 'task4.png'
task5_csv = 'task5.csv'
task5_png = 'task5.png'
task6_png = 'task6.png'
task7_png = 'task7.png'
task9_csv = 'task9.csv'


def task1():
    ''' Loads the file into python, return a list of teams_codes in sorted alphabetical order.
    '''
    # Declaring variables
    filename = datafilepath
    
    with open(filename, 'r') as fp:
        data = json.load(fp)
    
    return list(sorted(data[teams_codes]))


def task2():
    ''' Create a csv 'task2.csv' that shows the goals scored by and against each team
    '''
    
    # Declaring variables
    team_codes = task1() # get a sorted list of teams codes
    
    # Open json file, return a json object
    with open(datafilepath, 'r') as fp:
        data = json.load(fp)
        
        # Write data in a new csv file
        header = ['team_code', 'goals_scored_by_team', 'goals_scored_against_team']
        with open(task2_csv, "w") as fp_csv:
            writer = csv.writer(fp_csv)
            writer.writerow(header)
            
            # For each team in the sorted list, write the goals scored by and against them in the csv
            for code in team_codes:   
                for club in data[clubs_info]:
                    if code == club[club_code]:
                        writer.writerow([code, club[goals_scored], club[goals_conceded]])
                        break
    
    return

    
def task3():
    ''' Produce a csv file containing article's name and the total goals of the largest match score identified in the article
    '''
    
    # Declaring variables
    regex_match = '[^\d]\d{1,2}-\d{1,2}[^\d]'
    regex_score = '\d{1,2}'
    article_list = sorted(os.listdir(articlespath))
    
    # Create a new csv
    header = ['filename', 'total_goals']
    with open(task3_csv, "w") as fp_csv:
        writer = csv.writer(fp_csv)
        writer.writerow(header)
        
        # Iterate over each article name
        for filenames in article_list:
            
            # Open the article
            articles_location = articlespath + '/' + filenames
            with open(articles_location,) as textfile:

                # For each line of text, search match scores using regex, store matches to a list
                matches_text = []
                reg = re.compile(regex_match)
                for lines in textfile:
                    matches_text += reg.findall(lines)
                    
                # Remove the hypens of match scores, store scores in a list
                matches_scores = []
                reg_scores = re.compile(regex_score)
                for scores in matches_text:
                    matches_scores += [reg_scores.findall(scores)]
                    
            # Find the largest score for the article, write into the csv
            maxnum = 0
            largest_match = 0
            for scores in matches_scores:
                total_score = int(scores[0]) + int(scores[1])
                if total_score > largest_match:
                    largest_match = total_score
            writer.writerow([filenames, largest_match]) 
    
    return


def task4():
    ''' Produce a boxplot showing distribution of values for total_goals of each articles, save in 'task4.png'
    '''
    
    # Access the csv data produced by task3, which contains total goals of each articles
    task3()
    data = pd.read_csv(task3_csv)
    total_goals = 'total_goals'
    
    # Create a boxplot showing total_goals of each articles, save as a png
    plt.boxplot(data[total_goals], )
    plt.title('Distribution of Values for Total Goals')
    plt.ylabel('Total Goals')
    plt.savefig(task4_png)
    
    return

    
def task5():
    ''' Produce a csv 'task5.csv' containing club name and number of mentions for each club, and produce a bar chart showing this information, save the bar char as 'task5.png'
    '''

    # Access the json file, return a sorted list of clubs names
    clubs_name = []
    with open(datafilepath, 'r') as fp:
        data = json.load(fp)
        for clubs in data[clubs_info]:
            clubs_name.append(clubs[club_name])
        clubs_name = sorted(clubs_name)
        
    # For each club, count the number of articles that mentioned it and store the count in a dict
    article_list = sorted(os.listdir(articlespath))
    mentions = defaultdict(int)
    for filenames in article_list:
        articles_location = articlespath + '/' + filenames
        with open(articles_location,'r') as textfile:
            text_str = textfile.read()
            for names in clubs_name:
                if names in text_str:
                    mentions[names] += 1
             
    # Store the number of mentions of each club in a csv
    header = ['club_name', 'number_of_mentions']
    with open(task5_csv, "w") as fp_csv:
        writer = csv.writer(fp_csv)
        writer.writerow(header)
        for names in clubs_name:
            writer.writerow([names, mentions[names]])
            
    # Create a bar chart using the data in the csv created, save in task5.png
    data = pd.read_csv(task5_csv)
    plt.clf()
    plt.bar(data['club_name'], data['number_of_mentions'])
    plt.xticks(np.arange(0, 20, step = 1), data['club_name'], fontsize = 7, rotation = 90)
    plt.title('Number of Mentioning Articles for Each Club')
    plt.xlabel('Club Names')
    plt.ylabel('Number of Mentioning Articles')
    plt.tight_layout()
    plt.savefig(task5_png)
    
    return
  
    
def task6():
    ''' Produce a heat map 'task6.png' that shows the similarity scores of each pair of clubs
    '''
    
    # Access the json file, return a sorted list of clubs names
    clubs_name = []
    with open(datafilepath, 'r') as fp:
        data = json.load(fp)
        for clubs in data[clubs_info]:
            clubs_name.append(clubs[club_name])
        clubs_name = sorted(clubs_name)

    # For each club, store the name of the articles that mentioned it in a dict
    article_list = sorted(os.listdir(articlespath))
    mentions = defaultdict(list)
    for filenames in article_list:
        articles_location = articlespath + '/' + filenames
        with open(articles_location,'r') as textfile:
            text_str = textfile.read()
            for names in clubs_name:
                if names in text_str:
                    mentions[names].append(filenames)
                    continue

    # Create a dict that counts the mentions for each pair of clubs and 
    # a dict that stores the similarity scores of each pair of clubs
    pair_mentions = defaultdict(int)
    pair_sim = defaultdict(int)
    for i in range(0, len(clubs_name)):
        for j in range(i + 1, len(clubs_name)):
            club_a = clubs_name[i]
            club_b = clubs_name[j]
            for textfiles in mentions[club_a]:
                if textfiles in mentions[club_b]:
                    pair_mentions[(club_a, club_b)] += 1
            if len(mentions[club_a])+len(mentions[club_b]) != 0:
                pair_sim[(club_a, club_b)] = (2 * pair_mentions[(club_a,club_b)]
                                              /(len(mentions[club_a])+len(mentions[club_b])))
            else:
                pair_sim[(club_a, club_b)] = 0

    # Create a dict that represent a 2D dataframe for the similarity scores
    sim_dataframe = defaultdict(list)
    for i in range(0, len(clubs_name)):
        for j in range(0, len(clubs_name)):
            sim_dataframe['club_names_x'].append(clubs_name[i])
            sim_dataframe['club_names_y'].append(clubs_name[j])
            if i == j:
                sim_dataframe['sim_values'].append(1)
            elif i < j:
                sim_dataframe['sim_values'].append(pair_sim[(clubs_name[i], clubs_name[j])])
            elif i > j:
                sim_dataframe['sim_values'].append(pair_sim[(clubs_name[j], clubs_name[i])])

    # Use the dataframe dict of similarity scores to create heat map
    similarity = pd.DataFrame(sim_dataframe)
    piv = similarity.pivot(index = 'club_names_y', columns='club_names_x', values='sim_values')
    plt.clf()
    sns.heatmap(piv)
    plt.title('Similarity Score for Each Pair of Clubs')
    plt.xlabel('Club Names')
    plt.ylabel('Club Names')
    plt.tight_layout()
    plt.savefig(task6_png)
    
    return
    
    
def task7():
    ''' Produces a scatterplot comparing the number of articles mentioning each team with the total number of goals scored by each team, save the plot as 'task7.png'
    '''
    
    # Access the data from task2 and task5 to get number of goals and number of mentions of each team
    data_goals = pd.read_csv(task2_csv)
    data_mentions = pd.read_csv(task5_csv)
    x = data_goals['goals_scored_by_team']
    y = data_mentions['number_of_mentions']
    
    # Create a scatter plot using those data and save as a png file
    plt.clf()
    plt.scatter(x,y)
    plt.title('Number of Mentioning Articles vs Number of Goals')
    plt.xlabel('Number of Goals Scored by Each Team')
    plt.ylabel('Number of Mentioning Articles')
    plt.tight_layout()
    plt.savefig(task7_png)

    return
    
    
def task8(filepath):
    ''' Take a argument 'filepath' that indicates the location of an article, preprocess the article, return a processed string of the article
    '''

    # Access the article
    with open(filepath, 'r') as article:
        input_str = article.read()
    
    # Remove punctuations
    result = re.sub("[^\w\s]", ' ', input_str)
        
    # Remove numbers
    result = re.sub('[\d]', '', result)

    # Remove spacing characters
    result = re.sub('[\s]+', ' ', result)
    
    # Change letters to lowercase characters
    result = result.lower()
    
    # Tokenize the string
    tokens = word_tokenize(result)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_str = [w for w in tokens if not w in stop_words]
    
    # Remove single characters
    processed_str = [w for w in filtered_str if len(w) > 1] 
    
    return processed_str


def cos_sim(untfidf_dict_a, untfidf_dict_b):
    ''' Take two dictionaries (words as key and the unweighed tfidf as value) as inputs, calculate and return the cosine similarity.
    '''
    sum = 0
    for words in untfidf_dict_a:
        if words in untfidf_dict_b:
            sum += untfidf_dict_a[words] * untfidf_dict_b[words]
    
    return sum


def task9():
    ''' Produce a csv file 'task9.csv' containing the filenames of the 10 pairs of articles with the highest similarities and their similarity score.
    '''
    
    # Get a sorted list of filenames and the total number of files
    articles_list = sorted(os.listdir(articlespath))
    num_documents = len(articles_list)
    
    # Generate a sorted wordlist for all unique words in all files and get df and idf for each words
    all_wordlist = []
    df = defaultdict(int)
    idf = defaultdict(int)
    for filenames in articles_list:
        articles_location = articlespath + '/' + filenames
        words_list = set(task8(articles_location))
        for words in words_list:
            if words not in all_wordlist:
                all_wordlist.append(words)
            df[words] += 1
    all_wordlist = sorted(all_wordlist)    
    for words in all_wordlist:
        idf[words] = np.log((1 + num_documents) / (1 + df[words])) + 1
                                
    # Get the unweighed tfidf for each word for each file, store in dictionary 'all_vectors'
    all_vectors = dict()
    for filenames in articles_list:
        articles_location = articlespath + '/' + filenames
        words_list = task8(articles_location)
        
        # Get tf for each word
        tf = defaultdict(int)
        for words in words_list:
            tf[words] += 1

        # Calculate tf-idf for each word
        tf_idf = defaultdict(int)
        for words in set(words_list):
            tf_idf[words] = tf[words] * idf[words]

        # Get unweighted tfidf for each file
        un_tfidf = defaultdict(int)
        for words in set(words_list):
            un_tfidf[words] = tf_idf[words] / norm(list(tf_idf.values()))
        
        # Store the vector for the file into the dictionary
        all_vectors[filenames] = un_tfidf

    # Get cosine similarity for each pairs of articles
    sim_dict = dict()
    for i in range(0, num_documents - 1):
        for j in range(i + 1, num_documents - 1):
            sim_dict[(articles_list[i], articles_list[j])] = cos_sim(all_vectors[articles_list[i]], all_vectors[articles_list[j]])
    sorted_score = dict(sorted(sim_dict.items(), key=lambda item: item[1], reverse = True))
    
    # Write article names and their cosine similarities into csv
    header = ['article1', 'article2', 'similarity']
    with open(task9_csv, 'w') as fp_csv:
        writer = csv.writer(fp_csv)
        writer.writerow(header)
        i = 1
        for filenames, scores in sorted_score.items():
            if i <= 10:
                writer.writerow([filenames[0], filenames[1], scores])
                i += 1
            else:
                break
    
    return            
