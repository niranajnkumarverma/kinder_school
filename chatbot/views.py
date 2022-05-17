from django.shortcuts import render
from django.views.generic import TemplateView
from chatbot.chat import  chat


class mainpage(TemplateView):
	Template_name="user/chatbot.html"

	def get(self,request):
		return render(request,self.Template_name)

	def post(self,request):
		if request.method == 'POST':
			user = request.POST.get('input',False)
			context={"user":user,"bot":chat(request)}
			
		return render(request,self.Template_name,context)