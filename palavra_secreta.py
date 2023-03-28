import os
palavra_secreta = 'bia'
letras_acertadas = ''
tentativas = 0
tentativas_maximas = 10

print('Bem vindos ao jogo da palavra secreta!')
print(f'Você tem {tentativas_maximas} tentativas para completar a palavra secreta!')

while tentativas < tentativas_maximas:
    tentativas += 1

    letra_digitada = input(f'Tentativa {tentativas}, digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        print('Parabéns, você encontrou a palavra secreta!')  
        break
    if tentativas == tentativas_maximas:
        print('Você perdeu, a palavra secreta era:', palavra_secreta)
 