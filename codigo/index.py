qvit = int(input('Digite a quantidade de vitórias: '))
qder = int(input('Digite a quantidade de derrotas: '))
pts = qvit-qder

if pts <= 10:
    print('O Héroi tem o saldo de {} vítorias está no nível de ferro.'.format(pts))
elif pts > 11 and pts <=  20:
    print('O Héroi tem o saldo de {} vítorias está no nível de bronze.'.format(pts))
elif pts > 21 and pts <= 50:
    print('O Héroi tem o saldo de {} vítorias está no nível de prata.'.format(pts))
elif pts > 51 and pts <= 80:
    print('O Héroi tem o saldo de {} vítorias está no nível de ouro.'.format(pts))
elif pts > 81 and pts <= 90:
    print('O Héroi tem o saldo de {} vítorias está no nível de diamante.'.format(pts))
elif pts > 91 and pts <= 100:
    print('O Héroi tem o saldo de {} vítorias está no nível de lendário.'.format(pts))
elif pts >= 101:
    print('O Héroi tem o saldo de {} vítorias está no nível de imortal.'.format(pts))