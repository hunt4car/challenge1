def main():
    message = input("enter a message to be decoded")
    messageLength = len(message)

    print("the message is", messageLength)

    for i in range(0,messageLength,2):
        print(chr(int(message[i:i+2])),end = "")

main()
