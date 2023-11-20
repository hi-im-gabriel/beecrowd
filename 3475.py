n_to_number = {
    '0': 'zero',
    '1': 'um',
    '2': 'dois',
    '3': 'tres',
    '4': 'quatro',
    '5': 'cinco',
    '6': 'seis',
    '7': 'sete',
    '8': 'oito',
    '9': 'nove'
}

number_to_n = {v: k for k, v in n_to_number.items()}

s = input()

if s.isnumeric():
  print(n_to_number[s])
else:
  print(number_to_n[s])
