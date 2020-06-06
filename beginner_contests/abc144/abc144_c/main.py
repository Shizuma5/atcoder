import fractions

def make_divisor_list(num):
    i = 1
    table = []
    while i * i <= num:
        if num%i == 0:
            table.append(i)
            table.append(num//i)
        i += 1
    table = list(set(table))
    return table

N = int(input())

divisors = sorted(make_divisor_list(N))
center = int(len(divisors) / 2)

if len(divisors) % 2 == 1:
    ans = (divisors[center] - 1) * 2
else:
    ans = divisors[center] - 1 + divisors[center-1] - 1

print(ans)
