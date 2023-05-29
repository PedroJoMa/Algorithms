def is_palindrome_recursive(word, low_index, high_index):
    # Caso base: o index da palavra tem um caractere ou 2 caracteres iguais
    if high_index == 1 or high_index == 0:
        return True
    # Caso base: os caracteres inicial e final são diferentes
    elif not word or word[low_index] != word[-1]:
        return False
    # Chamada recursiva: verifica o palíndromo sem o primeiro e último caracter
    else:
        slice_word = word[1:-1]
        return is_palindrome_recursive(slice_word, 0, len(word) - 1)
