# Problem:
# Given integers x, y, z, and n, generate all 3D coordinates [i, j, k]
# such that 0 <= i <= x, 0 <= j <= y, 0 <= k <= z,
# and i + j + k != n.
# Output:
#   - Print the list of these coordinates in lexicographic order using list comprehension.


if __name__ == '__main__':
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    n = int(input("Enter n: "))

    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

    print(coordinates)