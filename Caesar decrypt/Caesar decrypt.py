caesar = input("the caesar say: ")
for i in range(0, 26, 1):
    print(f"\ncaesar for {i}: ", end = "")
    for j in range(0, len(caesar), 1):
        if(ord(caesar[j]) >= 65 and ord(caesar[j]) <= 90):
            if(ord(caesar[j]) + i > 90):
                print(chr(ord(caesar[j]) + i - 26), end = "")
            else:
                print(chr(ord(caesar[j]) + i), end = "")
        elif(ord(caesar[j]) >= 97 and ord(caesar[j]) <= 122):
            if(ord(caesar[j]) + i > 122):
                print(chr(ord(caesar[j]) + i - 26), end = "")
            else:
                print(chr(ord(caesar[j]) + i), end = "")
        else:
            print(caesar[j], end = "")