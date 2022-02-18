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