keys=[]
f = open('vardi1.csv', 'r')
for s in f:
    red_s = s.strip()
    keys.append(red_s)
f.close()
values=[]
f = open('numuri1.csv', 'r')
for s in f:
    red_s = s.strip()
    values.append(red_s)
f.close()
vardi = dict(zip(keys, values))
print(vardi)