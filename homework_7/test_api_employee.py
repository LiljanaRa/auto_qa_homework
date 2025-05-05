from homework_7.base_requests import EmployeeApi


base_url = 'http://5.101.50.27:8000'
api = EmployeeApi(base_url)

def test_create_new_employee():
    employee = api.create_new_employee(
         "Thomas",
         "Li",
         540,
         "thomasli@example.com",
         "+1234567891",
         "1998-03-25"
    )
    assert 'id' in employee

def test_get_employee():
    new_employee = api.create_new_employee(
        "Lucas",
        "Miller",
        540,
        "lucasmil@example.com",
        "+1235567891",
        "1999-10-13"
    )
    employee_id = new_employee['id']
    employee = api.get_employee(employee_id)
    assert employee['id'] == employee_id

def test_update_employee():
     updated_employee = api.update_employee(
            199,
            "Roy",
            "roysmith@example.com",
            False
     )
     assert updated_employee["email"] == "roysmith@example.com"


