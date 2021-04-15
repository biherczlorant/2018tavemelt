# 1. feladat a bentlévők számát is megállapítom hátha kell később
data = []
bentlevocnt = 0
with open('ajto.txt', 'r') as f:
    for line in f:
        splitter = line.strip().split(' ')
        if splitter[3] == 'be':
            bentlevocnt += 1
        else:
            bentlevocnt -=1
        linedata = {
            'ora': int(splitter[0]),
            'perc': int(splitter[1]),
            'id': int(splitter[2]),
            'irany': splitter[3],
            'bentlevokcnt': bentlevocnt
        }
        data.append(linedata)
    f.close()
# 2. feladat
elsobelep = 0
ucsokilep = 0
for i in data:
    if i['irany'] == 'be' and elsobelep==0:
        elsobelep = i['id']
    elif i['irany'] == 'ki' and ucsokilep==0:
        ucsokilep = i['id']
print(f'2. feladat\nAz első belépő: {elsobelep}\nAz utolsó kilépő: {ucsokilep}')
# 3. feladat
with open('athaladas.txt', 'w') as f:
    idk = set()
    for i in data:
        idk.add(i['id'])
    for id in sorted(idk):
        athaladasok = [i for i in data if i['id']==id]
        f.write(f'{id} {athaladasok.__len__()}\n')
    f.flush()
    f.close()
# 4. feladat
print("4. feladat\nA végén a társalgóban voltak: ")
for id in sorted(idk):
    athaladasok = [i['irany'] for i in data if i['id']==id]
    if athaladasok[-1] == 'be':
        print(id, end=" ")
# 5. feladat
maxszemely = 0
maxora = 0
maxperc = 0
for i in data:
    if i['bentlevokcnt'] > maxszemely:
        maxszemely = i['bentlevokcnt']
        maxora = i['ora']
        maxperc = i['perc']
print(f'\n5. feladat\nPéldául {maxora}:{maxperc}-kor voltak a legtöbben a társalgóban.')
# 6. feladat
bekertid = int(input('6.feladat\nAdja meg a személy azonosítóját!'))
# 7. feladat
beki = []
csakugy = 0
for i in data:
    if i['id'] == bekertid:
        beki.append([i['ora'], i['perc']])
for i in beki:
    csakugy+=1
    if csakugy%2==0:
        print(f'{i[0]}:{i[1]}')
    else:
        print(f'{i[0]}:{i[1]}-', end="")
# 8. feladat
def idopercbe(ora, perc):
    percek = ora*60+perc
    return percek
csakugy = 0
kettesido = 0
egyesido = 0
benttoltott = 0
for i in beki:
    csakugy+=1
    if csakugy%2==0:
        kettesido = idopercbe(i[0], i[1])
        benttoltott += (kettesido-egyesido)
    else:
        egyesido = idopercbe(i[0], i[1])
if beki.__len__()%2!=0:
    print(
        f'\n8. feladat\nA(z) {bekertid}. személy összesen {benttoltott} percet volt bent, '
        f'a megfigyelés végén a társalgóban volt.')
else:
    print(
        f'8. feladat\nA(z) {bekertid}. személy összesen {benttoltott} percet volt bent, '
        f'a megfigyelés végén nem volt a társalgóban.')
