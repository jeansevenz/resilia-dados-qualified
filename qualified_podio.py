import unittest
from solution import podio_olimpico

class Test(unittest.TestCase):
    def setUp(self):
        self.podio = (
            f"1 - Fulano1 - 1 minutos\n"
            f"2 - Fulano2 - 2 minutos\n"
            f"3 - Fulano3 - 3 minutos\n"
        )

    def test_primeiro_segundo_terceiro(self):
        self.assertEqual(podio_olimpico(1, 2, 3, "Fulano1", "Fulano2", "Fulano3"), self.podio)
    
    def test_primeiro_terceiro_segundo(self):
        self.assertEqual(podio_olimpico(1, 3, 2, "Fulano1", "Fulano3", "Fulano2"), self.podio)
    
    def test_segundo_primeiro_terceiro(self):
        self.assertEqual(podio_olimpico(2, 1, 3, "Fulano2", "Fulano1", "Fulano3"), self.podio)

    def test_segundo_terceiro_primeiro(self):
        self.assertEqual(podio_olimpico(2, 3, 1, "Fulano2", "Fulano3", "Fulano1"), self.podio)

    def test_terceiro_primeiro_segundo(self):
        self.assertEqual(podio_olimpico(3, 1, 2, "Fulano3", "Fulano1", "Fulano2"), self.podio)
        
    def test_terceiro_segundo_primeiro(self):
        self.assertEqual(podio_olimpico(3, 2, 1, "Fulano3", "Fulano2", "Fulano1"), self.podio)