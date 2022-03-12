from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Q

from .models import Topic


def index(request):
    topic_list = Topic.objects.order_by('-pub_date')[:5]
    context = {
        'topic_list': topic_list,
    }
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, topic_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question dows not exist.")
    if request.method == "POST":
        nice = request.POST['nice']
        print('押されました！')

    topic = get_object_or_404(Topic, pk=topic_id)

    ranking_list = Topic.objects.all().order_by('-nice')[:5]
    rank = 1
    for ranking_topic in ranking_list:
        ranking_topic.title = "第" + str(rank) + "位：" + ranking_topic.title
        rank += 1
    
    context = {
        'topic': topic,
        'ranking_list': ranking_list
    }

    return render(request, 'polls/detail.html', context)

def articles(request):
    if request.method == "POST":
        search_word = request.POST['search_word']
        topic_list = Topic.objects.filter(Q(title__contains=search_word) | Q(topic_text__contains=search_word)).distinct()
        # topic_list = Topic.objects.all().order_by('-pub_date')
    else:
        topic_list = Topic.objects.all().order_by('-pub_date')

    for topic in topic_list:
        if len(topic.topic_text) > 100:
            topic.topic_text = topic.topic_text[:100] + '.'*5
    
    ranking_list = Topic.objects.all().order_by('-nice')[:5]
    rank = 1
    for topic in ranking_list:
        topic.title = "第" + str(rank) + "位：" + topic.title
        rank += 1
    
    for topic in topic_list:
        print(topic, topic.id)
        
    context = {
        'topic_list': topic_list,
        'ranking_list': ranking_list
    }
    return render(request, 'polls/articles.html', context)

def articles_genre(request, topic_genre):
    # メインのトピックリスト 
    topic_list = Topic.objects.filter(genre=topic_genre).order_by('-pub_date')
    for topic in topic_list:
        if len(topic.topic_text) > 100:
            topic.topic_text = topic.topic_text[:100] + '.'*5
    
    # いいねランキングのトピックリスト
    ranking_list = Topic.objects.all().order_by('-nice')[:5]
    rank = 1
    for topic in ranking_list:
        topic.title = "第" + str(rank) + "位：" + topic.title 
        rank += 1
        

    topic_gen = topic_genre
        
    context = {
        'topic_list': topic_list,
        'ranking_list': ranking_list,
        'topic_gen': topic_genre
    }
    return render(request, 'polls/articles.html', context)


def profile(request):
    
    topic_list = Topic.objects.all().order_by('-pub_date')
    for topic in topic_list:
        if len(topic.topic_text) > 100:
            topic.topic_text = topic.topic_text[:100] + '.'*5
    
    ranking_list = Topic.objects.all().order_by('-nice')[:5]
    rank = 1
    for topic in ranking_list:
        topic.title = "第" + str(rank) + "位：" + topic.title + " "
    
    profile_text = "IT業界の片隅にいるネコです。昔はSEや会計士をやってました。好きなフレームワークはDjango、Reactです。たまにSwiftも書きます。"
    email = "1morimorimorita@gmail.com"
    
    context = {
        'profile_text': profile_text,
        'email': email,
        'topic_list': topic_list,
        'ranking_list': ranking_list
    }
    return render(request, 'polls/profile.html', context)