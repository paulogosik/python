def area(width, length):
    return width * length


print(f"{'Land Control':=^30}")
land_width = float(input("Width: "))
land_length = float(input("Length: "))
land_area = area(land_width, land_length)

print(f"Your landa area [{land_width:.1f} x {land_length:.1f}] is {land_area:.1f}m²")
print("-" * 30)
