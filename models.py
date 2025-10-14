import json
import os
USERS_FILE = os.path.join(os.path.dirname(__file__), '.', 'database', 'usuarios.json')

class Usuario:
    def __init__(self, matricula, senha):
        self.matricula = matricula
        self.senha = senha

    def to_dict(self):
        return {
            'matricula': self.matricula,
            'senha': self.senha
        }
    @staticmethod
    def load_all_users():
        print(os.path.exists(USERS_FILE))
        if not os.path.exists(USERS_FILE):
            return []

        with open(USERS_FILE, 'r') as f:
            try:
                users_data = json.load(f)
                print(users_data)
                return [Usuario(**u) for u in users_data]
            except json.JSONDecodeError:
                return []
    
    @staticmethod
    def save_all_users(users):
        with open(USERS_FILE, 'w') as f:
            json.dump([u.to_dict() for u in users], f, indent=4)
            
    @staticmethod
    def create_user(matricula, senha):
        new_user = Usuario(matricula, senha)
        print(new_user.to_dict())
        users = Usuario.load_all_users()
        users.append(new_user)
        Usuario.save_all_users(users)
        return new_user
    
    @staticmethod
    def procurar_por_matricula(matricula, senha):
        users = Usuario.load_all_users()
        print(users)
        for user in users:
            if user.matricula == matricula and user.senha == senha:
                return user
        return None