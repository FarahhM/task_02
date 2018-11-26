from django.shortcuts import render


def func1(request):
	context={
	"msg":"Hello World!"
	}
	return render(request, 'myfile.html', context)

# Create your views here.
