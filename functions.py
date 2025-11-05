#Functions are reusable blocks of code that do specific tasks. Instead of writing the same code multiple times, you write it once as a function and call it whenever needed.
#Parameters let you pass data into functions. Instead of hardcoding values, you make functions flexible to work with different inputs.
def great_name(name):
    print(f"hello , {name}")

name= "suyash"

def cal_area(breadth , width):
    total_area= breadth*width
    return total_area

area= cal_area(10, 12)
print(area)

