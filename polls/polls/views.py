import select
from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Question, Choice




def detail(request, question_id):
    question = get_object_or_404(pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

    # try:
    #     question = Question.object.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("질문이 없습니다.")
    # return render(request, 'polls/detail.html',{'question':question})
    # return HttpResponse("당신은 %s 질문을 보고 있습니다." % question_id)

def index(request):
    lastest_question_list = Question.objects.order_by('pub_data')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':lastest_question_list
    }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    # output = ','.join([q.question_text for q in lastest_question_list])
    # return HttpResponse(output)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # 질문 투표 양식을 다시 표시
        return  render(request, 'polls/detail.html', {'question':question,'error_message':"당신은 선택을 하지 않았습니다.",})
    else:
        selected_choice.vote += 1
        selected_choice.save()
    return  HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def results(request, question_id):
    response = "당신은 %s 질문의 결과를 보고 있습니다."
    return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("당신은 %s 질문에 투표하고 있습니다." % question_id)

# Create your views here.
