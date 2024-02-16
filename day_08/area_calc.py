def paint_calc(height, width, cover):
    cans = height * width / cover
    print(f"You'll need {round(cans)} cans of paint.")

''' Angela's solutions
import math
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover) #math.ceil() always round the number to the higher next
    print(f"You'll need {round(num_of_cans)} cans of paint.")'''


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height = test_h, width = test_w, cover = coverage)