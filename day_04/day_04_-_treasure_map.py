row1 = ["O","O","O"]
row2 = ["O","O","O"]
row3 = ["O","O","O"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0]) - 1
row = int(position[1]) - 1

if column >= 0 and column < 3:
    if row >= 0 and row < 3:
        map[row][column] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    else:
        print("Invalid row number")
else:
        print("Invalid column number")


''' My first solution
position = int(input("Where do you want to put the treasure? "))
column = int(position / 10)
row = position - (column * 10)

if column >= 0 and column <= 3:
    if row >= 0 and row <= 3:
        map[row - 1][column - 1] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    else:
        print("Invalid row number")
else:
        print("Invalid column number")'''
