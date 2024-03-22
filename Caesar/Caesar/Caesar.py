
def generate_shifts(keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifts = []
    for letter in keyword:
        # Находим позицию каждой буквы ключевого слова в алфавите и добавляем в список сдвигов
        shifts.append(alphabet.index(letter.lower()))
    return shifts

def caesar_cipher_encrypt(text, keyword):
    shifts = generate_shifts(keyword)
    encrypted_text = ''
    alphabet = 'catworldsun'
    for i, letter in enumerate(text.lower()):
        if letter in alphabet:
            # Вычисляем новую позицию буквы с учётом сдвига
            shifted_position = (alphabet.index(letter) + shifts[i % len(shifts)]) % len(alphabet)
            encrypted_text += alphabet[shifted_position]
        else:
            # Если символ не является буквой, добавляем его без изменений
            encrypted_text += letter
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, keyword):
    shifts = generate_shifts(keyword)
    decrypted_text = ''
    alphabet = 'catworldsun'
    for i, letter in enumerate(encrypted_text.lower()):
        if letter in alphabet:
            # Вычисляем оригинальную позицию буквы, отменяя сдвиг
            shifted_position = (alphabet.index(letter) - shifts[i % len(shifts)]) % len(alphabet)
            decrypted_text += alphabet[shifted_position]
        else:
            decrypted_text += letter
    return decrypted_text

# Пример использования
keyword = "key"
text = "My name is Andrey"
encrypted = caesar_cipher_encrypt(text, keyword)
decrypted = caesar_cipher_decrypt(encrypted, keyword)

print(f"Original: {text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
