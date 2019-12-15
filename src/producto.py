# -*- coding: utf-8 -*-
class Producto:
    # Constructor de clase
    __id=0
    def __init__(self, nombre, descripcion=None, precio=0, isOnline=False):
        self.nombre=nombre
        self.descripcion=descripcion
        self.precio=precio
        self.isOnline=isOnline


    def setId(self, id):
        self.__id=id

    def getId(self):
        return self.__id

    def setNombre(self, nombre):
	    self.nombre=nombre

    def getNombre(self):
	    return self.nombre
    
    def setDescripcion(self, descripcion):
        self.descripcion=descripcion

    def getDescripcion(self):
        return self.descripcion
    
    def setPrecio(self, precio):
        self.precio=precio
    
    def getPrecio(self):
        return self.precio

    def setIsOnline(self, isOnline):
        self.isOnline=isOnline
    
    def getIsOnline(self):
        return self.isOnline
