from tkinter import messagebox
from Models.ConexionBD import ConexionDB

class Usuario():
    def __init__(self, nombreUsuario, password):
        self.nombreUsuario = nombreUsuario
        self.password = password
        self.rol = ""

    def iniciarSesion(self, nombreUsuario, password):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conn = miConexion.getConnection()
        cursor = conn.cursor()
        cursor.execute("select * from usuario")
        listaUsuarios = cursor.fetchall()
        for usuario in listaUsuarios:
            if(usuario[1] == nombreUsuario and usuario[2] == password):
                self.rol = usuario[3]
                if(self.rol == "admin"):
                    messagebox.showinfo("Información", "Acceso correcto Administrador!")
                    #Crear objeto Administrador y abrir menú Administrador
                else:
                    messagebox.showinfo("Información", "Acceso correcto Digitador!")
                miConexion.cerrarConexion()
                return
        messagebox.showwarning("Advertencia", "El nombre de usuario y/o contraseña no existen, verifique e intente nuevamente!")
