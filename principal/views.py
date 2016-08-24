from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from .forms import CommentForm
from .models import Comment
# Create your views here.


class IndexView(TemplateView):

	template_name = 'index.html'

	def post(self, request, *args, **kwargs):
		request.session['name'] = request.POST['name']
		return redirect('/inicio/')

class InicioView(TemplateView):
	def get(self, request, *args, **kwargs):
		if request.session.get('name'):
			comments = Comment.objects.all()
			dic = {
				'name' : request.session['name'],
				'form' : CommentForm(),
				'comments' : comments
			}				
			return render(request, 'inicio.html', dic)
		else:
			return redirect('/')

	def post(self, request, *args, **kwargs):
		Comment.objects.create(
				user = request.session['name'],
				comment = request.POST['comment']	
			)
		return redirect('/inicio/')


@csrf_exempt
def create_comment(request):	
	Comment.objects.create(
			user = request.POST['user'],
			comment = request.POST['comment']
		)
	response = JsonResponse({'user' : request.POST['user'],
							'comment' : request.POST['comment']})
	return HttpResponse(response.content)