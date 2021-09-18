def decode_caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')

# If your argument --file is stored in the variable args, you can read the file you've passed to your script this way:
opened_file = open('13.txt')
encoded_text = opened_file.read()  # read the file into a string
print(decode_caesar_cipher(encoded_text, -13))
opened_file.close()  # always close the files you've opened

