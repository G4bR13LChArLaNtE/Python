n1 = int(input())
alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

if 1 <= n1 <= 26:
    for q in range(0, n1):
        print(alfa[q]*(q+1))