from django.shortcuts import render


posts = [
    {
        'author': 'Krisztian Markella',
        'title': 'Blog Post 1',
        'content': "First Blog Post",
        'date_posted': 'August 28, 2023',
    },

    {
        'author': 'Christian Markella',
        'title': 'Blog Post 2',
        'content': "Second Blog Post",
        'date_posted': 'August 29, 2023',
    },
    
    {
        'author': 'Mark Markella',
        'title': 'Blog Post 3',
        'content': "Third Blog Post",
        'date_posted': 'August 30, 2023',
    },
]

def home(request):
    context = {
        'posts': posts,
    }
    return render(request=request, template_name='blog/home.html', context=context)

def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
