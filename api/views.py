
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


@app.route('/api/v1/question', methods=['POST', 'GET'])
def postQuestion():


    request_data  = request.get_json()
    if (valid_question(request_data)):

        dictionary_with_highest_question_id = max(allQuestions, key = lambda x:x['id'])

        highest_value_of_id = dictionary_with_highest_question_id['id']

        the_next_value_of_id = highest_value_of_id + 1

        question = {
                'id' : the_next_value_of_id,
                'views' : 0,
                'answers' : 0,
                'votes' : 0,
                'title': request_data['title'],
                'content': request_data['content'],
                'author': 'Walter Nyeko',
                'ask_date' : '04-08-2018'
                
            }
        allQuestions.append(question)
        response = Response("", 201, mimetype="application/json")
        response.headers['Location'] = "api/v1/question/" + str(request_data['title'])
        return response
    else:
        invalid_entry = {
            "error": "Invalid question object"
        }
        response = Response(json.dumps(invalid_entry), status=400, mimetype="appliation/json")
        return response

    return jsonify({'Questions' : allQuestions})
    
@app.route('/api/v1/answers', methods=['POST','GET'])
def postAnswer():


    request_data  = request.get_json()
    if (valid_answer(request_data)):

        dictionary_with_highest_answer_id = max(allAnswers, key = lambda x:x['id'])

        highest_value_of_id = dictionary_with_highest_answer_id['id']

        the_next_value_of_id = highest_value_of_id + 1

        id_for_clicked_question = temporaryId[0]['id']

        yourAnswer = {
            'id' : the_next_value_of_id, 
            'question_id' : id_for_clicked_question, 
            'content' : request_data['content'], 
            'author' : 'Walter Geek'
            }
        allAnswers.append(yourAnswer)

        question_whose_answer_was_just_given = [question for question in allQuestions if question["id"] == id_for_clicked_question]
        
        answersReturned = [answer for answer in allAnswers if answer["question_id"] == id_for_clicked_question]

        return {'The Question': question_whose_answer_was_just_given, 'Its Answers': answersReturned}, 200
        
    else:
        invalid_entry = {
            "error": "Invalid answer object"
        }
        response = Response(json.dumps(invalid_entry), status=400, mimetype="appliation/json")
        return response   
    
    
def valid_question(questionObject):
    
    if "title" in questionObject and "content" in questionObject:
        return True
    else:
        return False

def valid_answer(answerObject):
    
    if "content" in answerObject:
        return True
    else:
        return False




