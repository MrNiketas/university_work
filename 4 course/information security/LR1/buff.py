def get_bigramm(message):
    bi = []
    i = 0
    print("Исходное сообщение: ", message)
    mess = message.replace(" ","")
    while i < (len(mess)-1):

        buff = mess[i]+mess[i+1]
        if(mess[i]==mess[i+1]):
            buff = mess[i]+"я"
            i += 1
        else: i+=2
        bi.append(buff)

        if i == len(mess)-1:
            buff = mess[i] + "я"
            bi.append(buff)
    print("Биграмма: ", bi)
    return bi