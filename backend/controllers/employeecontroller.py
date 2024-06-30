from flask import Blueprint, request, jsonify
from services.employeeservices import EmployeeService

employee_controller = Blueprint('employee_controller', __name__)
employee_service = EmployeeService()

@employee_controller.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employee_service.get_all_employees())

@employee_controller.route('/employees', methods=['POST'])
def add_employee():
    new_employee = request.get_json()
    
    data = request.json
    name = data.get('name')
    email = data.get('email')
    telefono = data.get('telefono')

    if not name or not email or not telefono:
        return jsonify({'error': 'Missing required fields'}), 400

    return jsonify(employee_service.add_employee(data))

@employee_controller.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    return jsonify(employee_service.update_employee(id, data))

@employee_controller.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    return jsonify(employee_service.delete_employee(id))
