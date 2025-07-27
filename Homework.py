import math

angle_degrees = int(input("Enter the degrees of your triangle:"))
angle_radians = math.radians(angle_degrees)

sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)

print(f"sin({angle_degrees}°) = {sin_value}")
print(f"cos({angle_degrees}°) = {cos_value}")
print(f"tan({angle_degrees}°) = {tan_value}")