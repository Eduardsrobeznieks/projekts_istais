keys=[]
f = open('C:/Users/erobs/Documents/GitHub/projekts_istais/open tests/vardi2.csv', 'r', encoding='utf-8')
for s in f:
    red_s = s.strip()
    keys.append(red_s)
f.close()
values=[]
f = open('C:/Users/erobs/Documents/GitHub/projekts_istais/open tests/numuri1.csv', 'r')
for s in f:
    red_s = s.strip()
    values.append(red_s)
f.close()
vardi = dict(zip(keys , values))
print(vardi)