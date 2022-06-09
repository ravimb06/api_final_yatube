### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ravimb06/api_final_yatube.git
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Использованные технологии:
- Python 3
- Django
- Django REST framework

# Автор:
Али Богатырев. <https://github.com/ravimb06>
