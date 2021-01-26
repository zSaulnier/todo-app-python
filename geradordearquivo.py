while True:
    r = int(input('1 para criar um novo documento e 2 p sair '))
    if r == 2 :
        break
    if r == 1:
        dia = int(input('que dia é hoje? '))
        docs = open(f"dia{dia}.txt", 'w')
        docs.write(f'eu sou o documento do dia {dia}')
        docs.close()
abrirdocs = int(input('Qual o dia do doc que vc quer abrir?'))
doc_aberto = open(f"dia{abrirdocs}.txt",'r')
for linhas in doc_aberto:
    print(linhas)