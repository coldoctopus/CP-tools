<<<<<<< HEAD
a = [2,5,7,1,3,4,4,2,5,1]
print(a[-1])


# n = 3
# m = 1
# records = [1, -1, 0]

n =9
m = 3
records = [0, 0, 1, 0, 2, -3, -2, -2, 1]

=======
def count_lego_bricks(base, height):
    # The area of the triangle
    triangle_area = 0.5 * base * height
    
    # The area of one LEGO brick (2x4)
    brick_area = 8  # 2 * 4
    
    # The number of complete LEGO bricks that fit in the triangle area
    return int(triangle_area // brick_area)

def main():
    # Read input values (base and height)
    base, height = map(int, input().split())
    
    # Call the function to compute the number of LEGO bricks
    result = count_lego_bricks(base, height)
    
    # Output the result
    print(result)
>>>>>>> a059a2cfdecbaf4b11e124e8980a4ff785f8cd21

if __name__ == "__main__":
    main()
