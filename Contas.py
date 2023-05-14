number1 = 0
number2  = 0

number1 = int(input('\nNumero 1 ''\t Resp: '))
print(number1)

while(number1 == 0):

    number2 = int(input('\nNumero 1 ''\t Resp: '))
    print(number1)
    print('\nDigite um número maior que 0\n' *5)

number2= int(input('\nNumero 2' '\tResp: '))
print(number2)

while(number2 == 0):

    number2 = int(input('\nNumero 2 ''\t Resp: '))
    print(number2)
    print('\nDigite um número maior que 0\n' *5)

number1 = number1+number2

print('\nSua Resposta é igual [Soma]: ', number1)

number1 = number1/number2

print('\nSua Resposta é igual [Divisão]', number1)

number1 = number1 * number2 *2

print('\nSua Resposta é igual [Vezes 2]', number1)