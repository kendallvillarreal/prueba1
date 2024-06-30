from models.employee import Employee

class EmployeeService:
    def __init__(self):
        self.employees = []
        self.next_user_id = 1     

    def get_all_employees(self):
        return [employee.to_dict() for employee in self.employees]

    def add_employee(self, data):
        new_employee = Employee(str(self.next_user_id), data['name'], data['email'], data['telefono'])
        self.employees.append(new_employee)
        self.next_user_id += 1
        return new_employee.to_dict()

    def update_employee(self, id, data):
        for employee in self.employees:
            if employee.id == str(id):
                employee.name = data.get('name', employee.name)
                employee.email = data.get('email', employee.email)
                employee.telefono = data.get('telefono', employee.telefono)
                return employee.to_dict()
        return {'error': 'Employee not found'}

    def delete_employee(self, id):
        self.employees = [employee for employee in self.employees if employee.id != str(id)]
        return {'message': 'Employee deleted'}
