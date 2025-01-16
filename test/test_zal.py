import requests


def test_add_2_tasks():
    body_1 = {"title": "Zalia_1_generated", "completed": False}
    response_1 = requests.post("https://todo-app-sky.herokuapp.com/", json=body_1)
    id_1 = response_1.json()["id"]

    response_2 = requests.delete(f'https://todo-app-sky.herokuapp.com/{id_1}')

    body_2 = {"title": "Zalia_2_generated", "completed": False}
    response_3 = requests.post("https://todo-app-sky.herokuapp.com/", json=body_2)
    id_2 = response_3.json()["id"]

    assert id_2 != id_1
    assert id_2 == id_1 + 1