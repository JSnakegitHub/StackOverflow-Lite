from flask import Flask, session, jsonify, request, json, Response
from models import Questions

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fhghgjhjhm'
allQuestions = Questions()

@app.route('/api/v1/questions')
def getAllQuestions():
   return jsonify({'Questions' : allQuestions})

@app.route('/api/v1/questions/<int:id>', methods=['GET'])
def getOneQuestionById(id):
    questionReturned = [question for question in allQuestions if question["id"] == id]
    return jsonify({'Question' :questionReturned })

@app.route('/api/v1/questions', methods=['POST', 'GET'])
def postQuestion():
    request_data  = request.get_json()
    if (valid_question(request_data)):
        question_id = len(allQuestions)+1
        question = {
                'id' : question_id,
                'title': request_data['title'],
                'content': request_data['content'],
                'answers' : []   
            }
        allQuestions.append(question)
    
        return "Question posted successfully"
    else:
        invalid_entry = {
            "error": "Invalid question object"
        }
        return invalid_entry + "Question Object is missing required attributes/properties"
    
@app.route('/api/v1/questions/<int:id>/answers', methods=['POST'])
def postAnswer(id):
    request_data  = request.get_json()
    if (valid_answer(request_data)):
        answer_id = 1
        yourAnswer = {
            'id' : answer_id, 
            'question_id' : id, 
            'content' : request_data['content'], 
            'author' : "Author"
            }
        question_whose_answer_was_just_given = [question for question in allQuestions if question["id"] == id]
        answers = question_whose_answer_was_just_given['answers']
        answers.append(yourAnswer)
        return jsonify({"Answer posted successfully": answers})
    else:
        invalid_entry = {
            "Error": "Invalid answer object, missing some parameters"
        }
        
        return invalid_entry   
    
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