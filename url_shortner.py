import pyshorteners
long_url = input("Enter the URL to shorten: ")

#TinyURL shortener service
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("Your URL has been shortened successfully....")
print("The Shortened URL is: " + short_url)