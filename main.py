from framework.rend import render
from framework.wsgi import Framework
from framework.urls import Url
from framework.view import View
from framework.response import Response



class IndexView(View):

    def get(self, request):
        return Response(body=render('index.html', title='Main page', body='Главная страница'))

    def post(self, request):
        return 'POST SUCCESS'

class AboutView(View):

    def get(self, request):
        return Response(body=render('index.html', title='About page', body='About page'))

    def post(self, request):
        return 'POST SUCCESS'

class ContactsView(View):

    def get(self, request):
        return Response(body=render('contacts.html', title='Contacts page', body='Контакты'))

    def post(self, request):
        return Response(body=render('contacts.html', title='Contacts page', body='Контакты', data=request.data))


urls = [
    Url('', IndexView),
    Url('index', IndexView),
    Url('about', AboutView),
    Url('contacts', ContactsView),
]


app = Framework(urls)
