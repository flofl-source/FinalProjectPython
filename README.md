Work made by Flora Maier & Sarah Lascar, 4th year students of engineer school (ESILV, Paris).

# Subject

Link of the dataset : https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29

The given dataset shows the consumption of 1885 respondents on 19 different drugs, depending on social criterias like personality, age, gender, country or level of education.

The dataset has 33 variables that we can group :
Social variables : ID, Age, Gender, Education Level, Country number, Ethnicity number

Personality level of: Neuroticism, Extraversion, Openness to experience, Agreeableness, Conscientiousness, Impulsiveness, Sensation seeing

Consumption level of : Alcohol, Amphet, Amyl, Benzos, Caffein, Cannabis, Chocolate, Coke, Crack, Ecstasy, Heroin, Ketamine, Legal highs consumptions, LSD, Meth, Mushrooms, Nicotine, Semeron, VSA

# The goal

The aim of this project was to predict if a person already used a drug in his/her life, depending on the social, personality variables, and the drug the peson already tried.

# How ?

Our work is divided in 3 parts : the visualization, the modelization and the Flask API.

## Vizualisation

This part helped us to have a better image of our data, to analyse the links between several parameters regardind to the drug consumption and mainly to choose the best parameters to take in consideration for the predictions.
Conclusion : We consider all the paameters!

## Modelization

To predict if the person already used a drug or not, we apply several machine learning models and compiled their accuracy to find the best one. We use the following models :
- Logistic regression model 
- Decision tree model 
- random forest model 
- boosting model 
- K-Nearest Neighbor model
Conclusion : In average the best model is the Random forest with an accuracy of 0.862814!
The easiest drug to predict the Caffeine, and for the illegal one it's the Cannabis. 
For the Caffeine, we obtained the best accuray (0.987097) thank to the KNN model (we improved the yper parameters by a GridSearch function) and the RandomForest one.

## Flask API

As asked by our teachers, we create a Flask API, that can be runned by the app.py file. We added the heroin_example.py file that contains the values of the pramaters from a respondent. The goal of our API is to predict if this person already used heroin or not, by testing our 5 several models.
