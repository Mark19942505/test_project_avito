Ответы на 1 задание лежат в файле Bugs.md


Инструкция по запуску тестов
Установка
Убедитесь, что у вас установлен Python 3.12
Установите необходимые библиотеки:
bash

pip install pytest requests

Запуск тестов
Сохраните тесты в файл test_ads.py

Запустите тесты в консоли pycharm с помощью команды:

pytest test_ads.py

Структура проекта
Code

/project
│
├── test_ads.py
├── TESTCASES.md
├── README.md
└── BUGS.md

Более развёрнутая инструкция(для чайников xD)

Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале

git clone https://github.com/Mark19942505/test_project_avito.git
Или скачайте zip архив по ссылке и распакуйте его

Убедитесь, что на Вашем компьютере установлен Python. В командной строке/терминале выполните команду

python -v
Если он не установлен, то установите с официального сайта Python, выбрав подходящую версию для Вашей операционной системы, и пройдите шаг сначала. В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH". Иначе, у Вас не будет корректно отображаться версия Python

Через командную строку/терминал перейдите в корневую директорию проекта, выполнив команду

cd /здесь укажите путь до директории с проектом
Установите необходимые зависимости, введя в терминал

pip install pytest requests

если она не выполняется, то попробуйте

pip3 install -r pytest requests

Наконец, запустите тесты, выполнив команду

pytest test_ads.py


PS. По условиям все тесты должны проходить, у меня 1 фейлит так как это баг