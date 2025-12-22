def rectangle_info(width, height):
    area = width * height     
    perimeter = 2 * (width + height)  
    return (area, perimeter)

def is_adult(age):
    return age >= 18

def safe_div(a, b):
    if b == 0:
        return None
    else:
        return a / b
