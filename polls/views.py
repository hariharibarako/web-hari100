from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

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
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'polls/detail.html', {'topic':topic})

def articles(request):
    
    topic_list = Topic.objects.all().order_by('-pub_date')
    for topic in topic_list:
        if len(topic.topic_text) > 100:
            topic.topic_text = topic.topic_text[:100] + '.'*5
    
    ranking_list = Topic.objects.all().order_by('-nice')[:3]
    rank = 1
    for topic in ranking_list:
        topic.title = "第" + str(rank) + "位：" + topic.title + " " 
        
    context = {
        'topic_list': topic_list,
        'ranking_list': ranking_list
    }
    return render(request, 'polls/articles.html', context)

def profile(request):
    
    topic_list = Topic.objects.all().order_by('-pub_date')
    for topic in topic_list:
        if len(topic.topic_text) > 100:
            topic.topic_text = topic.topic_text[:100] + '.'*5
    
    ranking_list = Topic.objects.all().order_by('-nice')[:3]
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