from django.shortcuts import render

posts = [
    {
        "author": "Morris",
        "title": "Blog Post1",
        "content": "First Post Content",
        "date_posted": "August 27, 2024",
    },
    {
        "author": "Sindet",
        "title": "Blog Post2",
        "content": "Second Post Content",
        "date_posted": "August 28, 2024",
    },
    {
        "author": "Chepkurui",
        "title": "Blog Post3",
        "content": "Third Post Content",
        "date_posted": "August 29, 2024",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
