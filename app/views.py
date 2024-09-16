from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from . import render, is_post

def details_view(request, form_class, header='Recods', data_template='data-table.html', main_template='details', *args, **kwargs):
    if is_post(request):
        form = form_class(request.POST)
        
        if form.is_valid() and form.save():
            messages.success(request, f"{header} created successfully!!!")
            return redirect(request.path)
    else: form = form_class()

    return render(
        request, main_template, 
        title=f"BSSB {header}", 
        header=header, form=form, 
        data_template=data_template, 
        *args, **kwargs
    )

def update_view(request, model, form_class, success_url, header='Recods',  template='update', *args, **kwargs):
    if is_post(request):
        form = form_class(instance=model, data=request.POST)
        
        if form.is_valid() and form.save():
            messages.success(request, f"{header} updated successfully!")
            return redirect(success_url)
    else: form = form_class(instance=model)
    
    return render(
        request, template, form=form, 
        model=model, 
        back_url=reverse_lazy(success_url),
        title=f"BSSB Update {header}",
        *args, **kwargs
    )
    
def delete_view(request, model, success_url, header='Recods'):
    if is_post(request):
        model.delete()
        messages.success(request, f"{header} deleted successfully!")
        return redirect(success_url)
    
    return render(
        request, 'delete', model=model,
        title=f"BSSB Delete {header}",
        back_url=reverse_lazy(success_url)
    )