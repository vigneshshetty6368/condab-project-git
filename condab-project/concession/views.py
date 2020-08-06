from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from .models import con,item,part
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . import forms

@login_required
def index(request):
    form=forms.Search(request.POST)
    context_dict= {}
    if request.method=='POST':
        if form.is_valid():
            context_dict['Items']=item.objects.filter(Conc_Number__Conc_Number__contains=request.POST['Conc'],Number__startswith=request.POST['Item'],
            SNumber__contains=request.POST['SNo'],
            Conc_Number__partnumber__Partnumber__contains=request.POST['Part'],
            Conc_Number__partnumber__Supplier__startswith=request.POST['Supplier'],
            Mpos__startswith=request.POST['Mpos'],
            Grid__startswith=request.POST['Grid'],
            Nom__startswith=request.POST['Nom'],
            Tol__contains=request.POST['Tol'],
            Actual__startswith=request.POST['Actual'],
            Conc_Number__Decision__contains=request.POST['Decision'],
            Conc_Number__Indate__year__startswith=request.POST['Indate'],
            Conc_Number__Outdate__year__startswith=request.POST['Outdate'],
            User__username__contains=request.POST['User'],).order_by('Conc_Number__partnumber__Partnumber','Nom','-Actual')
    else:
        context_dict['Items']=item.objects.order_by('-Conc_Number__Outdate','Conc_Number__Conc_Number','Number')
    return render (request,'concession/index.html',context=context_dict)

@login_required
def detail(request,nmn):
    detailcon= get_object_or_404(con,pk=nmn)
    oldcon=get_object_or_404(con,pk=nmn)
    if request.method =="POST" and 'update' in request.POST:
        return redirect('update', detailcon.pk)
    elif request.method =="POST" and 'createitem' in request.POST:
        return redirect('createitem',detailcon.pk)
    elif request.method =="POST" and 'delete' in request.POST:
        return redirect('delete', detailcon.pk)
    elif request.method =="POST" and 'saveas' in request.POST:
        try:
            newcon=con.objects.get(Conc_Number= request.POST['conc'])
            raise ValidationError("Concession/DP already exists")
        except con.DoesNotExist:
            detailcon.pk=None
            detailcon.Conc_Number= request.POST['conc']
            detailcon.save()
            for item in oldcon.item_set.all():
                item.Conc_Number= detailcon
                item.pk=None
                item.save()
            return redirect('detail', detailcon.pk)
    return render (request,'concession/detail.html',{'concession':detailcon,})

@login_required
def update(request, nmn):
    oldcon = get_object_or_404(con, pk= nmn)
    print(oldcon)
    form = forms.createconform(request.POST or None, instance = oldcon)
    if request.method =="POST" and 'Update' in request.POST:
        if form.is_valid():
            form.instance.User=request.user
            form.save()
            return redirect('detail', nmn)
    return render(request, 'concession/update.html', {'form':form, 'oldcon':oldcon})

@login_required
def delete(request,nmn): #latest one
    conobj = get_object_or_404(con, pk= nmn)
    if request.method =="POST":
        conobj.delete()
        return redirect ('index')
    return render(request, "concession/delete.html", {'concession':conobj})

@login_required
def help(request):
    context_dict={'key':'help madtini pa'}
    return render (request,'concession/help.html',context=context_dict)

@login_required
def createcon(request):
        form2 = forms.createconform(request.POST or None)
        if request.method=='POST' and 'import' in request.POST:
            #if form.is_valid(): #and form2.is_valid():
                importcon = get_object_or_404(con, Conc_Number=request.POST['conc'])
                print(importcon)
                form2 = forms.createconform(instance =importcon)
        if request.method=='POST' and 'Create' in request.POST:
            #if form2.is_valid():
                try:
                    con.objects.get(Conc_Number= request.POST['Conc_Number'])
                    raise ValidationError("Concession/DP already exists")
                except con.DoesNotExist:
                    form2.instance.User=request.user
                    newcon=form2.save()
                    print(newcon)
                    print(request.user)
                    return redirect('detail', newcon.pk)
        return render(request,'concession/create.html',{'form2':form2})

@login_required
def createitem(request,nmn):
        conobj = get_object_or_404(con, pk= nmn)
        N=conobj.item_set.count()
        #N=conobj.item.Number.max
        #try conobj.item_set.order_by('Number')[0]
        print(conobj)
        form2 = forms.createitemform(request.POST or None,initial={'Conc_Number':conobj,'Number':N+1,})
        form2.fields['Conc_Number'].disabled = True
        if request.method=='POST'and 'Create' in request.POST:
            if form2.is_valid():
                form2.instance.User=request.user
                newitem=form2.save()
                print(newitem)
                print(request.user)
                return redirect('detail', nmn)
        return render(request,'concession/createitem.html',{'form2':form2,'conobj':conobj})

@login_required
def detailitem(request,nmn): #latest one
    olditem = get_object_or_404(item, pk= nmn)
    return render(request, "concession/detailitem.html", {'item':olditem})

@login_required
def updateitem(request, nmn):
    olditem = get_object_or_404(item, pk= nmn)
    print(olditem)
    form = forms.createitemform(request.POST or None, instance = olditem)
    if request.method =="POST" and 'Updateitem' in request.POST:
        if form.is_valid():
            form.instance.User= request.user
            form.save()
            return redirect('detail', olditem.Conc_Number.pk)
    return render(request, 'concession/updateitem.html', {'form2':form,'olditem':olditem})

@login_required
def deleteitem(request,nmn):
    olditem = get_object_or_404(item, pk= nmn)
    if request.method =="POST":
        olditem.delete()
        return redirect ('detail', olditem.Conc_Number.pk)
    return render(request, "concession/deleteitem.html", {'item':olditem})


@login_required
def database(request):
        form = forms.createpartform(request.POST or None)
        if request.method=='POST' and 'createpart' in request.POST:
            #if form.is_valid():
                try:
                    part.objects.get(Partnumber= request.POST['Partnumber'])
                    raise ValidationError("Part already exists")
                except part.DoesNotExist:
                    newpart=form.save()
                    print(newpart)
        return render(request,'concession/database.html',{'form':form, 'Parts':part.objects.all})

@login_required
def about(request):
    return render(request,'concession/about.html')
