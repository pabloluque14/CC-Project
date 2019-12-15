# -*- coding: utf-8 -*-
import sys
sys.path.append('src')
import unittest
from producto import Producto
from tienda import Tienda

class Test(unittest.TestCase):

    def test_constructor(self):
        # Para clase tienda
        tienda = Tienda(0,"Moviles Shop")
        
        self.assertEqual(tienda.getId(),0,"El id inicial tiene que ser 0")
        self.assertEqual(tienda.getNombre(),"Moviles Shop","El nombre de la tienda debería ser: Moviles Shop")
        self.assertEqual(tienda.getDescripcion(),None,"La descripción debería ser igual a None")
        self.assertEqual(tienda.getDireccion(),None,"La dirección debería ser igual a None")
        self.assertEqual(tienda.getInfoContacto(),None,"La información de contacto debería ser igual a None")
        self.assertEqual(tienda.getTrans(),0,"Las transacciones iniciales deberían ser 0")
        self.assertEqual(tienda.getVal(),0,"La valoración inicial debería ser 0")
        self.assertEqual(len(tienda),0,"No debería haber productos")

        # Para clase producto
        p = Producto("Xiaomi Mi 9 T")

        self.assertEqual(p.getId(),0,"El id inicial tiene que ser 0")
        self.assertEqual(p.getNombre(),"Xiaomi Mi 9 T","El nombre de la tienda debería ser: Xiaomi Mi 9 T")
        self.assertEqual(p.getDescripcion(),None,"La descripción debería ser igual a None")
        self.assertEqual(p.getPrecio(),0,"Precio inicial de 0 euros")
        self.assertEqual(p.getIsOnline(),False,"Si no se cambia el producto no está disponible online")
    
    def test_metodos(self):
        tienda = Tienda(0,"Moviles Shop")
        
        tienda.setId(1)
        tienda.setNombre("Moviles Shop Granada")
        tienda.setDescripcion("Tienda de móviles")
        tienda.setDireccion("Avd Olivia")
        tienda.setInfoContacto("movilesshop@gmail.com")
        tienda.setTrans(2)
        tienda.setVal(200)
        
        # Para clase tienda
        self.assertEqual(tienda.getId(),1,"")
        self.assertEqual(tienda.getNombre(),"Moviles Shop Granada",)
        self.assertEqual(tienda.getDescripcion(),"Tienda de móviles")
        self.assertEqual(tienda.getDireccion(),"Avd Olivia")
        self.assertEqual(tienda.getInfoContacto(),"movilesshop@gmail.com")
        self.assertEqual(tienda.getTrans(),2)
        self.assertEqual(tienda.getVal(),200)
        
        # Para clase producto
        p = Producto("Xiaomi Mi 9 T")

        p.setId(1)
        p.setDescripcion("Nuevo movil de la marca china xiaomi")
        p.setIsOnline(True)
        p.setNombre("Xiaomi Mi 9 T Pro")
        p.setPrecio(300)

        self.assertEqual(p.getId(),1)
        self.assertEqual(p.getNombre(),"Xiaomi Mi 9 T Pro")
        self.assertEqual(p.getDescripcion(),"Nuevo movil de la marca china xiaomi")
        self.assertEqual(p.getPrecio(),300)
        self.assertEqual(p.getIsOnline(),True)

    def test_integracion(self):
        tienda = Tienda(0,"Moviles Shop")
        p = Producto("Xiaomi Mi 9 T","nuevo movil chino",300)
        p2 = Producto("Xiaomi Mi 9 T Pro","nuevo movil chino",400)

        tienda.addProducto(p)
        tienda.addProducto(p2)

        self.assertEqual(len(tienda),2)
        self.assertIs(tienda.getProducto_byId(0),p)
        self.assertIs(tienda.getProducto_byId(1),p2)

        tienda.delProducto_byId(0)
        self.assertEqual(len(tienda),1)



if __name__ == '__main__':
    unittest.main()