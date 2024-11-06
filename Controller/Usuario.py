from Model.ConexionDB import ConexionDB
import tkinter as tk
from tkinter import messagebox

from View.ConsultarUsuarios import ConsultarUsuarios

class Usuario():
    def __init__(self):
        self.cedula = None
        self.nombre = None
        self.rol = None

    # Poiner aqui getter´s y setter´s

    def iniciarSesion(self, nombreUsuario, password, loggin):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("Select * from usuario")
        listaUsuarios = cursor.fetchall()
        for usuario in listaUsuarios:
            if(usuario[2] == nombreUsuario and usuario[1] == password):
                self.cedula = usuario[1]
                self.nombre = usuario[2]
                self.rol = usuario[3]
                print(usuario[3])
                if(usuario[3] == "Admin"):
                    messagebox.showinfo("Información", "Acceso Correcto! Administrador")
                    #Crear el objeto Mesero
                    miMenu = ConsultarUsuarios(loggin, self)
                else:
                    messagebox.showinfo("Información", "Acceso Correcto! Usuario")
                miConexion.cerrarConexion()
                return
        messagebox.showwarning("Advertencia", "El nombre de usuario y/o contraseña no existen, verifique e intente nuevamente!")

    def consultarTabla(self):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("Select * from usuario")
        listaUsuarios = cursor.fetchall()
        return listaUsuarios
    
    def crearUsuario(self, nombreUsuario, cedulaUsuario, rolUsuario):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("INSERT INTO usuario (cedula, nombre, rol) VALUES (?, ?, ?)", (cedulaUsuario, nombreUsuario, rolUsuario))
        miConexion.cerrarConexion()

    def eliminarUsuario(self, cedulaUsuario):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("DELETE from usuario WHERE cedula ="+cedulaUsuario)
        miConexion.cerrarConexion()

    def modificarUsuario(self, nombreUsuario, cedulaUsuario, rolUsuario):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("UPDATE usuario SET nombre=?, rol=? WHERE cedula=?", (nombreUsuario, rolUsuario, cedulaUsuario))
        miConexion.cerrarConexion()

    def buscarUsuario(self, cedulaUsuario):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM usuario WHERE cedula="+cedulaUsuario)
        listaUsuarios = cursor.fetchall()
        miConexion.cerrarConexion()
        if(len(listaUsuarios)) > 0:
            usuario = listaUsuarios[0]
            return usuario
        else:
            return None