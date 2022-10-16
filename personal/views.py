from django.shortcuts import render, HttpResponse
from jinja2 import Environment, select_autoescape, FileSystemLoader



def Env_setUp(template_path):
    return Environment(
        loader = FileSystemLoader(str(template_path)),
        autoescape = select_autoescape()
    )

def index(request, n):
    env = Env_setUp("templates/personal")
    print(f'number : {n}')
    template = env.get_template("index.html").render(**{"number" : int(n)})
    print(template)
    return HttpResponse(template)

def post(request):
    env = Env_setUp("templates/personal")
    template = env.get_template("post.html").render()
    print(template)
    return HttpResponse(template)
    # return render(request, 'personal/post.html')