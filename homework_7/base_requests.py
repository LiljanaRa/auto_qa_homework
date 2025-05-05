import requests


class EmployeeApi:
    base_url = 'http://5.101.50.27:8000'

    def __init__(self, url):
        self.url = url

    def get_token(self):
        creds = {
            "username": "harrypotter",
            "password": "expelliarmus"
        }
        responce = requests.post(self.url + '/auth/login', json=creds)
        assert responce.status_code == 200
        return responce.json()['user_token']

    def create_new_employee(self, first_name, last_name, company_id, email, phone, birthdate, is_active=True):
        new_employee = {
            "first_name": first_name,
             "last_name": last_name,
             "company_id": company_id,
             "email": email,
             "phone": phone,
             "birthdate": birthdate,
             "is_active": is_active
        }
        responce = requests.post(self.url + '/employee/create', json=new_employee)
        assert responce.status_code == 200
        return responce.json()

    def get_employee(self, employee_id):
        responce = requests.get(f"{self.url}/employee/info/{employee_id}")
        assert responce.status_code == 200
        return responce.json()

    def update_employee(self, employee_id, first_name, email, is_active):
        client_token = self.get_token()
        url_with_token = f"{self.url}/employee/change/{employee_id}?client_token={client_token}"
        update_data = {
            "first_name": first_name,
            "email": email,
            "is_active": is_active
        }
        responce = requests.patch(url_with_token, json=update_data)
        assert responce.status_code == 200
        return responce.json()








