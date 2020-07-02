import pyaes

# A 256 bit (32 byte) key
key = "KvCCPflL7IfGHEhbu4yfKQYYrzdGi25r"
plaintext = 'bJMPEckryvRRKT1fhEOHlhZJlhRJvcvQWpsmkHUlNPwQReFy22fu0KQiU9AbvW003HFmx3pPbu8dPX9hQykuRA=='

# key must be bytes, so we convert it
key = key.encode('utf-8')

aes = pyaes.AESModeOfOperationCTR(key)    
ciphertext = aes.encrypt(plaintext)

# show the encrypted data
f = open("demofile3.txt", "wb")
f.write(ciphertext)
f.close()

# DECRYPTION
# CRT mode decryption requires a new instance be created
aes = pyaes.AESModeOfOperationCTR(key)

# decrypted data is always binary, need to decode to plaintext
decrypted = aes.decrypt(ciphertext).decode('utf-8')

# True
print (decrypted == plaintext)