import requests
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CallbackForm
from .models import News, Events


def contacts(request):
    if request.method == "POST":
        Callback = CallbackForm(request.POST)
        if Callback.is_valid():
            object = Callback.save()
            telegram_bot_sendtext("{} {}".format(object.name,object.phone))
        return render(request, "Html/contacts.html", {"title" : "Ваша заявка успешно отправлена."})
    else:
        Callback = CallbackForm()
    return render(request, "Html/contacts.html", {'Callback': Callback})


def mainpage(request):
    return render(request,'Html/index.html')

def telegram_bot_sendtext(bot_message):

   bot_token = '1905580144:AAG54VgDmir7Tm9Z8jhH5xy92g6wqHcLpjY'
   bot_chatID = '714097504'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()

def news(request):
    news = News.objects.all().order_by("-created_at")
    return render(request,'Html/news.html',{"News" : news })

def events(request):
    events = Events.objects.all().order_by("-created_at")
    return render(request,'Html/events.html',{"Events" : events })


def post_list(request):
    posts = News.objects.all().order_by("-created_at")
    paginator = Paginator(posts, 4)
    # 5  на каждой странице
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        posts = paginator.get_page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        posts = paginator.get_page(paginator.num_pages)
    print(posts)
    return render(request,
                  'Html/news.html',
                  {'page': page,
                   'News': posts})


def post_list_events(request):
    posts = Events.objects.all().order_by("-created_at")
    paginator = Paginator(posts, 4)
    # 5  на каждой странице
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        posts = paginator.get_page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        posts = paginator.get_page(paginator.num_pages)
    print(posts)
    return render(request,
                  'Html/events.html',
                  {'page': page,
                   'Events': posts})






