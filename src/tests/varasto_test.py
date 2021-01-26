import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_negatiivinen_alkutilavuus(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_negatiivinen_alkusalo(self):
        varasto = Varasto(10, -10)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_konstruktori_salo_pienempi_kuin_tilavuus(self):
        varasto = Varasto(10, 4)
        self.assertAlmostEqual(varasto.saldo, 4)

    def test_konstruktori_salo_suurempi_kuin_tilavuus(self):
        varasto = Varasto(4, 10)
        self.assertAlmostEqual(varasto.saldo, 4)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)


    def test_lisays_lisaa_saldoa_negatiivinen(self):
        self.varasto.lisaa_varastoon(-10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    
    def test_lisays_likaa_laittaa_niin_paljon_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(1000)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_negatiivinen_maara_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-10)

        self.assertAlmostEqual(saatu_maara, 0.0)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ottaminen_liikaa_palauttaa_kaiken(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 8)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_to_string(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(str(self.varasto), "saldo = 8, vielä tilaa 2")