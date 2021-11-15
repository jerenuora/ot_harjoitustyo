import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahaa_voi_lisätä(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.1")

    def test_rahaa_voi_nostaa_jos_saldoa_on(self):
        self.maksukortti.ota_rahaa(9)
        self.assertEqual(str(self.maksukortti), "saldo: 0.01")

    def test_rahaa_ei_voi_nostaa_jos_saldoa_ei_ole(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_ota_rahaa_palautusarvo_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(11), False)    
        
    def test_ota_rahaa_palautusarvo_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10), True)