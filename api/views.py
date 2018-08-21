
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

@app.route('/api/v1/question/<int:id>', methods=['GET'])
def getOneQuestionById(id):

    questionReturned = [question for question in allQuestions if question["id"] == id]
    
    answersReturned = [answer for answer in allAnswers if answer["question_id"] == id]

    temporaryId[0]['id'] = id

    return jsonify({'Answers' : answersReturned, 'Quetion' :questionReturned })

