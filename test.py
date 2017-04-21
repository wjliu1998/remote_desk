f = open("user", "r+")
allLines = f.readlines()
for eachline in allLines:
    (username, iv, ciphertext) = eachline.split(":")
    print username
    print iv
    print ciphertext
