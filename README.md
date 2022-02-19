# comp20008-2021sm2a1

## Project: Assignment 1
Student ID: 1255069
Name: Junfei Zhang
Class: COMP20008
Date: September 9, 2021

This project is about extracting and analysing information from the match results and articles news relating to soccor matches in the English Premier League. There are 9 programming tasks and 1 report in this assignment. Task1 - Task9 are included on github, and the final report is submitted through canvas. 


## Description
The file assignment1.py contains all the solutions of Task 1 to Task 9; main.py is used to test the code.
In assignment1.py, task 1 loads the file; task 2 creates a csv 'task2.csv' that shows the goals scored by and against each team; task 3 produces a csv file containing article's name and the total goals of the largest match score identified in the article; task 4 produces a boxplot showing distribution of values for total_goals of each articles, save in 'task4.png'; task 5 produces a csv 'task5.csv' containing club name and number of mentions for each club, and produce a bar chart showing this information, save the bar char as 'task5.png'; task 6 produces a heat map 'task6.png' that shows the similarity scores of each pair of clubs; task 7 produces a scatterplot comparing the number of articles mentioning each team with the total number of goals scored by each team, save the plot as 'task7.png'; task 8 takes an argument 'filepath' that indicates the location of an article, preprocess the article, return a processed string of the article; and task 9 produce a csv file 'task9.csv' containing the filenames of the 10 pairs of articles with the highest similarities and their similarity score.

The function cos_sim is used in task 9; it takes two dictionaries (words as key and the unweighed tfidf as value) as inputs, calculate and return the cosine similarity.


## Dependencies
The program needs to download the following libraries:

collections
csv
json
matplotlib
nltk
nltk.corpus
nltk.tokenize
numpy
numpy.linalg
os
pandas
re
seaborn
string

## Executing Program
Use terminal to type 'python main.py all' to execute assignment1.py

## Acknowledgements
Inspirations of this program are from:
COMP20008 Lecture Notes and Workshop Materials
stackoverflow.com
towardsdatascience.com
scikit.org
pythontutorial.net


