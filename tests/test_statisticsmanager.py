import sys
import os
sys.path.append('src')
import unittest
import statistic_manager
import json



class TestStatsRest(unittest.TestCase):

    def setUp(self):
        self.client = statistic_manager.app.test_client()

    
    def test_unitario(self):

        stat = {
        'nombre_t': "Apple Store",
        'ventas': "300",
        'puntuacion': "5"
        }
        headers = {'content-type': 'application/json'}
        
        # PUT Transaction
        # Caso 1: Todo ok
        response = self.client.put("/stats", data = json.dumps(stat), headers = headers)
        self.assertEqual(200, response.status_code)

        # GET SHOPS
        # Caso 1: Todo ok
        response = self.client.get("/stats")
        self.assertEqual(200, response.status_code)
        # Caso 2: GET transacciones de una tienda
        response = self.client.get("/stats/Apple Store")
        self.assertEqual(200, response.status_code)
        # Caso 3: La tienda debe existir
        response = self.client.get("/stats/rrrrrrr")
        self.assertEqual(404, response.status_code)

if __name__ == '__main__':
    unittest.main()