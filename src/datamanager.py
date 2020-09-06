import os.path
import pymongo
from pymongo import MongoClient
import pprint
from pymongo.errors import OperationFailure


class DataManager:

    def __init__(self,URI,db,collection):

        try:
            # conectar base de datos
            self.client= MongoClient(URI)
            # traer base de datos
            self.db = self.client[db]
            # traer coleccion que queremos
            self.collection= self.db[collection]
            
            self.client.server_info()

            self.status = "Ok. connected to: {}".format(self.client)

        except:
            self.status = "connection error"

        
        try:
            # usamos como index el nombre de la tienda
            self.collection.create_index([("nombre", pymongo.TEXT)], unique = True)
        except OperationFailure:
            pass
        

    def getStatus(self):
        return self.client    


    def getCollection(self):
        return self.collection

    def find_all(self):
        elements = []
        if self.collection.count_documents({}) == 0:
            return False
        # la funcion find no devueleve lista devuelve un puntero
        for element in self.collection.find():
            element.pop('_id', None)
            elements.append(element)
        return elements


    def find_shop(self,name):
        if self.isShop(name) == False:
            return False
        result=self.collection.find_one({'nombre':name})
        result.pop('_id', None)
        return result


    def save_one(self,shop):
        if self.isShop(shop['nombre']) == True:
            return False  
        # insertar un tienda en la colección
        self.collection.insert_one(shop)
        return True

    
    def update_one(self, shop):
        if self.isShop(shop['nombre']) == False:
            return False
        myquery = { "nombre" : shop['nombre'] }
        new = {"$set":shop}
        
        self.collection.update_one(myquery, new)
        return True

    
    def delete_one(self,name):
        if self.isShop(name) == False:
            return False
        myquery = { "nombre" : name }
        self.collection.delete_one(myquery)
        return True


    def isShop(self, name):
        if self.collection.count_documents({'nombre': name}) > 0:
            return True
        else:
            return False

    def isProduct(self, shop_name, product_name):
        if  self.collection.find({'productos.0.nombre_p':{'$eq':product_name}}).count() > 0:
            return True
        else:
            return False


    def insert_product(self, shop_name, product):

        if self.isShop(shop_name) == False:
            return False

        if self.isProduct(shop_name, product['nombre_p']) == True:
            return False

        myquery = { "nombre" : shop_name }
        new ={"$push":{"productos":{"$each": [product]}}}
        self.collection.update_one(myquery,new)

        return True

    def find_product(self, shop_name, product_name):

        if self.isShop(shop_name) == False:
            return 

        if self.isProduct(shop_name, product_name) == False:  
            return False

        result = self.collection.find_one({'nombre':shop_name, 'productos.nombre_p':{'$eq':product_name}})
        result.pop('_id', None)
        
        for ele in result['productos']:
            if ele['nombre_p'] == product_name:
                return ele

        return False

    
    def update_product(self, shop_name, product):

        if self.isShop(shop_name) == False:
            return False

        if self.isProduct(shop_name, product['nombre_p']) == False:
            return False

        myquery = { "nombre" : shop_name, 'productos.nombre_p':product['nombre_p'] }
        new ={"$set":{"productos.$":product}}
        self.collection.update_one(myquery,new)
        return True
        
    def delete_product(self, shop_name, product_name):

        if self.isShop(shop_name) == False:
            return False

        if self.isProduct(shop_name, product_name) == False:
            return False
        
        myquery = { "nombre" : shop_name}
        new ={"$pull": {"productos": {"nombre_p": product_name}}}
        self.collection.update_one(myquery,new)
        return True
    
    def isShopTrans(self, name):
        if self.collection.count_documents({'nombre_t': name}) > 0:
            return True
        else:
            return False

    def save_trans(self,trans): 
        # insertar un venta en la colección
        self.collection.insert_one(trans)
        return True

    def find_trans(self,nombre):
        if self.isShopTrans(nombre) == False:
            return False
        result=self.collection.find({'nombre_t':nombre})
        return result
