from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NameForm
from .models import UserName


def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # Сохраняем имя в базу данных
            user_name = form.save()
            messages.success(request, f'Привет, {user_name.name}!')
            return redirect('greeting:index')  # С указанием пространства имен
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = NameForm()

    # Получаем последние 5 сохраненных имен для отображения
    recent_names = UserName.objects.all()[:5]

    context = {
        'form': form,
        'recent_names': recent_names,
    }
    return render(request, 'greeting/index.html', context)