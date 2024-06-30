class Employee:
    def __init__(self, id, name, email, telefono):
        self.id = id
        self.name = name
        self.email = email
        self.telefono = telefono

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'telefono': self.telefono
        }
