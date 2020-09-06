import sys
import os
sys.path.append('src')
import unittest
import shop_manager
import json





class TestShopRest(unittest.TestCase):

    def setUp(self):
        self.client = shop_manager.app.test_client()

    
    def test_unitario(self):
        shop = {
            "nombre": "Cascabeles",
            "descripcion": "Tienda de musica", 
            "direccion": "avd Barcelona", 
            "info":"111111111"
         }
        headers = {'content-type': 'application/json'}
        
        # PUT SHOP
        # Caso 1: Todo ok
        response = self.client.put("/shops", data = json.dumps(shop), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: No se puede insertar la misma tienda
        response = self.client.put("/shops", data = json.dumps(shop), headers = headers)
        self.assertEqual(404, response.status_code)

        # GET SHOPS
        # Caso 1: Todo ok
        response = self.client.get("/shops")
        self.assertEqual(200, response.status_code)
        # Caso 2: GET de una tienda
        response = self.client.get("/shops/Cascabeles")
        self.assertEqual(200, response.status_code)
        # Caso 3: La tienda debe existir
        response = self.client.get("/shops/rrrrrrr")
        self.assertEqual(404, response.status_code)

        # POST
        # Caso 1: Todo ok
        shop = {
            "nombre": "Cascabeles",
            "info":"cascabeles@shop.com"
         }
        response = self.client.post("/shops", data = json.dumps(shop), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: La tienda debe existir
        shop = {
            "nombre": "rrrrr",
            "info":"cascabeles@shop.com"
         }
        response = self.client.post("/shops", data = json.dumps(shop), headers = headers)
        self.assertEqual(404, response.status_code)
         # Caso 3: Hay que pasarle el nombre de la tienda
        shop = {
            "info":"cascabeles@shop.com"
         }
        headers = {'content-type': 'application/json'}
        response = self.client.post("/shops", data = json.dumps(shop), headers = headers)
        self.assertEqual(400, response.status_code)

        # DELETE
        # Caso 1: Todo ok
        shop = {
            "nombre": "Cascabeles",
         }
        response = self.client.delete("/shops", data = json.dumps(shop), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: La tienda debe existir
        shop = {
            "nombre": "rrrrrr",
         }
        response = self.client.delete("/shops", data = json.dumps(shop), headers = headers)
        self.assertEqual(404, response.status_code)
    
    def test_integracion(self):
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
        response = self.client.put("/shops", data = json.dumps(shop), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: No se puede insertar la misma tienda
        response = self.client.put("/shops", data = json.dumps(shop), headers = headers)
        self.assertEqual(404, response.status_code)

        # PUT PRODUCT
        # Caso 1: Todo ok
        
        response = self.client.put("/shops/Apple Store", data = json.dumps(product), headers = headers)
        self.assertEqual(200, response.status_code)

        # Caso 2: No se puede insertar un producto que ya existe
        response = self.client.put("/shops/Apple Store", data = json.dumps(product), headers = headers)
        self.assertEqual(404, response.status_code)

        # GET PRODUCT
        # Caso 1: Todo ok
        response = self.client.get("/shops/Apple Store/Iphone 6")
        self.assertEqual(200, response.status_code)

        response = self.client.get("/shops/Apple Store/Iphone 7")
        self.assertEqual(404, response.status_code)

        # POST PRODUCT
        # Caso 1: Todo ok
        
        product = {       
            "nombre_p": "Iphone 6",
            "descripcion_p": "Iphone 6 64GB Plata"
        }
        response = self.client.post("/shops/Apple Store", data = json.dumps(product), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: La tienda o el producto debe existir
        product = {       
            "nombre_p": "Iphone 7",
            "descripcion_p": "Iphone 6 64GB Plata"
        }
        response = self.client.post("/shops/Apple Store", data = json.dumps(product), headers = headers)
        self.assertEqual(404, response.status_code)

        # DELETE PRODUCT
        # Caso 1: Todo ok
        product = {       
            "nombre_p": "Iphone 6"
        }
        response = self.client.delete("/shops/Apple Store", data = json.dumps(product), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: El producto debe existir
        product = {       
            "nombre_p": "Iphone 7"
        }
        response = self.client.delete("/shops/Apple Store", data = json.dumps(product), headers = headers)
        self.assertEqual(404, response.status_code)

        # DELETE SHOP
        # Caso 1: Todo ok
        shop = {
            "nombre": "Apple Store",
         }
        response = self.client.delete("/shops", data = json.dumps(shop), headers = headers)
        self.assertEqual(200, response.status_code)
        # Caso 2: La tienda debe existir
        shop = {
            "nombre": "rrrrrr",
         }
        response = self.client.delete("/shops", data = json.dumps(shop), headers = headers)
        self.assertEqual(404, response.status_code)
        
if __name__ == '__main__':
    unittest.main()

        












        
