n = int(input())
pattren = []
prev = []
for i in range(1,n+1):
    pattren.append(str(i))
    if i == 1:
        print("  "*(n-i)+",".join(pattren))
    else:
        each = []
        prev_rev = prev[::-1]
        each = pattren+prev_rev
        print("  "*(n-i)+",".join(each)) 
    prev.append(str(i))
pattren.pop()
prev.pop()
for i in range(1,n):
    pattren.pop()
    result = pattren+prev[::-1]
    print("  "*(i)+",".join(result))
    prev.pop()


