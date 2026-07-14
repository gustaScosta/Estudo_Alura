dicionario = {'prima': 'prima', 'segunda': 'segunda'}

print(dicionario)

entrada = str(input('num: '))

if entrada == 'prima':
    print(dicionario['prima'])

elif entrada == 'segunda':
    print(dicionario['segunda'])
else:
    exit