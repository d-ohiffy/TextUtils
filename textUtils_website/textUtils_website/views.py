from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



def analyze(request):
    # Get Text
    djtext = request.POST.get('text','defualt')

    # Get Checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    #charCounter = request.GET.get('charCounter','off')
    extraspaceRemover = request.POST.get('extraspaceRemover','off')
    # the first value will be displayed if the value is passed, else second value will be displayed
    original = djtext
    analyzed = ""
    actions = ''
    count = 0
    for char in djtext:
        count+=1
        
    if removepunc=='on':
        analyzed = ""
        punctuation = '''!()-[]{};:'"\,<>.?@#$%^&*_~'''
        for char in djtext:
            if char in punctuation:
                continue
            else:
                analyzed+= char
        djtext = analyzed

        actions += '\nRemoved Punctuations'
    
    if fullcaps=='on':
        analyzed = djtext.upper()
        djtext = analyzed
        actions += '\nCapatalize Text'

    if newlineremover=='on':
        analyzed = ''        
        for char in djtext:
            if char!='\n' and char !='\r':
                analyzed+=char
        djtext = analyzed
        actions += '\nRemove New Line'
   
    if extraspaceRemover=='on':
        analyzed = ''
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analyzed+=char
        djtext = analyzed
        actions += '\nRemove Extra Space'
    
    params = {'original_text': original, 'purpose':actions, 'analyzed_text':analyzed, 'total_Char': count}

    if removepunc=='off' and extraspaceRemover!='on' and newlineremover!='on' and fullcaps!='on':
        alert = {'message':'Please Select the following option'}
        return render(request, 'index.html',alert)

    return render(request, 'analyze.html', params)




    


