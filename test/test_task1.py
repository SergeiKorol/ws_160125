import requests


def test_add():
    body = {"title": "New_task", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    body = {"completed": True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['completed'] == True

    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 200



