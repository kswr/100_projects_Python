import string

alp = string.ascii_lowercase

key = {value: key for key, value in enumerate(alp)}
value = {key:value for key, value in enumerate(alp)}

def encoding(string):
    en_string = []
    for i in string:
        en_string.append(key[i])
    return en_string

def decoding(encoded):
    string = ''
    for i in encoded:
        string += value[i]
    return string

encoded_lab = encoding('labrador')
print(encoded_lab)

decoded_lab = decoding(encoded_lab)
print(decoded_lab)
