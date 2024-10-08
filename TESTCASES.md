Тест-кейсы для API микросервиса

Тест-кейс 1: Создание объявления
Предусловия -
Шаги:
Метод: POST
URL: https://qa-internship.avito.com/api/1/item
Тело запроса:
json

{
  "name": "Кирпич",
  "price": 10000,
  "sellerId": 3452,
  "statistics": {
    "contacts": 32,
    "like": 35,
    "viewCount": 14
  }
}
Ожидаемый результат:
Статус 201 (Created)
Возвращается объект объявления с уникальным идентификатором.
Фактический результат:
Совпадает с ожидаемым
Коментарии: В ответе содержится только уникальный индетификатор без значений полей, это баг или фича?)

Тест-кейс 2: Получение объявления по идентификатору
Предусловия -
Шаги:
Метод: GET
URL: https://qa-internship.avito.com/api/1/item/{id}
Параметры: {id} - идентификатор объявления, полученный из предыдущего теста.
Ожидаемый результат:
Статус 200 (OK)
Возвращается объект объявления с корректными данными.
Проверка, что поля name, price, sellerId соответствуют ожидаемым значениям.
Фактический результат:
Совпадает с ожидаемым
Коментарии 

Тест-кейс 3: Получение всех объявлений по идентификатору продавца
Предусловия -
Шаги:
Метод: GET
URL: https://qa-internship.avito.com/api/1/{sellerID}/item
Параметры: {sellerID} - идентификатор продавца, использованный при создании объявления.
Ожидаемый результат:
Статус 200 (OK)
Возвращается массив объектов объявлений, связанных с указанным sellerID.
Проверка, что массив не пустой и содержит объекты с корректными полями.
Фактический результат:
Совпадает с ожидаемым
Коментарии 

Тест-кейс 4: Негативный тест на создание объявления с отсутствующими обязательными полями
Предусловия -
Шаги:
Метод: POST
URL: https://qa-internship.avito.com/api/1/item
Тело запроса:
json

{
  "price": 10000,
  "sellerId": 3452
}
Ожидаемый результат: Статус 400 (Bad Request).
Фактический результат:
Статус ответа [500]
Коментарии: багрепорт #2

Тест-кейс 5: Негативный тест на получение объявления по несуществующему ID
Предусловия -
Шаги:
Метод: GET
URL: https://qa-internship.avito.com/api/1/item/{non_existent_id}
Ожидаемый результат: Статус 404 (Not Found).
Фактический результат:
Совпадает с ожидаемым
Коментарии 