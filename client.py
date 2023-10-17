import socket

# Создаем клиентский сокет
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))  # IP и порт сервера

while True:
    message = client.recv(1024).decode()  # Получаем сообщение от сервера
    if not message:
        print("Сервер отключился. Завершение работы клиента.")
        break
    print(f"Сообщение от сервера: {message}")
