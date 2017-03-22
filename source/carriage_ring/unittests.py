import unittest
from source.carriage_ring.carriage_ring import Carriage, CarriageRing


class CarriageTest(unittest.TestCase):

    def setUp(self):

        self.coupling = [Carriage(light='off'), Carriage(light='off')]
        self.carriage = self.coupling[0]

    def test_create(self):

        self.assertTrue(hasattr(self.carriage, 'turn_light_on'))
        self.assertTrue(hasattr(self.carriage, 'turn_light_off'))
        self.assertTrue(hasattr(self.carriage, 'light_is_turned_on'))

    def test_on_off_light(self):

        self.carriage.turn_light_on()
        self.assertTrue(self.carriage.light_is_turned_on)

        self.carriage.turn_light_off()
        self.assertFalse(self.carriage.light_is_turned_on)

    def test_distin_lighting(self):

        self.coupling[0].turn_light_on()
        self.coupling[1].turn_light_off()

        self.assertTrue(self.coupling[0].light_is_turned_on)
        self.assertFalse(self.coupling[1].light_is_turned_on)


class TestCarriageRing(unittest.TestCase):

    def setUp(self):
        self.carriage_ring = CarriageRing()

    def test_create(self):

        self.assertTrue(hasattr(self.carriage_ring, 'next'))
        self.assertTrue(hasattr(self.carriage_ring, 'previous'))
        self.assertTrue(hasattr(self.carriage_ring, 'current_carriage'))

    def test_is_ring(self):

        start = self.carriage_ring.current_carriage

        while self.carriage_ring.current_carriage is not start:
            self.carriage_ring.next()

    def test_is_ring_reversed(self):

        start = self.carriage_ring.current_carriage

        while self.carriage_ring.current_carriage is not start:
            self.carriage_ring.previous()


if __name__ == '__main__':
    unittest.main()