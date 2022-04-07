from django.shortcuts import render

# Create your views here.
context = {
    'book1': {
        'name': "三国演义",
        'person': '诸葛亮',
    }
}


def index(request):
    return render(request, "book/index.html", context)
