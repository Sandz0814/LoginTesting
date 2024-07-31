import json
import os


class URL:
    site_url = 'https://admin-demo.nopcommerce.com/login'
    customer_url = "https://admin-demo.nopcommerce.com/Admin/Customer/List"


class Creds:
    email = 'admin@yourstore.com'
    password = 'admin'


class DataJson:
    # Open and read the JSON file
    file_path = os.path.join(os.path.dirname(__file__), 'C:/Users/Change Me/PycharmProjects/NOCOMMERCE_V4/TestData.json')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Test data file not found: {file_path}")

    with open(file_path, 'r') as file:
        data = json.load(file)


class CustomerData:
    with open('C:/Users/Change Me/PycharmProjects/NOCOMMERCE_V4/TestDataCustomer.json', 'r') as file:
        data = json.load(file)

        print(data['email'])

















