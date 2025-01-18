def sol(a, b):
    count = 0
    ans = 0
    for i in range(0, a):
        # Calculate the width of the current row using integer arithmetic
        temp = (i * b * 112.5) / (a * 225)
        
        # Check if temp is >= 1 and represents a complete block
        if temp >= 1 and temp == int(temp):
            ans += int(temp)
            count += 1

    # Return the total number of full bricks, adjusting for the square blocks in each layer
    return ans - (count // 2)


def main():
    base, height = map(int, input().split())
    print(max(sol(base, height), sol(height, base)))


if __name__ == "__main__":
    main()
