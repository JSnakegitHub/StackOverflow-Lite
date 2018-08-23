# class Questions:
#     def __init__(self, question_id, content, title):
#        self.question_id = question_id
#        self.content = content
#        self.title = title
#        self.answers = []

#     def get_json(self):
#         questions_json = {
#             "question_id" : self.question_id,
#             "content" : self.content,
#             "title" : self.title
#             "answers": self.answers
#         }

#         return questions_json

def Questions():

    questions = [
        
    ]

    return questions

def Answers():

    answers = [
        {
            # 'id' : 1, 
            'question_id' : 1, 
            'content' : "Answer One", 
            'author' : "Walter"
            }
    ]
    return answers

def questionTempId():

    tempID =[

        {
           "id" : 0
        }
    ] 

    return tempID
