from flask import Flask
from flask_restful import Api, Resource, reqparse
import pickle
import numpy as np

APP = Flask(__name__)
API = Api(APP)

#We reload the logistic regression model, studied for the heroin use
heroin_reg = pickle.load(open('Heroin consumptionLogReg.sav','rb'))

class Predict(Resource):

    @staticmethod
    def post():
        #All the parameters except Heroin one
        parser = reqparse.RequestParser()
        parser.add_argument('ID')
        parser.add_argument('Age')
        parser.add_argument('Gender')
        parser.add_argument('Education level')
        parser.add_argument('Country number')
        parser.add_argument('Ethnicity number')
        parser.add_argument('Neuroticism')
        parser.add_argument('Extraversion')
        parser.add_argument('Openess to exp')
        parser.add_argument('Agreeableness')
        parser.add_argument('Conscientiousness')
        parser.add_argument('Impulsiveness')
        parser.add_argument('Sensation seeing')
        parser.add_argument('Amphet consumption')
        parser.add_argument('Alcohol consumption')
        parser.add_argument('Amyl consumption')
        parser.add_argument('Benzos consumption')
        parser.add_argument('Caffeine consumption')
        parser.add_argument('Cannabis consumption')
        parser.add_argument('Chocolate consumption')
        parser.add_argument('Coke consumption')
        parser.add_argument('Crack consumption')
        parser.add_argument('Ecstasy consumption')
        parser.add_argument('Ketamine consumption')
        parser.add_argument('Legal highs consumption')
        parser.add_argument('LSD consumption')
        parser.add_argument('Meth consumption')
        parser.add_argument('Mushrooms consumption')
        parser.add_argument('Nicotine consumption')
        parser.add_argument('VSA consumption')
        args = parser.parse_args()

        X_nb = np.fromiter(args.values(), dtype=float)  
        out = {'Is the person going to drink Alcohol?': heroin_reg.predict([X_nb])[0]}

        return out, 200


API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(debug=True, port='1080')