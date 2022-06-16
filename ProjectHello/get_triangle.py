def get_triangle(fig):
    n = 10
    for i in range(1, n + 1, 2):
        print(' ' * (int((n - i) / 2)), fig * i, sep='')
