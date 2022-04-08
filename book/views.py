from django.shortcuts import render

context = {
    "person": {
        "name": "诸葛亮",
        "detail": "军师",
    }
}


# Create your views here.
def index(request):
    return render(request, 'book/index.html', context)
