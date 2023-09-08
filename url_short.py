import pyshorteners

url = input("enter Url for shortening: \n")

print("URL After Shortening : - ", pyshorteners.Shortener().tinyurl.short(url))

input("Press Enter to exit")