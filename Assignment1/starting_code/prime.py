def is_prime(n):
    if n == 1:
        return False

    for integer in range(2,int(n**0.5)+1):
        if n % integer == 0:
            return False
        else:
            continue
    
    return True
    # pass

if __name__ == "__main__":
    
    def list_prime(n):
        p = []
        for i in range(1, n):
            if is_prime(i):
                p.append(i)
        return p

    print(list_prime(10000))
    # print(len(list_prime(10000)))