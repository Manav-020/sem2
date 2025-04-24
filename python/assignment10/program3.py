def odd_square(n):
    if n % 2 == 0:
        raise ValueError("Only odd-order magic squares are supported by this method.")
    
    magic_square = [[0] * n for _ in range(n)]
    
    i, j = 0, n // 2  # Start from the middle of the top row
    
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        
        if magic_square[new_i][new_j]:  # If the new position is already filled
            i += 1
        else:
            i, j = new_i, new_j
    
    return magic_square
def even_square(n):
    if n % 4 != 0:
        raise ValueError("Only doubly even numbers (divisible by 4) are allowed")

    magic_square = [[(n * i) + j + 1 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i + j) % 4 == 3):
                magic_square[i][j] = n * n + 1 - magic_square[i][j]

    return magic_square

n=int(input("enter number:"))
if n%2!=0:
    ans=odd_square(n)
    for i in ans:
        print(i)
else:
    a=even_square(n)
    for i in a:
        print(i)
