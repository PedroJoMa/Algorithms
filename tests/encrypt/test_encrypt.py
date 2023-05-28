from challenges.challenge_encrypt_message import encrypt_message
import pytest


wrong_key = "trybe"
odd_key = 3
pair_key = 4
out_key = 12
message = "decola"
wrong_message = 2


def test_encrypt_message():
    # Retorna um erro para uma chave de tipo inválido.
    with pytest.raises(TypeError):
        encrypt_message(message, wrong_key)

    # Retorna um erro para uma messagem de tipo inválido.
    with pytest.raises(TypeError):
        encrypt_message(wrong_message, odd_key)

    # Retorna uma string criptografada com uma chave ímpar
    assert encrypt_message(message, odd_key) == "ced_alo"

    # Retorna uma string criptografada com uma chave par
    assert encrypt_message(message, pair_key) == "al_oced"

    # Retorna a string criptografada com uma chave fora do escopo
    assert encrypt_message(message, out_key) == "aloced"
