from django.shortcuts import render as render_template

def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except:
        return None

def is_post(request):
    return request.method == 'POST'

def render(request, template, *args, **kwargs):
    return render_template(request, f"{template}.html", *args, kwargs)