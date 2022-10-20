import socket

sock = socket.socket()
print("Запускаем сервер")
sock.bind(('', 9090))
print("Начинаем слушать порт")
sock.listen(0)
print("Подключаем клиентов")
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	print("Принимаем данные от клиента по 1КБ")
	data = conn.recv(1024)
	if not data:
		print("Остановка подключения")
		break
	msg += data.decode()
	print("Отправляем данные клиенту")
	conn.send(data)

print("Суммированное сообщение:")	
print(msg)
print("Останавливаем сервер")
conn.close()
