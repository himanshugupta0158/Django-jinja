from email.mime.image import MIMEImage
import os
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from django_jinja.settings import *

from django.shortcuts import render, HttpResponse
from jinja2 import Environment,select_autoescape, FileSystemLoader

from django_jinja.jinja2 import environment
from django.middleware.csrf import get_token


def Env_setUp(template_path):
    """
    Using this when using flask and jinja
    this one does not need much changes.
    """
    return Environment(
        loader = FileSystemLoader(str(template_path)),
        autoescape = select_autoescape()
    )

def Env_setUp2(template_path):
    """
    Use this when using Django and jinja
    For this :
    1.> create jinja2.py file in root directory and put requred code in it 
    2.> makes changes in template of settings.py
    3.> from root_directory.jinja2 import environment <- use this environment instead of ENvironment else some code will not work.
    """
    return environment(
        loader = FileSystemLoader(str(template_path)),
        autoescape = select_autoescape()
    )


def index(request, n):
    csrf_token = get_token(request)
    env = Env_setUp2("templates/personal")
    print(f'number : {n}')
    template = env.get_template("index.html").render(**{"number" : int(n)})
    # print(template)
    return HttpResponse(template)

def post(request):
    csrf_token = get_token(request)
    env = Env_setUp2("templates/personal")
    template = env.get_template("post.html").render(**{"email" : "himashugupta12369@gmail.com", "csrf_token" : csrf_token})
    # print(template)
    return HttpResponse(template)
    # return render(request, 'personal/post.html')



def sendEmailCode(request):
    """
    sending gmail msg
    """
    email = request.POST.get("Email")
    print(email, type(email))
    if not email :
        email ="himanshugupta.ongraph@gmail.com"
    print(f'Email : {email}')
    email_from = EMAIL_HOST_USER
    subject = "Sending HTML to Gamil"
    body_html = render_to_string(
        "personal/email_code_template.html", 
        {"otp": int(123456), "time": "16-10-2022 03:30:00"}
    )
    msg = EmailMultiAlternatives(
        subject,
        body_html,
        from_email = email_from,
        to = [
            email,
        ]
    )
    msg.mixed_subtype = "related"
    msg.attach_alternative(body_html, "text/html")
    img_dir = str(BASE_DIR) + '/static'
    image = "Mascot.png"
    file_path = os.path.join(img_dir, image)
    print(file_path)
    with open(file_path, "rb") as f:
        print(f)
        img = MIMEImage(f.read())
        img.add_header("Content-ID", "<{name}>".format(name=image))
        img.add_header("Content-Disposition", "inline", filename=image)
    msg.attach(img)

    try:
        msg.send()
    except Exception as e:
        print(str(e))
        return False
    env = Env_setUp2("templates/personal")
    template = env.get_template("post.html").render(**{"message" : "message sent"})
    print(template)
    return HttpResponse(template)
