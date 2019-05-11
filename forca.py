import unicodedata
import re
import string
import random


def removerAcentosECaracteresEspeciais(palavra):
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

palavras = "Como você pode ver, uma garotinha está deitada displicentemente no colo de um senhor bem velhinho e bem simpático. Ela parece um anjo. Loirinha, cabelo castanho-claro, encaracolado, nariz e boca perfeitos, ar inteligente e sadio, uma dessas crianças que a gente vê em anúncios. Pelo jeito deve ter uns três ou quatro anos, não mais que isso. Ela está vestida num desses macaquinhos de flanela, com florzinhas azuis e vermelhas e uma malha creme por baixo. Calçando um tênis transadíssimo nas discretas cores amarelo, vermelho e azul, o que nos mostra que a mocinha não é apenas novinha, mas moderninha também. O velhinho tem um tipo bem italiano. O boné cinza é típico desses senhores que a gente vê passeando pelo Bixiga nos domingos à tarde. Estatura mediana, cabelos e bigodes branquinhos, rosto e mãos enrugadas que traem uma idade bem avançada. Paletó marrom e calça cinza, ambos de lã, malha creme, abotoada até o último botão, como faz todo senhor que se preze. Embaixo da malha uma camisa azul mas bem azul mesmo, que destoa de todo o conjunto. O que prova que o cavalheiro e a mocinha apreciam cores fortes. Pela roupa que os dois estão vestindo e pela carinha rosada dela, deve estar fazendo muito frio. Fato que o ar enevoado e cinzento do jardim, que está atrás deles, vem a comprovar. Os dois estão sentados num balanço de madeira de cor verde, desses que cabem apenas duas pessoas e que são bastante comuns em quintais, varandas e jardins de casas de classe média, classe média alta. Ela está comodamente estirada. Com a cabeça entre o ombro e a barriga do velhinho e os pés apoiados numa almofada de crochê de cor creme. Nas mãos ela traz um livro de histórias cheio de desenhos coloridos. Livro esse que, olhando atentamente, você verá que se trata da história da Bela Adormecida. O que, aliás, é muito engraçado, porque enquanto a bela conta a história da Bela Adormecida, o velho é que adormeceu. Ele dorme a sono solto. Com uma mão envolta na dela e a outra apoiada sobre sua própria perna direita, na altura do joelho. Ambos à sua maneira estão sonhando. Ele sonha dormindo, ela sonha acordada. O jardim atrás, ligeiramente desfocado, complementa esse clima de sonho. Atrás do balanço verde, onde os dois estão sentados, vê-se uma cerca de madeira também verde, só que num tom mais escuro, que os decoradores costumam chamar de verde-império. Cor, aliás, mais que apropriada para servir de fundo a essa pequena princesa encantada por sua história. Por trás do vazado da cerca verde de madeira, podemos ver um jardim bem amplo. O que vem a reforçar a idéia que se trata de uma família de posses. Porque ou eles têm uma casa com um jardim bem amplo na cidade ou têm uma ampla casa de campo, o que nos dias de hoje não é luxo para qualquer um. O verde lá fora, combinando com o verde-cana do balanço e o verde-império do alambrado, cria um clima gostoso no ambiente, mostrando que a dona da casa é mais cuidadosa na escolha das cores que a mocinha e seu cavalheiro adormecido. A presença de plantas tão variadas e viçosas nos permite pensar que ou a família tem um jardineiro aplicado ou alguém na família gosta muito de jardinagem. Mas isso já é divagação demais. E já basta a menina que está divagando no colo do avô. Isso mesmo: do avô. Por que o velho que você está vendo só pode ser o avô dela. Pela intimidade com que ela está comodamente instalada no colo dele, percebe-se que não pode ser visita, pessoa de cerimônia. E sim alguém bem chegado, alguém da família. Para um estranho ouvir essa história contada por uma criaturinha tão linda seria uma novidade excitante, que dificilmente o faria cair no sono. E se não fosse por isso, um estranho também não cairia no sono, pelo menos por dever de educação. Resistiria bravamente até a Bela Adormecida acordar. Além disso, é só olhar para a roupa caseira que ele está usando para perceber que não é alguém que foi fazer uma visita. É pessoa da casa mesmo, pai não é. Ele é muito velhinho para ser o pai dela. E pouco provavelmente seria um tio. Tanto pela idade quanto pela disponibilidade e paciência. Tio dá doces, presentes, mas ouvir histórias intermináveis, contadas por uma narradora que de vez em quando divaga, tio não faz. Só pode ser mesmo um avo ouvindo pela milésima vez a mesma história. Que para ele deve ser sempre igual e para ela deve ser sempre diferente. Ela, por sua vez, não deve se importar que seu ouvinte durma. Afinal ela só quer colo e aquela mão terna, enrugada e querida em volta da sua cintura pequenina. Mesmo desatento ele está dando a ela seu tempo e seu carinho sonolento. Porque o balanço de jardim pode ser gostoso de sentar. Mas como você pode ver não é o local mais confortável para se dormir. Principalmente num dia frio como esse, num descampado de uma varanda. Mas o fato é que ele não sente a dureza do balanço porque dorme e ela, igualmente, não sente a dureza da madeira e a frieza do tempo por vários motivos: primeiro porque sonha e no sonho não há desconforto ou frio. E segundo porque ela tem a barriga do avô como travesseiro, o braço dele como edredom e uma almofada como encosto para seus pés e seu tênis multicolorido. Juntos os dois, ali na varanda, vivem um momento que ela vai se lembrar sempre e ele não vai se lembrar de nada. Inclusive nada da história. Por isso que ela vai ter que contar e recontar essa história para o avô centenas de vezes. Principalmente para reviver os trechos que ele perdeu com seus cochilos. Assim como você vai ter que ler e reler muitas vezes esse texto até conseguir enxergar toda a beleza e ternura contidas nessa cena."
palavras = palavras.translate(str.maketrans('', '', string.punctuation)).split()

for i in palavras:
    if len(i) <= 3:
        palavras.remove(i)

chances = 0
print('+=' * 10, 'ATENÇÃO, FOI GERADA UMA PALAVRA ALEATÓRIA, TENTE ADIVINHAR', '+=' * 10)
palavras = random.choice(palavras).upper()
escolhida = removerAcentosECaracteresEspeciais(palavras)
escolhida1 = escolhida2 = escolhida
palavradigitada = []

print()
print('JOGO DA FORCA\n')
print(f'A palavra escolhida tem {len(escolhida)} letras')
print('VAMOS COMEÇAR')
print('VOCÊ TEM 5 CHANCES\n')

for i in escolhida1:
    print('_ ', end='')
print()

while True:
    user = str(input('DIGITE UMA LETRA: ')).upper().split()[0]
    print()
    if user not in escolhida:
        chances += 1
        if chances == 5:
            print('INFELIZMENTE VOCÊ PERDEU, TENTE NOVAMENTE =)')
            print(f'A PALAVRA ERA {escolhida2}')
            break
        if chances > 0:
            print(f'Você ainda tem {5 - chances} chances')
    if user in escolhida:
        print(f'Voce achou a letra {user}')
        palavradigitada.append(user[:])
        escolhida = str(escolhida).replace(user, '')
        for i in escolhida1:
            if i not in palavradigitada:
                escolhida1 = str(escolhida1).replace(i, '_ ')
        print(f'{escolhida1}\n')

    escolhida1 = escolhida2

    if len(escolhida) == 0:
        print('PARABENS VOCE VENCEU')
        print(f'A PALAVRA É {escolhida2}')
        break