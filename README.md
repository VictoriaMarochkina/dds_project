# Django-приложение для управления движением денежных средств (ДДС)

---

## Инструкция по запуску проекта

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/VictoriaMarochkina/dds_project
cd dds_project
```
### 2. Создайте и активируйте виртуальное окружение
Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 3. Установите зависимости
```bash
pip install -r requirements.txt
```
### 4. Настройте переменные окружения
Создайте файл .env в корне проекта и добавьте туда ваш секретный ключ:
```
SECRET_KEY=ваш-секретный-ключ
```
Если у вас нет ключа, вы можете сгенерировать его командой:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Настройка базы данных
- Если вы используете уже загруженную базу (db.sqlite3 есть в проекте):
всё готово — переходите к запуску сервера.

- Если база отсутствует, выполните миграции для создания таблиц:

```bash
python manage.py migrate
```
База будет создана с нуля (без данных). Далее можно добавить записи вручную через интерфейс

### 6. Запустите веб-сервис
```bash
python manage.py runserver
```
Откройте в браузере:
```
http://127.0.0.1:8000/
```
## Интерфейс приложения

### Главная страница
Отображение всех записей с возможностью фильтрации.
![Главная страница](img/Главная%20страница.png)

### Главная страница с применением фильтра
После применения фильтров таблица отфильтрована по заданным параметрам.
![Фильтрация](img/Главная%20страница%20с%20применением%20фильтра.png)

### Создание или редактирование записи
Форма для добавления или изменения записи с динамической фильтрацией категорий и подкатегорий.
![Форма записи](img/Создание%20или%20редактирование%20записи.png)

### Страница управления списками
Добавление, редактирование и удаление справочников: статусы, типы, категории и подкатегории.
![Справочники](img/Страница%20управления%20списками.png)


