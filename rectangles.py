print("enter only integer numbers")
print("First Rectangle")

print("Enter x position:")
ax1 = int(input())
print("Enter y position:")
ay1 = int(input())

print("Enter width:")
w1 = int(input())
print("Enter height:")
h1 = int(input())

ax2 = ax1 + w1
ay2 = ay1 + h1

print("Second Rectangle")

print("Enter x position:")
bx1 = int(input())
print("Enter y position:")
by1 = int(input())

print("Enter width:")
w2 = int(input())
print("Enter height:")
h2 = int(input())

bx2 = bx1 + w2
by2 = by1 + h2

print("First Rectangle")
print("coordinate 1:", ax1, ay1)
print("coordinate 2:", ax2, ay1)
print("coordinate 3:", ax1, ay2)
print("coordinate 2:", ax2, ay2)

print("Second Rectangle")
print("coordinate 1:", bx1, by1)
print("coordinate 2:", bx2, by1)
print("coordinate 3:", bx1, by2)
print("coordinate 2:", bx2, by2)

if (bx1 >= ax1 and bx1 <= ax2) and (by1 >= by1 and by1 <= by2):
    print("rectangles intersect")
elif (bx2 >= ax1 and bx2 <= ax2) and (by1 >= by1 and by1 <= by2):
    print("rectangles intersect")
elif (bx1 >= ax1 and bx1 <= ax2) and (by2 >= by1 and by2 <= by2):
    print("rectangles intersect")
elif (bx2 >= ax1 and bx2 <= ax2) and (by2 >= by1 and by2 <= by2):
    print("rectangles intersect")
else:
    print("rectangles dont intersect")

