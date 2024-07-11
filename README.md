# Тестовое задание
## Установка зависимостей
```shell
pip install -r requirements.txt
```
## 1. Задача по API покрытию:
```shell
pytest
allure serve ./allure-results 
```

## 2. Задача по UI покрытию:
```shell
python tests\test_currency_conversion.py
```