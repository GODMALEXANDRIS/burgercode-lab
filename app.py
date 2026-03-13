from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
....return "¡Bienvenido a BurgerCode! La mejor hamburguesa v1.0 🍔"  # <--- ESTOS 4 ESPACIOS SON CLAVE

if __name__ == '__main__':
....app.run(host='0.0.0.0', port=5000)  # <--- ESTOS 4 ESPACIOS TAMBIÉN
