document.addEventListener('DOMContentLoaded', fetchEmployees);

function fetchEmployees() {
    fetch('http://127.0.0.1:5000/employee/employees')
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector('#employeeTable tbody');
            tbody.innerHTML = '';
            data.forEach(employee => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${employee.id}</td>
                    <td>${employee.name}</td>
                    <td>${employee.email}</td>
                    <td>${employee.telefono}</td>
                    <td>
                        <button onclick="editEmployee(${employee.id})">Editar</button>
                        <button onclick="deleteEmployee(${employee.id})">Eliminar</button>
                    </td>
                `;
                tbody.appendChild(row);
            });
        });
}

function addEmployee() {
    const name = prompt("ingrese el nombre:");
    const email = prompt("ingrese el email");
    const telefono = prompt("ingrese el telefono");
    const id = Date.now();

    fetch('http://127.0.0.1:5000/employee/employees', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, telefono })
    })
    .then(response => response.json())
    .then(() => fetchEmployees());
}

function editEmployee(id) {
    const name = prompt("nuevo name:");
    const email = prompt("nuevo email:");
    const telefono = prompt("nuevo telefono:");

    fetch(`http://127.0.0.1:5000/employee/employees/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, telefono })
    })
    .then(response => response.json())
    .then(() => fetchEmployees());
}

function deleteEmployee(id) {
    fetch(`http://127.0.0.1:5000/employee/employees/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(() => fetchEmployees());
}

