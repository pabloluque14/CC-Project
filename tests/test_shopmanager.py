import sys
import os
sys.path.append('src')
import unittest
import shop_manager
import json





class TestEventsRest(unittest.TestCase):

    def setUp(self):
        self.client = shop_manager.app.test_client()
        self.api = "http://"+os.environ['SM_URI']

    
    def test_unitario(self):
        api = self.api+"/shops"
        shop = {
            "nombre": "Cascabeles",
            "descripcion": "Tienda de musica", 
            "direccion": "avd Barcelona", 
            "info":"111111111"
         }
        headers = {'content-type': 'application/json'}
        
        # PUT SHOP
        # Caso 1: Todo ok
        response = self.client.put(api, data = json.dumps(shop), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: No se puede insertar la misma tienda
        response = self.client.put(api, data = json.dumps(shop), headers = headers)
        self.assertEqual(404, response.status_code)

        # GET SHOPS
        # Caso 1: Todo ok
        response = self.client.get(api)
        self.assertEqual(200, response.status_code)
        # Caso 2: GET de una tienda
        api2=api+"/Cascabeles"
        response = self.client.get(api2)
        self.assertEqual(200, response.status_code)
        # Caso 3: La tienda debe existir
        api2=api+"/rrrrrr"
        response = self.client.get(api2)
        self.assertEqual(404, response.status_code)

        # POST
        # Caso 1: Todo ok
        shop = {
            "nombre": "Cascabeles",
            "info":"cascabeles@shop.com"
         }
        response = self.client.post(api, data = json.dumps(shop), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: La tienda debe existir
        shop = {
            "nombre": "rrrrr",
            "info":"cascabeles@shop.com"
         }
        response = self.client.post(api, data = json.dumps(shop), headers = headers)
        self.assertEqual(404, response.status_code)
         # Caso 3: Hay que pasarle el nombre de la tienda
        shop = {
            "info":"cascabeles@shop.com"
         }
        headers = {'content-type': 'application/json'}
        response = self.client.post(api, data = json.dumps(shop), headers = headers)
        self.assertEqual(400, response.status_code)

        # DELETE
        # Caso 1: Todo ok
        shop = {
            "nombre": "Cascabeles",
         }
        response = self.client.delete(api, data = json.dumps(shop), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: La tienda debe existir
        shop = {
            "nombre": "rrrrrr",
         }
        response = self.client.delete(api, data = json.dumps(shop), headers = headers)
        self.assertEqual(404, response.status_code)

    def test_integracion(self):
        api = self.api+"/shops"
        shop = {
            "nombre": "Apple Store",
            "descripcion": "Tienda de musica", 
            "direccion": "avd Barcelona", 
            "info":"111111111"
         }
        product = {       
            "nombre_p": "Iphone 6",
            "descripcion_p": "Iphone 6 64GB",
            "precio": 700,
            "cantidad": 5,
            "online": ""
        }
        headers = {'content-type': 'application/json'}
        
        # PUT SHOP
        # Caso 1: Todo ok
        response = self.client.put(api, data = json.dumps(shop), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: No se puede insertar la misma tienda
        response = self.client.put(api, data = json.dumps(shop), headers = headers)
        self.assertEqual(404, response.status_code)

        # PUT PRODUCT
        # Caso 1: Todo ok
        api2=api+"/Apple Store"
        response = self.client.put(api2, data = json.dumps(product), headers = headers)
        self.assertEqual(200, response.status_code)

        # Caso 2: No se puede insertar un producto que ya existe
        response = self.client.put(api2, data = json.dumps(product), headers = headers)
        self.assertEqual(404, response.status_code)

        # GET PRODUCT
        # Caso 1: Todo ok
        api2=api+"/Apple Store/Iphone 6"
        response = self.client.get(api2)
        self.assertEqual(200, response.status_code)

        api2=api+"/Apple Store/Iphone 7"
        response = self.client.get(api2)
        self.assertEqual(404, response.status_code)

        # POST PRODUCT
        # Caso 1: Todo ok
        api2=api+"/Apple Store"
        product = {       
            "nombre_p": "Iphone 6",
            "descripcion_p": "Iphone 6 64GB Plata"
        }
        response = self.client.post(api2, data = json.dumps(product), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: La tienda o el producto debe existir
        api2=api+"/Apple Store"
        product = {       
            "nombre_p": "Iphone 7",
            "descripcion_p": "Iphone 6 64GB Plata"
        }
        response = self.client.post(api2, data = json.dumps(product), headers = headers)
        self.assertEqual(404, response.status_code)

        # DELETE PRODUCT
        # Caso 1: Todo ok
        api2=api+"/Apple Store"
        product = {       
            "nombre_p": "Iphone 6"
        }
        response = self.client.delete(api2, data = json.dumps(product), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: El producto debe existir
        api2=api+"/Apple Store"
        product = {       
            "nombre_p": "Iphone 7"
        }
        response = self.client.delete(api2, data = json.dumps(product), headers = headers)
        self.assertEqual(404, response.status_code)

        # DELETE SHOP
        # Caso 1: Todo ok
        shop = {
            "nombre": "Apple Store",
         }
        response = self.client.delete(api, data = json.dumps(shop), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: La tienda debe existir
        shop = {
            "nombre": "rrrrrr",
         }
        response = self.client.delete(api, data = json.dumps(shop), headers = headers)
        self.assertEqual(404, response.status_code)

        












        
