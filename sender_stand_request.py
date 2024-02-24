import data
import requests
import configuration
def order_create(body):
    data_headers = data.headers.copy()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        json=data.order_body,
                        headers=data_headers)
response = order_create(data.order_body)
track_number = response.json()["track"]
print(track_number)
def get_order():
   return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                       params={
                           't': track_number,
                       })
response = get_order()
