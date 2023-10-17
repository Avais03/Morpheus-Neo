import socket
import sys
import threading

# Функция для отправки сообщений клиентам
def send_message(client_socket, message):
    try:
        client_socket.send(message.encode())
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {str(e)}")

# Функция для обслуживания каждого клиента
def handle_client(client_socket):
    try:
        while True:
            message = input("Введите сообщение для клиента: ")
            if message == '/quit':
                # Если сервер отправил '/quit', отключаем всех клиентов и завершаем работу сервера
                print("Отключение всех клиентов...")
                for client in clients:
                    client.close()
                server.close()
                print("Сервер завершил работу.")
                flag = True
                break
            send_message(client_socket, message)
    except Exception as e:
        print(f"Ошибка при отправке сообщения клиенту: {str(e)}")

# Создаем серверный сокет
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(5)
print("Сервер запущен. Ожидание подключений...")

flag = False
clients = []  # Список для хранения клиентских сокетов

while True:
    client_socket, addr = server.accept()
    print(f"Принято подключение от {addr}")

    clients.append(client_socket)  # Добавляем клиентский сокет в список

    # Запускаем поток для обслуживания клиента
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
