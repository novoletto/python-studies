tel = {'jack': 555, 'sape': 398}
tel['guido'] = 321

#print(tel['jack'])

#print(list(tel))


## Técnicas de iteração
knights = {'Gallahad': 'the pure', 'Robin': 'the brave'}

for k, v in knights.items():
    pass #print(k, v)

## enumerate para obter chave e valor

for i, v in enumerate(['tic', 'tac', 'toe']):
    pass #print(i, v)


## Percorrer duas ou mais sequencias utilize a função zip
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    pass #print('What is your {0}? It is {1}.'.format(q, a))

## Percorrer uma sequencia em ordem inversa, reversed()

for i in reversed(range(1,10,2)):
    print(i)