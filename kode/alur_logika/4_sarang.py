i = 2 
while (i < 30):
    j = 2 
    while(j <= (i/j)):
        if not (i%j):
            break
        j = j + 1
    if (j > i/j):
        print(f'{i} merupakan bilangan prima')
    i = i + 1