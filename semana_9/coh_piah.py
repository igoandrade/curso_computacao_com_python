import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:\n")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    df = []
    for i in range(6):
        df.append(abs(as_a[i] - as_b[i]))
    grau_similaridade = sum(df)/len(df)
    return grau_similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_sentencas = separa_sentencas(texto)

    lista_frases = []
    for sentenca in lista_sentencas:
        lista_frases += separa_frases(sentenca)
    
    lista_palavras = []
    for frase in lista_frases:
        lista_palavras += separa_palavras(frase)

    total_palavras = len(lista_palavras)

    tamanho_palavras = [len(palavra) for palavra in lista_palavras]

    wal = sum(tamanho_palavras)/total_palavras
    ttr = n_palavras_diferentes(lista_palavras)/total_palavras
    hlr = n_palavras_unicas(lista_palavras)/total_palavras
    
    tamanho_sentencas = [len(sentenca) for sentenca in lista_sentencas]
    sal = sum(tamanho_sentencas)/len(tamanho_sentencas)
    
    
    sac = len(lista_frases)/len(lista_sentencas)
    pal = sum(tamanho_palavras)/len(lista_frases)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_graus_similaridade = [] 
    for texto in textos:
        ass_x = calcula_assinatura(texto)
        grau_similaridade = compara_assinatura(ass_cp, ass_x)
        lista_graus_similaridade.append(grau_similaridade)
    minimo = min(lista_graus_similaridade)
    id_minimo = lista_graus_similaridade.index(minimo)+1
    return id_minimo
    

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    id_minimo = avalia_textos(textos, ass_cp)
    print(f"\nO autor do texto {id_minimo} está infectado com COH-PIAH")


if __name__=="__main__":
    main()