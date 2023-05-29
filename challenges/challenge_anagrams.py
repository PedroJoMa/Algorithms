def is_anagram(first_string, second_string):
    # Colocando as strings em minúsculo
    lower_first_s = first_string.lower()
    lower_second_s = second_string.lower()

    first_word_ordered = ordenar_palavra(lower_first_s)
    second_word_ordered = ordenar_palavra(lower_second_s)
    bool = first_word_ordered == second_word_ordered
    # Verifica se os parametros estão preenchidos
    if not first_word_ordered or not second_word_ordered:
        return (first_word_ordered, second_word_ordered, False)

    # Comparando o tamanho das palavras
    if len(first_word_ordered) != len(second_word_ordered):
        return (first_word_ordered, second_word_ordered, False)

    return (first_word_ordered, second_word_ordered, bool)


def ordenar_palavra(palavra):
    # Converter a palavra em uma lista de caracteres
    caracteres = list(palavra)
    # Iterar sobre a lista de caracteres
    for i in range(1, len(caracteres)):
        chave = caracteres[i]
        j = i - 1
        # Mover os elementos maiores que a chave para a direita
        while j >= 0 and caracteres[j] > chave:
            caracteres[j + 1] = caracteres[j]
            j -= 1
        # Inserir a chave na posição correta
        caracteres[j + 1] = chave
    # Converter a lista de caracteres de volta para uma string
    palavra_ordenada = ''.join(caracteres)
    return palavra_ordenada
