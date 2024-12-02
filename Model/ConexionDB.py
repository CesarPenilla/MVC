import mariadb as sql
from tkinter import messagebox

class ConexionDB():
    def __init__(self):
        self.__host = "localhost" # Cambia si el servidor está en un host remoto
        self.__user = "root"
        self.__password = ""
        self.__port = 3307
        self.__database = "mvc"
        self.__conection = None

    def crearConexion(self):
        try:
            self.__conection = sql.connect(
                host = self.__host,
                user = self.__user,
                password = self.__password,
                port = self.__port,
                database = self.__database
            )
        except sql.OperationalError as e:
            messagebox.showwarning("Advertencia", "Error de conexión al Servidor de Bases de Datos\nVerifique su conexión a internet o contacte al administrador del Sistema...")

    def cerrarConexion(self):
        if self.__conection:
            self.__conection.close()
            self.__conection = None

    # Poner aqui getter´s y setter´s
    def getConection(self):
        return self.__conection