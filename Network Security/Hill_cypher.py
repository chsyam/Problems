from email import message


keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]

def getKeyMatrix(key):
    ind = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[ind])%65
            ind += 1

def encrypt(messageVector,keyMatrix):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] %26

def HillCipher(message,key):
    getKeyMatrix(key)

    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
    
    encrypt(messageVector,keyMatrix)

    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))

    return "".join(CipherText)

message = input() # ACT
key = input() # GYBNQKURP

encrypted = HillCipher(message,key)
print("Encrypted Text is : ",encrypted)

# source : Greeks For Greeks