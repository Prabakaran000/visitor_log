from django.shortcuts import render, redirect
from .models import Visitor
from .forms import VisitorForm

def visitors_log(request):
    visitors = Visitor.objects.all()
    query = request.GET.get('q')
    if query:
        visitors = visitors.filter(name__icontains=query)
    return render(request, 'visitors_log.html', {'visitors': visitors, 'query': query})


def add_visitor(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitors_log')
    else:
        form = VisitorForm()
    return render(request, 'add_visitor.html', {'form': form})


def admin(request):
    return redirect('/admin/')
