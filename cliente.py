import socket
def ejecutar_cliente():
    # creamos el socket del cliente
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # definimos el host y el puerto al que nos vamos a conectar
    host = 'localhost'
    puerto = 9876
    direccion_servidor = (host, puerto)

    # nos conectamos al servidor
    socket_cliente.connect(direccion_servidor)

    # recibimos los datos
    datos = socket_cliente.recv(100)

    # los datos estan en bytes, hay que transformar a string con 'decode()'
    print('El servidor dice: ' + datos.decode())

    # respondemos al servidor
    mensaje = 'Hola servidor!'
    socket_cliente.send(mensaje.encode())

    # mostramos el menssje enviado
    print('estamos respondiendo al servidor: ' + mensaje)

    # cerramos la conexion
    socket_cliente.close()

    # mostramos un mensaje final
    print('la conexion ha terminado')

if __name__ == '__main__':
    ejecutar_cliente()
