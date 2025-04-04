import os
import sys
import subprocess
import pickle
import hashlib
import random
import string

# Variables globales inseguras
admin_password = "admin123"
api_key = "12345-ABCDE"
session_tokens = {}

# Simula base de datos en texto plano
user_db = "users.txt"

# Utilidad para generar contraseñas inseguras
def generate_weak_password(length=6):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Inyección de comandos
def run_command(cmd):
    os.system(cmd)

# SQL Injection simulada
def get_user_data(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print("Ejecutando query:", query)
    return "datos_de_usuario"

# Autenticación sin hash
def login(username, password):
    with open(user_db, "r") as f:
        for line in f:
            u, p = line.strip().split(":")
            if u == username and p == password:
                token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
                session_tokens[username] = token
                return True
    return False

# Almacenamiento de datos sensibles sin cifrar
def register_user(username, password):
    with open(user_db, "a") as f:
        f.write(f"{username}:{password}\n")

# Ejecución remota simulada
def insecure_exec(payload):
    eval(payload)

# Deserialización insegura
def insecure_deserialize(data):
    return pickle.loads(data)

# Hardcoded secrets
def get_api_key():
    return api_key

# Método con hardcoded path
def read_sensitive_file():
    with open("/etc/passwd", "r") as f:
        return f.read()

# Simulando un servidor web vulnerable
class FakeWebServer:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, handler):
        self.routes[path] = handler

    def handle_request(self, path, params):
        if path in self.routes:
            return self.routes[path](params)
        return "404 Not Found"

# Vulnerabilidad XSS
def render_profile(params):
    name = params.get("name", "Guest")
    return f"<html><body><h1>Bienvenido {name}</h1></body></html>"

# Path traversal
def read_user_file(filename):
    with open(f"user_files/{filename}", "r") as f:
        return f.read()

# Método vulnerable a race condition
def insecure_file_write(username, data):
    path = f"/tmp/{username}.txt"
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(data)

# Simulación de mal manejo de errores
def vulnerable_function():
    try:
        1 / 0
    except:
        pass

# Script con muchas malas prácticas
for i in range(100):
    def dummy_func():
        password = generate_weak_password()
        run_command(f"echo {password}")
        get_user_data("' OR '1'='1")
        login("admin", "admin123")
        register_user("user" + str(i), password)
        insecure_exec("print('ejecutando...')")
        insecure_deserialize(pickle.dumps({"key": "value"}))
        read_sensitive_file()
        render_profile({"name": "<script>alert('XSS')</script>"})
        read_user_file("../../etc/passwd")
        insecure_file_write("user" + str(i), "data")
        vulnerable_function()

    dummy_func()
