from winreg import QueryValue
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.
from .models import Question, Choise

def index(request):
    questions = Question.objects.all()
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #Entregando un objeto por medio de una consulta
    #output = ', '.join([q.question_text for q in latest_question_list])
    #output = ', '.join([q.question_text for q in questions])
    template = loader.get_template('polls/index.html')
    context = {
        'mensaje': "Lista encuestas",
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse(output)

#def hola_dos(request):
 #   return HttpResponse("hola Mundo/2")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    #return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)
    context = {
        'mensaje': 'Detalle de la encuenta',
        'question': question
    }
    return render(request, 'polls/detail.html',context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
