# -*- coding: utf-8 -*-
from producto import Producto

class Tienda(object):

	__puntuacion=0
	__ids=0
	__val=0 # Valoración de la tienda
	__trans=0 # Transacciones de la tienda

	# Constructor de clase
	def __init__(self, id, nombre, descripcion=None, direccion=None, infoContacto=None,):

		self.id=id
		self.nombre=nombre
		self.descripcion=descripcion
		self.direccion=direccion
		self.infoContacto=infoContacto
		self.__val=0
		self.__trans=0
		self.productos=[]

	def setId(self,id):
		self.id=id

	def getId(self):
		return self.id

	def setNombre(self,nombre):
		self.nombre=nombre

	def getNombre(self):
		return self.nombre

	def setDescripcion(self,descripcion):
		self.descripcion=descripcion

	def getDescripcion(self):
		return self.descripcion

	def setDireccion(self,direccion):
		self.direccion=direccion

	def getDireccion(self):
		return self.direccion

	def setInfoContacto(self,infoContacto1):
		self.infoContacto=infoContacto1

	def getInfoContacto(self):
		return self.infoContacto
	
	def setTrans(self,trans):
		self.__trans=trans

	def getTrans(self):
		return self.__trans

	def getVal(self):
		return self.__val
	
	def setVal(self, val):
		self.__val=val
	
	def getProductos(self):
		return self.productos

	def addProducto(self, producto):
		producto.setId(self.__ids)
		for p in self.getProductos():
			if p.getId() == producto.getId():
				return False
		
		self.productos.append(producto)
		self.__ids+=1
		return True

	def getProducto_byId(self, id_producto):
		cont = 0
		for p in self.productos:
			if p.getId() == id_producto:
				return self.productos[cont]
			cont+=1
		return False

	# Ver cuantos productos tiene la tienda
	def __len__(self):
		return len(self.productos)
	# Eliminar producto por id
	def delProducto_byId(self, id_producto):
		cont=0
		for p in self.getProductos():
			if p.getId() == id_producto:
				self.productos.pop(cont)
				return True
			cont+=1
		return False
	
	# Implementar modificar producto y puntuacion tienda
