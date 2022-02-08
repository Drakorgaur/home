from home.Helpers.room import *
from django.shortcuts import render, redirect


def save_object(request, form, link):
    if not link:
        form.save()
    else:
        obj = form.save(commit=False)
        obj.room = request.user.room
        obj.save()


def common_create(request, _class, url, template, link=False):
    context = get_context(request)
    if request.method == 'POST':
        form = _class(request.POST)
        if form.is_valid():
            save_object(request, form, link)
            return redirect(url)
        else:
            context['error'] = 'form is invalid'
    form = _class()
    context['form'] = form
    return render(request, template, context)


def common_detail(request, _class, pk, template, _subclass=None):
    context = get_context(request=request)
    object = _class.objects.get(pk=pk)
    context[(_class.__name__).lower()] = object
    if _subclass is not None:
        objects = _subclass.objects.filter(room=context['room'])
        context[(_subclass.__name__).lower()] = objects
    return render(request, template, context)


def common_list(request, _class, template):
    context = get_context(request)
    objects = _class.objects.all()
    key = (_class.__name__).lower()
    context[f'{key}s'] = objects
    return render(request, template, context)


def common_edit(request, _class, pk, _form, url, template, link=False):
    context = get_context(request)
    obj = _class.objects.get(pk=pk)
    if request.method == 'POST':
        form = _form(request.POST)
        if form.is_valid():
            save_object(request, form, link)
            return redirect(url)
        else:
            context['error'] = 'form is invalid'
    form = _form(instance=obj)
    context['form'] = form
    return render(request, template, context)


def common_delete(request, _class, pk, redirect_to):
    obj = _class.objects.get(pk=pk)
    obj.delete()
    return redirect(redirect_to)