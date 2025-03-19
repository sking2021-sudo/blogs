from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        "id":1,
        "title":'Let\'s explore python',
        "content":'Python is interpreted ajksdhsjdnjknahfsnafknsk',

    },
    {
        "id":2,
        "title":'Let\'s explore javascript',
        "content":'Javascript is interpreted ajksdhsjdnjknahfsnafknsk',
    },
    {
        "id":3,
        "title":'Django the best framework',
        "content":'Django used by almost every big tech hjfsrjagkbcbgashjfbchjasgf',
    },
]
#function based views
def home(request):
    html = ""
    for post in posts:
        html += f''' 
            <div>
                <h1>{post['id']} - {post['title']}</h1>
                <p>{post['content']}</p>
            </div>
        '''
    return HttpResponse(html)



    
