import pyshorteners

long_url = input("Input url that u want to shorten: ")
bitly_shortner = pyshorteners.Shortener(api_key="your bitly api key")
short_url = bitly_shortner.bitly.short(long_url)

print("short url: {}".format(short_url))