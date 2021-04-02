from django.http import HttpResponse
from  django.shortcuts import render

#vid6
# def index(request):
#     return HttpResponse('''<h1>hello harry</h1><a href="https://www.geeksforgeeks.org/python-programming-language/">gfg</a>''')

# def about(request):
#     return HttpResponse("abou hello harry bhai")

# def rempunc(request):
#     djtext=request.GET.get('text' ,'default') #get the text
#     print(djtext)
#     return HttpResponse("remove punctuation")
# def capfir(request):
#     return HttpResponse("capitalize first")
# def newrem(request):
#     return HttpResponse("new line remover")
# def remspa(request):
#     return HttpResponse("remove space")
# def charc(request):
#     return HttpResponse("charcount")

# def index(request):
#     return HttpResponse("Home")
# def index(request):
#   params={'name':'rimi' , 'p':'mars'}
#   return render(request , 'index.html' , params)
#//

def index(request):
    return render(request, 'index.html')

def analyze(request):
     djtext=request.GET.get('text' ,'default') #get the text
     removepunc=request.GET.get('rempunc' , 'off')
     caps = request.GET.get('fullcaps', 'off')
     newlineremover =request.GET.get('newlinerem', 'off')
     extraspacerem = request.GET.get('spacerem', 'off')

     # print(djtext)
     # print(removepunc)
     # return HttpResponse("remove punctuation")
     if(removepunc == 'on'):
        punc ='''!@#$%^&*;:>'"<"?/}{[]'''
        analyzed=""
        for char in  djtext:
            if char not in punc:
               analyzed+=char
        params = {'purpose': 'Remove punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
     elif(caps == 'on'):
         analyzed = ""
         for char in djtext:
             analyzed += char.upper()
         params = {'purpose': 'capitalize text', 'analyzed_text': analyzed}
         return render(request, 'analyze.html', params)
     elif(newlineremover =='on'):
         analyzed = ""
         for char in djtext:
             if char !='\n':
                analyzed += char
         params = {'purpose': 'new line remover', 'analyzed_text': analyzed}
         return render(request, 'analyze.html', params)
     elif(extraspacerem =='on'):
         analyzed = ""
         for index, char in enumerate(djtext):
             if not(djtext[index] ==" " and djtext[index+1] ==" "):
                 analyzed += char
         params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
         return render(request, 'analyze.html', params)
     #charcount
     else:
        return HttpResponse("Error")





