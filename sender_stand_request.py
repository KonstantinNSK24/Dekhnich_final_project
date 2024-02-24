import data
import requests
import configuration


def order_create(body): #Создание заказа
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        json=body,
                        headers=data.headers)

def get_order_on_track(track): #Получение заказа по трек номеру
   return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                       params={
                           't': track,
                       })









