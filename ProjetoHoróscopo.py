print('\t\t\n---HORÓSCOPO---\n\t\t')
dia = int(input('Informe o dia em que nasceu: \n'))
mes = int(input('Agora digite o mês: \n'))

# parabéns pelo desenvolvimento
#  o código funciona muito bem!
# Segue o Plano!

if mes == 12 and 31>= dia >= 22 or mes == 1 and 31>= dia <=19:
    print('Você é do signo Capricórnio!')
if mes == 1 and 31>= dia >= 20 or mes == 2 and 29>= dia <=18:
    print('Você é do signo Aquário!')
if mes == 2 and 29>= dia >= 19 or mes == 3 and 31>= dia <=20:
    print('Você é do signo Peixes!')
if mes == 3 and 31>= dia >= 21 or mes == 4 and 30>= dia <=19:
    print('Você é do signo Áries!')
if mes == 4 and 30>= dia >= 20 or mes == 5 and 31>= dia <=20:
    print('Você é do signo Touro!')
if mes == 5 and 31>= dia >= 21 or mes == 6 and 30>= dia <=20:
    print('Você é do signo Gêmeos!')
if mes == 6 and 30>= dia >= 22 or mes == 7 and 31>= dia <=22:
    print('Você é do signo Cancêr!')
if mes == 7 and 31>= dia >= 23 or mes == 8 and 31>= dia <=22:
    print('Você é do signo Leão!')
if mes == 8 and 31>= dia >= 23 or mes == 9 and 30>= dia <=22:
    print('Você é do signo Virgem!')
if mes == 9 and 30>= dia >= 23 or mes == 10 and 31>= dia <=22:
    print('Você é do signo Libra!')
if mes == 10 and 31>= dia >= 23 or mes == 11 and 30>= dia <=21:
    print('Você é do signo Escorpião!')
if mes == 11 and 30>= dia >= 22 or mes == 12 and 31>= dia <=19:
    print('Você é do signo Sagitário!')
if mes > 12 or dia > 31:
    print('ERRO ---  Data irregular!')