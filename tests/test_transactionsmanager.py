import sys
import os
sys.path.append('src')
import unittest
import transaction_manager
import json





class TestTransRest(unittest.TestCase):

    def setUp(self):
        self.client = transaction_manager.app.test_client()

    
    def test_unitario(self):

        sale = {
        'nombre_t': "Apple Store",
        'nombre_p': "Ipad Pro 12 pulgadas",
        'cantidad': "1",
        'comprador': "Jorge"
        }
        headers = {'content-type': 'application/json'}
        
        # PUT Transaction
        # Caso 1: Todo ok
        response = self.client.put("/trans", data = json.dumps(sale), headers = headers)
        self.assertEqual(200, response.status_code)

        # GET SHOPS
        # Caso 1: Todo ok
        response = self.client.get("/trans")
        self.assertEqual(200, response.status_code)
        # Caso 2: GET transacciones de una tienda
        response = self.client.get("/trans/Apple Store")
        self.assertEqual(200, response.status_code)
        # Caso 3: La tienda debe existir
        response = self.client.get("/trans/rrrrrrr")
        self.assertEqual(404, response.status_code)

if __name__ == '__main__':
    unittest.main()