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
    file_path = os.path.join(os.path.dirname(__file__), '/TestData/TestData.json')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Test data file not found: {file_path}")

    with open(file_path, 'r') as file:
        data = json.load(file)


class CustomerData:
    with open('/TestData/TestDataCustomer.json', 'r') as file:
        data = json.load(file)

        print(data['email'])

















