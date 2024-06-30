from flask import Flask
from flask_cors import CORS
from controllers.employeecontroller import employee_controller
app = Flask(__name__)
CORS(app)  # Configurar CORS para permitir todas las solicitudes

# Register Blueprints
app.register_blueprint(employee_controller, url_prefix='/employee')

if __name__ == '__main__':
    app.run(debug=True)
