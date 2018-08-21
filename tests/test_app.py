import json
import pytest
from api.views import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    return test_client

# Helper functions 

def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))

# Test for GET endpoint:

def test_get_all_questions_is_successfully_rendered(client):
    response = client.get('/api/v1/questions')
    assert response.status_code == 200

def test_get_a_question_is_successfully_rendered_for_details_page_with_id(client):
    response = client.get('/api/v1/question/1')
    assert response.status_code == 200

# Test for POST endpoint. Checking resulting json data:

def test_post_question_is_json_formatted(client):
    response = post_json(client, '/api/v1/question', {
            "id" : 9,
            "votes" : 3,
            "answers" : 0,
            "views" : 0,
            "title" : "Question One",
            "content" : "This question seems to be useless",
            "author" : "Walter Nyeko",
            "ask_date" : "04-24-2018"})
    assert response.status_code == 400


def test_post_answer_is_json_formatted(client):
    response = post_json(client, '/api/v1/answers', {
            'id' : 1, 
            'question_id' : 2, 
            'content' : 'Yessss', 
            'author' : 'Walter Geek'})
    assert response.status_code == 400
    