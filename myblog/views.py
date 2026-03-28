from django.shortcuts import render

def post_list(request):
    template_name = 'myblog/post_list.html'
    
    saludo = 'hola'
    
    context ={
        'saludo': saludo
    }
    
    return render(request, template_name, context)
