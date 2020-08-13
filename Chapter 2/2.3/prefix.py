"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: prefix
"""

INPUTFILE = "prefix.in"
OUTFILE = "prefix.out"


fin = open(INPUTFILE, 'r')

arr = []
seq = ""
listdone = False
for line in fin.readlines():
    if "." not in line and not listdone:
        [arr.append(str(item)) if "\n" not in item else arr.append(str(item).split("\n")[0]) for item in line.split(" ")]
    elif "." in line:
        listdone = True
    else:
        seq += str(line).split("\n")[0]
fin.close()

seq_length = len(seq)
max = 0
available = [0 for i in range(200010)]
available[0] = True
for i in range(seq_length):
    if available[i] == True:
        for p in arr:

            p_len = len(p)

            if (i+p_len<=seq_length and seq[i:i+p_len] == p):
                if max < i+p_len:
                    max = i+p_len

                available[i+p_len]=True

fout = open(OUTFILE, 'w')
fout.write(str(max) + "\n")
fout.close()