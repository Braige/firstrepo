"""
it takes aastring as a inout and the string is going t be a whatsapp message 
if the string contains the words product then the bot should reply with these are our products 
then if the message contains the 
word hours then it replys wiht the words "heres our avalability" 
if the message contians facebook OR insta OR tikTOk it replys here is our social media 
otherwise it says I dont know how to respond to that question 
"""

#input ? message is our input


#Keywords here 
keywords = ["product","hours","facebook","tiktok","instagram"]


#bot response (output)
product = "these are our products"
hours = "heres our avalbility"
social_media = "here is our social media link"
unknown = "i dont know how to respond to that"

while True: 
    message = input("send message: ")

    if not "exit" in message and not "product" in message and not "hours" in message and not any(k in message for k in keywords):
        print(unknown)
    if "product" in message:
        print(product)
    if "hours" in message:
        print(hours)
    if any(k in message for k in keywords[2:4]):
        print(social_media)

    if "exit" in message:
        break
git --version
