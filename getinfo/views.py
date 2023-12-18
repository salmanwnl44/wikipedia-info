from django.shortcuts import render
import wikipedia

def index(request):
    return render(request, 'index.html')

def getWiki(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        try:
            # Fetch Wikipedia content for the given query
            summary = wikipedia.page(query).content
            context = {"output": summary}
            return render(request, 'index.html', context)

        except wikipedia.exceptions.PageError:
            error_message = f"Sorry, I couldn't find a page for '{query}'."
            context = {"error": error_message}
            return render(request, 'index.html', context)

