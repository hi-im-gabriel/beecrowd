def obter_signo(data):
    dia, mes = map(int, data.split('/'))

    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return 'aries'
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return 'touro'
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return 'gemeos'
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return 'cancer'
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return 'leao'
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return 'virgem'
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return 'libra'
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return 'escorpiao'
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return 'sagitario'
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return 'capricornio'
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return 'aquario'
    else:
        return 'peixes'

data_input = input()
signo = obter_signo(data_input)
print(signo)
