

with open(r'../picoCTF_2019/vault.txt') as f:
    lineroni = []
    for line in f:
        line = line.replace('password.charAt(', '')
        line = line.replace(')','')
        line = line.replace('==','')
        line = line.replace('&&','')
        line = line.replace('\'','')
        line = line.replace(';','')
        line = line.split()
        lineroni += str(line) + '\n'
        #with open(r'../picoCTF_2019/vault2.txt','a+') as vault:
            #vault.writelines(str(line) + '\n')
        #vault.close()
        #for i in range(32):
            #liner = int(line[0])
            #if i == liner:
    lineroni = sorted(lineroni)
    with open(r'../picoCTF_2019/vault2.txt','a+') as f2:
        f2.writelines(lineroni)            #print(line[1])
    print(lineroni)
    #with open(r'../picoCTF_2019/vault2.txt') as f2:
        #f2.read()
        #for line in f2:
            #line = line.sorted()
            #print(f2.read())
        #print(line)

