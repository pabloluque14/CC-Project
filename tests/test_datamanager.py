# -*- coding: utf-8 -*-
import sys
sys.path.append('src')
import unittest
from datamanager import DataManager

class Test(unittest.TestCase):

    def test_constructor(self):
        DM = DataManager('localhost:28900', 'test', 'test_shops')
        self.assertNotEqual(DM.getStatus(),"connection error")


    def test_metodos(self):
        DM = DataManager('localhost:28900', 'test', 'test_shops')

        shop = {
            "nombre": "Cascabeles",
            "descripcion": "Tienda de musica", 
            "direccion": "avd Barcelona", 
            "info":"111111111"
         }

        shop2 = {
            "nombre": "Tecmies", 
            "descripcion": "Tienda de moviles",
            "direccion": "CC Arcangel", 
            "info":"angeljimez"
        }

        shop3 = {
            "nombre": "Arteaga", 
            "descripcion": "Tienda de deportes", 
            "direccion": "avd Barcelona", 
            "info":""
            }

        #shops =[shop, shop2, shop3]

        self.assertEqual(DM.save_one(shop),True)
        self.assertEqual(DM.save_one(shop2),True)
        self.assertEqual(DM.save_one(shop3),True)   
        #self.assertEqual(DM.find_all(),shops)    
        shop4 = DM.find_shop(shop['nombre'])
        self.assertEqual(shop4['nombre'], shop['nombre'])
        self.assertEqual(len(DM.find_all()),3) # poner los documentos de la bd
        self.assertEqual(DM.save_one(shop),False)
        self.assertEqual(len(DM.find_all()),3)

        shop = {
            "nombre": "Cascabeles",
            "descripcion":"Tienda de musica y arte",
            "direccion":"avd Barcelona",
            "info":"111111111"
        }

        self.assertEqual(DM.update_one(shop),True)
        shop4 = DM.find_shop(shop['nombre'])
        self.assertEqual(shop4, shop)
        self.assertEqual(DM.isShop(shop['nombre']), True)
        self.assertEqual(DM.delete_one(shop['nombre']),True)
        self.assertEqual(DM.delete_one(shop2['nombre']),True)
        self.assertEqual(DM.delete_one(shop3['nombre']),True)
        self.assertEqual(DM.find_all(), False)

        DM.getCollection().drop()


    def test_integracion(self):
        DM = DataManager('localhost:28900', 'test', 'test_shops_integration')

        shop = {
            "nombre": "App Store",
            "descripcion": "Tienda de electronica", 
            "direccion": "avd Barcelona", 
            "info":"applesupport",
            "productos":[]
         }

        product = {       
            "nombre_p": "Iphone 6",
            "descripcion_p": "Iphone 6 64GB",
            "precio": 700,
            "cantidad": 5,
            "online": ""
        }

        self.assertEqual(DM.save_one(shop),True)
        self.assertEqual(DM.insert_product(shop['nombre'],product),True)
        self.assertEqual(DM.find_product(shop['nombre'],product['nombre_p']),product)
        product = {       
            "nombre_p": "Iphone 6",
            "descripcion_p": "Iphone 6 64GB Plata"
        }
        self.assertEqual(DM.update_product(shop['nombre'],product),True)
        self.assertEqual(DM.delete_product(shop['nombre'],product['nombre_p']),True)

        DM.getCollection().drop()
        
if __name__ == '__main__':
    unittest.main()