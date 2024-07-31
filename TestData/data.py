import json


class URL:
    site_url = 'https://admin-demo.nopcommerce.com/login'
    customer_url = "https://admin-demo.nopcommerce.com/Admin/Customer/List"


class Creds:
    email = 'admin@yourstore.com'
    password = 'admin'


class DataJson:
    # Open and read the JSON file
    with open('C:/Users/Change Me/PycharmProjects/NOCOMMERCE_V4/TestData.json', 'r') as file:
        data = json.load(file)


class CustomerData:
    with open('C:/Users/Change Me/PycharmProjects/NOCOMMERCE_V4/TestDataCustomer.json', 'r') as file:
        data = json.load(file)

        print(data['email'])

















