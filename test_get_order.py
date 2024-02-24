import sender_stand_request
import data
import configuration

def test_positive_assert():
    sender_stand_request.order_create(data.order_body)
    response = sender_stand_request.get_order()
    assert response.status_code == 200

#Дехнич Константин 13-я когорта — Финальный проект. Инженер по тестированию плюс
