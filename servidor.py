import socket
def ejecutar_servidor():
    #creamos un socket para el servidor
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #definimos la direccion IP o el nombre del servidor, puede ser vacio (es una cadena)
    # (cuando es vacio funciona en cualquier interfaz de red)
    host = ''

    #definimos el puerto (es un numero) a abrir, debe ser un puerto que no este siendo usado
    #el numero debe ser mayor a 1024 y menor a 65536
    puerto = 9876

    # abrimos el puerto en la direccion indicada
    socket_servidor.bind((host, puerto))

    # le decimos al socket que escuche
    socket_servidor.listen()

    # mostramos un mensaje
    print('el servidor "' + host + '" esta esperando conexiones en el puerto: ' + str(puerto))

    # esperamos y aceptamos la conexion
    socket_cliente, direccion_cliente = socket_servidor.accept()

    # hasta aqui ya hay un cliente conectado, mostramos la direccion de quien se ha conectado
    print('se ha conectado el cliente en la direccion remota: ' + str(direccion_cliente))

    # enviamos un mensaje al cliente
    # la variable 'mensaje' es una cadena
    mensaje = 'Hola!'
    # convertimos la variable 'mensaje' a bytes, con el metodo 'encode()'
    socket_cliente.send(mensaje.encode())

    # recibimos los datos del cliente
    datos = socket_cliente.recv(1000)

    # mostramos lo que recibmos del cliente
    print('El cliente nos dice: ' + datos.decode())

    # cerramos la conexion del cliente
    socket_cliente.close()

    # cerramos la conexion del servidor
    socket_servidor.close()

    # mostramos un mensaje final
    print('programa finalizado!!!')

if __name__ == '__main__':
    ejecutar_servidor()