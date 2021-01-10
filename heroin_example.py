import requests


url = 'http://127.0.0.1:1080/predict' 
#One of the respondent from our test set, in order to predict the Heroin use  
body = {
        'Gender':0.48246
        'Education level':1.16365
        'Country number':0.96082
        'Ethnicity number':-0.31685
        'Neuroticism':-0.14882
        'Extraversion':0.80615
        'Openess to exp':-0.01928
        'Agreeableness':0.95042
        'Conscientiousness':0.58489
        'Impulsiveness':-1.37983
        'Sensation seeing':-1.18084
        'Alcohol consumption':4
        'Amphet consumption':0
        'Amyl consumption':0
        'Benzos consumption':3
        'Caffeine consumption':5
        'Cannabis consumption':2
        'Chocolate consumption':4
        'Coke consumption':2
        'Crack consumption':0
        'Ecstasy consumption':0
        'Ketamine consumption':2
        'Legal highs consumption':1
        'LSD consumption':0
        'Meth consumption':0
        'Mushrooms consumption':2
        'Nicotine consumption':2
        'VSA consumption':0
}
response = requests.post(url, data=body)
print(response.json())