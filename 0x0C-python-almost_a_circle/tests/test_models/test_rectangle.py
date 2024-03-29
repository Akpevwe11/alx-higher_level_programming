#!/usr/bin/python3
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_no_docstring(self):
        self.assertIsNotNone(Rectangle.__doc__)

    def test_structure(self):
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, "width"))
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertTrue(hasattr(Rectangle, "height"))
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertTrue(hasattr(Rectangle, "x"))
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertTrue(hasattr(Rectangle, "y"))
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test_rectangle_initialize(self):
        self.assertIsNotNone(Rectangle(1, 1))

    def test_rectangle_missing_arguments(self):
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)

    def test_rectangle_init(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 2)

        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r3.id, 3)

        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 5)

    def test_rectangle_width(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertGreater(r1.width, 0)
        self.assertIs(type(r1.width), int)
        self.assertRaises(TypeError, Rectangle, 1.1, 2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, -1, 2)

    def test_rectangle_height(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.height, 2)
        self.assertGreater(r1.height, 0)
        self.assertIs(type(r1.height), int)
        self.assertRaises(TypeError, Rectangle, 2, 1.1)
        self.assertRaises(ValueError, Rectangle, 2, 0)
        self.assertRaises(ValueError, Rectangle, 2, -1)

    def test_rectangle_x(self):
        self.assertEqual(Rectangle(1, 2).x, 0)
        self.assertEqual(Rectangle(1, 2, 3).x, 3)
        self.assertGreaterEqual(Rectangle(1, 2, 3).x, 0)
        self.assertGreaterEqual(Rectangle(1, 2, 0).x, 0)
        self.assertIs(type(Rectangle(1, 2, 3).x), int)
        self.assertRaises(TypeError, Rectangle, 2, 1, 1.1)
        self.assertRaises(ValueError, Rectangle, 2, 1, -1)

    def test_rectangle_y(self):
        self.assertEqual(Rectangle(1, 2).y, 0)
        self.assertEqual(Rectangle(1, 2, 4, 3).y, 3)
        self.assertGreaterEqual(Rectangle(1, 2, 3, 3).y, 0)
        self.assertGreaterEqual(Rectangle(1, 2, 4, 0).y, 0)
        self.assertIs(type(Rectangle(1, 2, 3, 3).y), int)
        self.assertRaises(TypeError, Rectangle, 2, 1, 1, 2.2)
        self.assertRaises(ValueError, Rectangle, 2, 1, 1, -1)

    def test_rectangle_update(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.id, 1)
        r1.update()
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r1.update(10)
        self.assertEqual(r1.id, 10)
        r1.update(20, 30)
        self.assertEqual(r1.id, 20)
        self.assertEqual(r1.width, 30)
        r1.update(30, 40, 50)
        self.assertEqual(r1.id, 30)
        self.assertEqual(r1.width, 40)
        self.assertEqual(r1.height, 50)
        r1.update(40, 50, 60, 70)
        self.assertEqual(r1.id, 40)
        self.assertEqual(r1.width, 50)
        self.assertEqual(r1.height, 60)
        self.assertEqual(r1.x, 70)
        r1.update(50, 60, 70, 80, 90)
        self.assertEqual(r1.id, 50)
        self.assertEqual(r1.width, 60)
        self.assertEqual(r1.height, 70)
        self.assertEqual(r1.x, 80)
        self.assertEqual(r1.y, 90)
        r1.update(60, 70, 80, 90, 100, id=10, width=20)
        self.assertEqual(r1.id, 60)
        self.assertEqual(r1.width, 70)
        self.assertEqual(r1.height, 80)
        self.assertEqual(r1.x, 90)
        self.assertEqual(r1.y, 100)
        r1.update(70, id=10, width=20)
        self.assertNotEqual(r1.id, 10)
        self.assertEqual(r1.id, 70)
        self.assertNotEqual(r1.width, 20)
        r1.update(id=10, width=20)
        self.assertEqual(r1.id, 10)
        self.assertNotEqual(r1.id, 70)
        self.assertEqual(r1.width, 20)
        self.assertNotEqual(r1.width, 70)
        r1.update(hight=30)
        self.assertEqual(r1.height, 80)
        self.assertNotEqual(r1.height, 30)
        r1.update(x=5, y=6, id=100, width=200, height=400)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 400)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)
        r1.update(x=5, xx=8, y=6, id=100, width=200, height=400)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 400)
        self.assertEqual(r1.x, 5)
        self.assertNotEqual(r1.x, 8)
        self.assertEqual(r1.y, 6)

    def test_rectangle_area(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)
        r1.update(1, 100, 20, 5, 6)
        self.assertEqual(r1.area(), 2000)
        r1.width = 5
        r1.height = 6
        self.assertEqual(r1.area(), 30)

    @staticmethod
    def capture_our_buffer(obj, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        buffer = io.StringIO()
        sys.stdout = buffer
        if method == "print":
            print(obj)
        elif method == "display":
            obj.display()
        sys.stdout = sys.__stdout__
        return buffer

    def test_rectangle_display_width_height(self):
        r1 = Rectangle(2, 3)
        buffer = TestRectangle.capture_our_buffer(r1, "display")
        self.assertEqual("##\n##\n##\n", buffer.getvalue())

    def test_rectangle_display_width_height_x(self):
        r1 = Rectangle(2, 3, 2)
        buffer = TestRectangle.capture_our_buffer(r1, "display")
        self.assertEqual("  ##\n  ##\n  ##\n", buffer.getvalue())

    def test_rectangle_display_width_height_x_y(self):
        r1 = Rectangle(2, 3, 2, 4)
        buffer = TestRectangle.capture_our_buffer(r1, "display")
        self.assertEqual("\n\n\n\n  ##\n  ##\n  ##\n", buffer.getvalue())

    def test_rectangle__str__(self):
        r1 = Rectangle(20, 30)
        self.assertEqual("[Rectangle] (1) 0/0 - 20/30", r1.__str__())
        r1 = Rectangle(20, 30, 41, 51)
        self.assertEqual("[Rectangle] (2) 41/51 - 20/30", r1.__str__())
        r1 = Rectangle(22, 33, 44, 55, 66)
        self.assertEqual("[Rectangle] (66) 44/55 - 22/33", r1.__str__())

    def test_rectangle_print(self):
        r1 = Rectangle(2, 3, 4, 5)
        buffer = TestRectangle.capture_our_buffer(r1, "print")
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3\n", buffer.getvalue())

    def test_rectangle_to_dictionary(self):
        r1_dict = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        test_dict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(test_dict, r1_dict)
        r1_dict = Rectangle(10, 22, 30, 44).to_dictionary()
        test_dict = {'id': 1, 'width': 10, 'height': 22, 'x': 30, 'y': 44}
        self.assertEqual(test_dict, r1_dict)
