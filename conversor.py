def cmParaPol():
  
  cm = float(input("Digite o tamanho em centímetros: "))
  pol = cm/2.54
  
  print(f"O valor {cm} em centímetros corresponde a {pol} em polegadas")
  
  file = open('cmParaPol.txt', 'a+')
  file.write('\n cmParaPol: \n')
  file.write(f"O valor {cm} em centímetros corresponde a {pol} em polegadas")
  file.close()