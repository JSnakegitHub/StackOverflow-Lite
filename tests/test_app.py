import json
import pytest
from api.views import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    return test_client

# Test for GET endpoint:

# Testing if the URL for getting all questions is accessible
def test_get_all_questions_is_successfully_rendered(client):
    response = client.get('/api/v1/questions')
    assert response.status_code == 200

# Testing if the URL for getting one question is accessible
def test_get_a_question_is_successfully_rendered_for_details_page_with_id(client):
    response = client.get('/api/v1/questions/1')
    assert response.status_code == 200

# Test for POST endpoint. Checking resulting json data:

# Testing if the question being sent is JSON formatted
def test_post_question_is_json_formatted(client):
    response = client.post('/api/v1/questions')
    assert response.status_code == 500

# Testing if the answer being sent is JSON formatted
def test_post_answer_is_json_formatted(client):
    response = client.post('/api/v1/questions/1/answers')
    assert response.status_code == 500
    
