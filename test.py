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

if __name__ == "__main__":
    main()
