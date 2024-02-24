import sender_stand_request
import data
import configuration

def get_track():
    sender_stand_request.order_create()
    response = sender_stand_request.order_create()
    track = response.json()["track"]

def positive_assert():
    sender_stand_request.order_create()
    response = sender_stand_request.order_create()
    track_number = response.json()["track"]
    sender_stand_request.get_order(track_number)
    response = sender_stand_request.get_order(track_number)
    assert response.status_code == 200

#Дехнич Константин 13-я когорта — Финальный проект. Инженер по тестированию плюс
def test_get_order_by_track_success():
    positive_assert()