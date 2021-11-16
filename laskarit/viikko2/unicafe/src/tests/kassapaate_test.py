import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_oikea_rahamaara_ja_lounasmaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateis_osto_toimii_edullinen(self):
        #tarpeeksi rahaa
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500),260)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

        # ei tarpeeksi rahaa
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200),200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateis_osto_toimii_maukas(self):
        #tarpeeksi rahaa 
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

        #ei tarpeeksi rahaa
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortti_osto_toimii_edullinen(self):
         
        #tarpeeksi rahaa
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(250)),True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)

        # ei tarpeeksi rahaa
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(230)),False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortti_osto_toimii_maukas(self):
         
        #tarpeeksi rahaa
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(410)),True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

        # ei tarpeeksi rahaa
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(230)),False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_lataa_rahaa_kortille(self):
        # tämä vaati pienen muutoksen kassapäätteen koodiin jotta saatiin sama rahasumma 
        # sekä kortille että maksupäätteelle, toisen käsitellessä senttejä ja toisen euroja

        # positiivinen määrä
        self.kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(self.kortti,400)
        self.assertEqual(str(self.kortti),"saldo: 400.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa , 100400)

        #negatiivinen määrä
        self.kassapaate.lataa_rahaa_kortille(self.kortti,-400)
        self.assertEqual(str(self.kortti),"saldo: 400.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa , 100400)
