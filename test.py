chooses = ["<= Лево", "Право =>"]
width = 800
for i in range(len(chooses)):
    part_i = ((-1)**(i+1)) * 200
    part_width = (width//2)
    pos_x = part_i + part_width
    print("part width: ", part_width, end = "    ")
    print("part i: ", part_i, "")
    print("i: ", i, end = "    ")
    print("x: ", pos_x)
    print()

# ans = 2^8
# print(ans)