from producto import Producto

class Tienda(object):

	__puntuacion=0
	__ids=0

	# Constructor de clase
	def __init__(self, id, nombre, descripcion, direccion, infoContacto, val, trans):

		self.id=id
		self.nombre=nombre
		self.descripcion=descripcion
		self.direccion=direccion
		self.infoContacto=infoContacto
		self.val=val
		self.trans=trans
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
		self.trans=trans

	def getTrans(self):
		return self.trans
	
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

	# Ver cuantos productos tiene la tienda
	def __len__(self):
		return len(self.productos)
	# Eliminar producto por id
	def delProducto(self, id_producto):
		cont=0
		for p in self.getProductos():
			if p.getId() == id_producto:
				self.productos.pop(cont)
				return True
			cont+=1
		return False
	
	# Implementar modificar producto y puntuacion tienda
