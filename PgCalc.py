from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time
import cv2
import pytesseract
import pyautogui
import numpy as np
import socketio  # Usado para o cliente SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # Chave secreta para sessão
sio_server = SocketIO(app, cors_allowed_origins='*')  # Habilita CORS para todas as origens

@app.route('/')
def index():
    return render_template('index.html')  # Usar render_template

@sio_server.on('receive_message')
def handle_message(data):
    print("Mensagem recebida:", data)

@sio_server.on('connect')
def handle_connect():
    print("Cliente conectado")

@sio_server.on('disconnect')
def handle_disconnect():
    print("Cliente desconectado")

def start_server():
    sio_server.run(app, host='127.0.0.1', port=3000, allow_unsafe_werkzeug=True)

def start_client():
    time.sleep(5)  # Aumente o tempo de espera se necessário
    client = socketio.Client()
    try:
        client.connect("http://127.0.0.1:3000")
    except socketio.exceptions.ConnectionError as e:
        print("Erro ao conectar ao servidor:", e)
        return

    while True:
        try:
            screenshot = pyautogui.screenshot(region=(0, 25, 158, 380))
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
            resultado = pytesseract.image_to_string(frame)
            print(resultado)
            client.emit('receive_message', {'texto': resultado})
            time.sleep(1)
        except Exception as e:
            print("Erro:", e)
            time.sleep(1)

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    time.sleep(2)  # Dê um tempo para o servidor iniciar antes de iniciar o cliente
    start_client()
