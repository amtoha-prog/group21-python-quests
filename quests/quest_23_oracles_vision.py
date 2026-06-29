def calculate_area(length, width):
    area = length * width

    return area
area_1 = calculate_area(5, 3)
area_2 = calculate_area(12.5, 4)

print(f"Rectangle 1 (5 x 3)      → Area = {area_1}")
print(f"Rectangle 2 (12.5 x 4)   → Area = {area_2}")

print(f"Combined area of both     → {area_1 + area_2}")
