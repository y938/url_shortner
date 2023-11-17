from django.shortcuts import render
import pyshorteners
from django.http import JsonResponse

def url_shortner(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        bitly_shortener = pyshorteners.Shortener(api_key="your bitly api")  # Replace with your Bitly API key

        try:
            short_url = bitly_shortener.bitly.short(long_url)
            return JsonResponse({'short_url': short_url})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return render(request, 'index.html')