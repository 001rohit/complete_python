# Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
color1 = set(["white","black","red"])
color2 = set(["green","brown","red"])
print("Original set element: ")
print(color1)
print(color2)

print("\n Difference of color1 and color2 ")
print(color1.difference(color2))
print()
print(color2.difference(color1))