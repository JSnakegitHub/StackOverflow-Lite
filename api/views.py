from flask import Flask, session, jsonify, request, json, Response
from api.models import Questions, Answers

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my-secret-keys-are-here'
allQuestions = Questions()
allAnswers = Answers()

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
    if not any(eachtitle['title'] == request_data['title'] for eachtitle in allQuestions):
        if request_data['title'].strip() == "":
            return "Please fill the title"
        else:
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
        return "Question already exists"
        
@app.route('/api/v1/questions/<int:id>/answers', methods=['POST'])
def postAnswer(id):
    request_data  = request.get_json()
    answer_id = len(allAnswers)+1
    yourAnswer = {
        'id' : answer_id, 
        'question_id' : id, 
        'content' : request_data['content'], 
        'author' : "Author's Name"
        }
    allAnswers.append(yourAnswer)
    questionReturned = [question for question in allQuestions if question["id"] == id]
    questionReturned[0]['answers'].append(yourAnswer)
    return jsonify({"Answer posted successfully": questionReturned})
