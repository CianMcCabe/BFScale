# Component testcase for Image_class.py

# Run file to ensure that main functions of Image_class execute. Testcase is a typical usecae senario.
# Works with "Control_Image" located in subdirectory static

from Image_class import Image

fname_raw_image = "Control_Image.jpg"
file_path = "static/"

#Create Image object
working_image = Image(fname_raw_image, file_path)

# Generate index image (Image with objects highlighted and numbered)
fname_index_image, path = working_image.generate_index_image()

# This image will be displayed to the user. The user will then select a ref object number and object to measure number
# Based on this image
measure_object_index = 4
ref_object_index = 3
# Update Fields in Class
working_image.update_ref_object_index(ref_object_index)
working_image.update_measure_object_index(measure_object_index)

# Generate Image with measurement
fname_measured_image, path = working_image.generate_measured_image()
