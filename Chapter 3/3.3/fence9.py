"""
ID: aasang1
LANG: PYTHON3
PROG: fence9
"""

fin = open("fence9.in", 'r')
in_arr = [i.split("\n")[0] for i in fin.readlines()]
fin.close()

n, m, p = in_arr[0].split()
x, y, p = int(n), int(m), int(p)

def gcd(a, b):
    if a == 0:
        return b
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

output = p*y/2+1-(gcd(x,y)+gcd(abs(x-p), y)+p)/2

fout = open("fence9.out", 'w')
fout.write(str(int(output)) + "\n")
fout.close()