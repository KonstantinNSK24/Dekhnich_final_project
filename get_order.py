import sender_stand_request
import data
import configuration

def get_oder_body(): #Получаем тело запроса для создания заказа
    order_body = data.order_body.copy()
    return order_body
def get_track(): #Создаем заказ используя полученное тело запроса
    body = get_oder_body()
    response = sender_stand_request.order_create(body)
    track_number = response.json()["track"]
    return track_number #Возвращаем трекномер заказа

def get_order(track_number): #Получаем информацию о заказе используя трекномер
    response = sender_stand_request.get_order_on_track(track_number)
    status_code = response.status_code
    return status_code #Возвращаем статус-код ответа сервера

def get_order_status_code():
    track = get_track()
    statuscode = get_order(track)
    assert statuscode == 200

def test_get_order_by_track_success(): #Проверка что стаус код равен 200
    get_order_status_code()

#Дехнич Констанин 13-ая когорта - Финальный проект. Инженер по тестированию плюс