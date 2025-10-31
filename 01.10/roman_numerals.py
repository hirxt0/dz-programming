def convertation(n: int) -> str:
  sl = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: "L", 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
  res = []
  for num, roman in sl.items():
    while n >= num:
      res.append(roman)
      n -= num
  return "".join(res)



def anti_convertation(ch: str) -> int:
  sl = {'M': 1000,'D': 500, 'C': 100, "L": 50, 'X': 10, 'V': 5, 'I': 1}
  res = 0
  for i in range(len(ch) - 1):
    if sl[ch[i]] < sl[ch[i + 1]]:
      res -= sl[ch[i]]
    else:
      res += sl[ch[i]]
  res += sl[ch[-1]]
  return res
