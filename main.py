import pyshorteners

long_url = input("Input url that u want to shorten: ")
bitly_shortner = pyshorteners.Shortener(api_key="9993696dd9a1d0ffc7524025ea821372c812a045")
short_url = bitly_shortner.bitly.short(long_url)

print("short url: {}".format(short_url))