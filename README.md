## Project: Stack Overflow survey network analysis

### Authors
Romain Choukroun, Matthias Leroy, Alain Milliet, Hector Parmantier

### Question

What's the best developer job like ? (depending on your own definition
of "best")

### Dataset

We used the dataset provided by [StackOverflow on
Kaggle](https://www.kaggle.com/stackoverflow/so-survey-2017/data), you can download it and directly run the notebook. It contains about fifty thousand answers from a
sample of the active StackOverflow population about a lot of questions,
namely 154. This means that we have a tremendous insight into what
makes a programmer unique, but we also can answer a lot of
interesting questions.

### Project

#### Exploratory

Check the distributions of all useful features, outliers, quantiles.
Questions we could answer with the exploration:

-   What features are more correlated with satisfaction?
        Does salary equates to happiness/fulfilment in your job ?
        How much is Job Satisfaction linked to education ?
        Are "gif" people more satisfied with their job compared to "jif" people ?

-   What does the population that answered to this survey looks like ?
-   Can we find what are the most used programming languages in the StackOverflow population ?
    
#### Metric
Derive a metric to measure the distance inbetween users

#### Pre-processing

Data cleaning, categorize values, check out their distribution,
selecting columns, removing bad values if needed.

#### Graph Analysis

The graph will be built the following way:

-   Users will be the nodes

-   Correlations (with a threshold) in-between users used as edges

#### Recommender System

The idea of the recommender system is to be able to recommend users
to recruiters. To do so, we would simply check
which existing node is the closest to the artificial one that we create
for the chosen features a recruiter is looking for.

Important, to correctly see the graphs and the map of this notebook, click on this link : https://nbviewer.jupyter.org/github/agpmilli/network-tour-so/blob/master/StackOverflow.ipynb
