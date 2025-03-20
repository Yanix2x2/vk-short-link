# Обрезка ссылок с помощью VK

Скрипт принимает на вход ссылку. Программа либо сокращает длинную ссылку, либо показывает количество кликов у короткой ссылки. Например:
```bash
>>> main.py https://dvmn.org/modules/
Сокращенная ссылка:  https://vk.cc/aCA1ad
``` 
Или:
```bash
>>> main.py https://vk.cc/aCA1ad
Количество переходов:  106
```

## Окружение
Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3.13/library/venv.html) для изоляции проекта.

### Настройка виртуальное окружение
* Для Windows:
```bash
python -m venv C:\path_to_new_virtual_environment
venv\Scripts\activate
```

## Зависимости
Python3 должен быть уже установлен. Используйте `pip` или `pip3` для установки зависимостей:
```bash
pip install -r requirements.txt
```

## Переменные окружения
### Как получить
Получите [ключ доступа](https://dev.vk.com/ru/api/access-token/getting-started) для работы с VK API. 

Ключ необходимо добавить в `.env`, предварительно создав его в корне проекта:
```
VK_TOKEN='ваш_токен'
```

## Запуск
Запустите программу, передав ссылку как аргумент:
```bash
python main.py https://dvmn.org/modules/
```

## Примечание

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).