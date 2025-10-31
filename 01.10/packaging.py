def print_pack_report(n: int) -> str:
  
  for i in range(n, 0, -1):

    if i % 5 == 0 and i % 3 == 0:
      print(f'{i}, расфасуем и по 3 и по 5')

    elif i % 5 == 0:
      print(f'{i}, расфасуем по 5')

    elif i % 3 == 0:
      print(f'{i}, расфасуем по 3')

    else:
      print(f'{i}, не сможем нормально расфасовать')

  return 'конец'

print(print_pack_report(10))