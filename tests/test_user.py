import requests
import allure

BASE_URL = "https://reqres.in/api"


@allure.feature('User')
@allure.story('Получение информации о существующем пользователе')
@allure.severity(allure.severity_level.NORMAL)
def test_get_existing_user():
    user_id = 2
    expected_email = "janet.weaver@reqres.in"
    expected_first_name = "Janet"
    expected_last_name = "Weaver"
    expected_avatar_url = "https://reqres.in/img/faces/2-image.jpg"

    with allure.step('Отправить GET-запрос http://api/users/{id}'):
        response = requests.get(f"{BASE_URL}/users/{user_id}")

    with allure.step('Проверить что статус ответа 200 OK'):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    with allure.step('Проверить, что в ответе содержится информация о пользователе'):
        response_data = response.json()
        user_data = response_data.get("data", {})

        assert user_data["id"] == user_id, f"Expected id {user_id}, but got {user_data['id']}"
        assert user_data["email"] == expected_email, f"Expected email {expected_email}, but got {user_data['email']}"
        assert user_data[
                   "first_name"] == expected_first_name, f"Expected first name {expected_first_name}, but got {user_data['first_name']}"
        assert user_data[
                   "last_name"] == expected_last_name, f"Expected last name {expected_last_name}, but got {user_data['last_name']}"
        assert user_data[
                   "avatar"] == expected_avatar_url, f"Expected avatar URL {expected_avatar_url}, but got {user_data['avatar']}"
