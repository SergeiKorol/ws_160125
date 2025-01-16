import requests

def test_check_delete_task():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    new_id = response_body["id"]

    requests.delete(f'https://todo-app-sky.herokuapp.com/{new_id}')

    response = requests.get(f'https://todo-app-sky.herokuapp.com/{new_id}')

    assert response.status_code == 200

