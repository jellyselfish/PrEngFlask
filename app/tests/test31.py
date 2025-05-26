import requests

BASE_URL = "http://127.0.0.1:8080/api/jobs"

def test_get_all_jobs():
    print("Тест: Получение всех работ")
    response = requests.get(BASE_URL)
    print(f"Код ответа: {response.status_code}")
    if response.status_code == 200:
        print("Пример данных:", response.json()[:2])
    else:
        print("Ошибка:", response.text)

def test_get_job(job_id):
    print(f"Тест: Получение работы с id={job_id}")
    response = requests.get(f"{BASE_URL}/{job_id}")
    print(f"Код ответа: {response.status_code}")
    try:
        print("Ответ:", response.json())
    except:
        print("Не удалось распарсить JSON")

def test_create_job():
    print("Тест: Добавление новой работы")
    data = {
        "team_leader": 1,
        "job": "Исследование луны",
        "work_size": 40,
        "collaborators": "2,3",
        "is_finished": False
    }
    response = requests.post(BASE_URL, json=data)
    print(f"Код ответа: {response.status_code}")
    try:
        print("Ответ:", response.json())
    except:
        print("Не удалось распарсить JSON")

def test_update_job(job_id):
    print(f"Тест: Обновление работы с id={job_id}")
    data = {
        "work_size": 50,
        "is_finished": True
    }
    response = requests.put(f"{BASE_URL}/{job_id}", json=data)
    print(f"Код ответа: {response.status_code}")
    try:
        print("Ответ:", response.json())
    except:
        print("Не удалось распарсить JSON")

def test_delete_job(job_id):
    print(f"Тест: Удаление работы с id={job_id}")
    response = requests.delete(f"{BASE_URL}/{job_id}")
    print(f"Код ответа: {response.status_code}")
    try:
        print("Ответ:", response.json())
    except:
        print("Не удалось распарсить JSON")

if __name__ == "__main__":
    # 1. Получение всех работ
    test_get_all_jobs()

    # 2. Получение существующей работы
    test_get_job(1)

    # 3. Получение работы с несуществующим id
    test_get_job(999)

    # 4. Получение работы с неверным типом id (строка)
    print("Тест: Неверный тип id (строка)")
    response = requests.get(f"{BASE_URL}/abc")
    print(f"Код ответа: {response.status_code}")
    try:
        print("Ответ:", response.json())
    except:
        print("Не удалось распарсить JSON")

    # 5. Добавление новой работы
    test_create_job()

    # 6. Редактирование работы
    test_update_job(11)

    # 7. Удаление работы
    test_delete_job(11)