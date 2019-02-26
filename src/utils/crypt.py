# encrypt passwor======================================
chaisarMove = 2


def encrypt(secretMessage):
  chars = "abcdefghijklmnopqrstuvwxyz0123456789"
  listCharts = list(chars)

  listSecretMessage = list(secretMessage)
#   print(listCharts)
#   print("=============")
#   print(listSecretMessage)

  for i in range(len(listSecretMessage)):
    indexChar = listCharts.index(listSecretMessage[i])
    changeChar = (indexChar+chaisarMove) % len(chars)
    listSecretMessage[i] = listCharts[changeChar]
  return "".join(listSecretMessage)


# decrypt passwor======================================


def decrypt(secretMessage):
  chars = "abcdefghijklmnopqrstuvwxyz0123456789"
  listCharts = list(chars)

  listSecretMessage = list(secretMessage)
#   print(listCharts)
#   print("=============")
#   print(listSecretMessage)

  for i in range(len(listSecretMessage)):
    indexChar = listCharts.index(listSecretMessage[i])
    changeChar = (indexChar-chaisarMove) % len(chars)
    listSecretMessage[i] = listCharts[changeChar]
  return "".join(listSecretMessage)
