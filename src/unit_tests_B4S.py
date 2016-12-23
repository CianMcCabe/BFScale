#####Unit tests for Image Class

import unittest
from Image_class import Image


global test_image

FNAME = "Control_Image.jpg"
FDIR = "static/"
INDEX = 42

class MyTest(unittest.TestCase):
    def setUp(self):
        global test_image
        test_image = Image(FNAME, FDIR)

    def test_midpoint(self):
        self.assertEqual(test_image.midpoint([10,10],[20,20]),(15,15),
                         msg="Failure:Midpoint")

    def test_gen_index_image(self):
        self.assertEqual(first=test_image.generate_index_image(), second=("index_image_" + FNAME, FDIR),
                         msg="Failure:Generate index Image")

    def test_gen_measured_image(self):
        self.assertEqual(first=test_image.generate_measured_image(), second=("measured_image_" + FNAME, FDIR),
                         msg="Failure:Generate measured Image")

    def test_update_measure_object_index(self):
        test_image.update_measure_object_index(INDEX)
        self.assertEqual(first=test_image.measure_object_index, second= INDEX,
                         msg='Failure:Update Measure Object')

    def test_update_ref_object_index(self):
        test_image.update_ref_object_index(INDEX)
        self.assertEqual(first=test_image.ref_object_index, second=INDEX,
                         msg='Failure:Update Measure Object')

    #TODO: Implement tests for the following if time
    # def test_get_pixel_per_unit(self):
    # def test_get_bounding_box(self):
    # def test_get_distance_cordinate_points(self):
    # def test_import_image_and_extract_contors(self):

unittest.main()




