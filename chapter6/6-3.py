def get_total_page(m, n):
    if m % n == 0:
        return m//n
    else:
        return m//n+1

print(get_total_page(19,10))
