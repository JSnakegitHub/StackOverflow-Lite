
from flask import Flask, session, jsonify, request, json, Response
from models import Questions, Answers, questionTempId

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fhghgjhjhm'

allQuestions = Questions()
allAnswers = Answers()
temporaryId = questionTempId()

@app.route('/api/v1/questions')
def getAllQuestions():
   return jsonify({'Questions' : allQuestions})






