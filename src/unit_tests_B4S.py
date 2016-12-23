#####Unit test for midpoint function

######
#####

import unittest
from Image_class import Image

class MyTest(unittest.TestCase):
    def test_midpoint(self):
        test_image = Image("","")
        #correct values
        self.assertEqual(test_image.midpoint([10,10],[20,20]),(15,15))
        #test fail
        #self.assertEqual(test_image.midpoint([10,10],[20,20]),(0,0)
unittest.main()

"""
#####Unit test for get_pixel_per_unit function
def get_pixel_per_unit(self,ref_object, ref_width):
        box = self.get_bounding_box(ref_object)
        points = self.get_distance_cordinate_points(box)
        distX, distY = points[0][0], points[0][1] #TODO: Bad Smell distX never used
        pixelsPerUnit = distY / ref_width
        dimensionY = distY / pixelsPerUnit
       # print("sucessful excution of get_pixel_per_unit")
       # print("ref object is :" + str(ref_object))
        if dimensionY == ref_width:
          print("dimensionY == ref_width")
        return pixelsPerUnit


class MyTest(unittest.TestCase):
    def get_pixel_per_unit(self):
        #correct values
        self.assertEqual(get_pixel_per_unit(Valid input1),(Expected Output))
        #test fail
        self.assertEqual(get_pixel_per_unit(Invalid Input),(Unexpected output))




  def get_bounding_box(self, c):
    box = cv2.minAreaRect(c)
    print("box calling ", box)
   # print("c is :" + str(c)) ATM contors array being passed in here 
    #TODO:Is this nessary
    if imutils.is_cv2():
        box = cv2.cv.BoxPoints(box)
    else:
        box = cv2.boxPoints(box)

    box = np.array(box, dtype="int")

class MyTest(unittest.TestCase):
    def get_bounding_box(self):
        #correct values
        self.assertEqual(get_bounding_box(Valid input1),(Expected Output))
        #test fail
        self.assertEqual(get_bounding_box(Invalid Input),(Unexpected output))


#Test for method extract_contours_and_import_image

 def extract_contors_and_import_image(self):
      # read the image
      # image = cv2.imread(args["image"])
      image = cv2.imread(self.fname_image)
      # convert the image to gray scale, and blur it using GaussianBlur
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      gray = cv2.GaussianBlur(gray, (7, 7), 0)
      # perform edge detection,
      detected_edges = cv2.Canny(gray, 50, 100)
      # perform a dilation
      detected_edges = cv2.dilate(detected_edges, None, iterations=1)
      # perform erosion to close gaps in between object edges
      detected_edges = cv2.erode(detected_edges, None, iterations=1)
      # find contours in the edge map
      cntores = cv2.findContours(detected_edges.copy(), cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)
      print("sucessful excution of extract_contors_and_import_image")
      return cntores, image


class MyTest(unittest.TestCase):
    def extract_contors_and_import_image(self):
        #correct values
        self.assertEqual(extract_contors_and_import_image(Valid input1),(Expected Output))
        #test fail
        self.assertEqual(extract_contors_and_import_image(Invalid Input),(Unexpected output))


#Test for method extract_contours_and_import_image		
 def print_dimensions_on_object(self, X_top_left_top_right, X_top_right_bottom_right, Y_top_left_top_right,
                                 Y_top_right_bottom_right, distX, distY, orig, pixelsPerUnit):
      # Drawing the objects according to their size on the image
      cv2.putText(orig, "{:.1f}in".format(distX / pixelsPerUnit),
                  (int(X_top_left_top_right - 15), int(Y_top_left_top_right - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
                  WHITE, 2)
      cv2.putText(orig, "{:.1f}in".format(distY / pixelsPerUnit),
                  (int(X_top_right_bottom_right + 10), int(Y_top_right_bottom_right)), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
                  WHITE, 2)
class MyTest(unittest.TestCase):
    def extract_contors_and_import_image(self):
        #correct values
        self.assertEqual(extract_contors_and_import_image(Valid input1),(Expected Output))
        #test fail
        self.assertEqual(extract_contors_and_import_image(Invalid Input),(Unexpected output))
"""




