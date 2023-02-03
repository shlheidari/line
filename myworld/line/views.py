from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.core import serializers 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import Members
from .models import Capacity
from .models import Selection
import json
from csv import reader
from django.contrib.auth.models import User
import datetime
import time
import _thread as thread
import pytz
from pytz import timezone


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))

def member(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('member.html')
    context = {'mymembers': mymembers,}
    return HttpResponse(template.render(context, request))

def select(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:         
            time_z = timezone('Asia/Tehran')
            now_time = datetime.datetime.now( tz = time_z )
            now = datetime.datetime.strptime(str(now_time)[:19], '%Y-%m-%d %H:%M:%S')
            me =  Members.objects.get(student_id=user)
            now = datetime.datetime.now()
            end_t = datetime.datetime.strptime(me.end_time, '%Y-%m-%d %H:%M:%S')
            start_t = datetime.datetime.strptime(me.start_time, '%Y-%m-%d %H:%M:%S')
            if start_t < now and end_t > now:
                login(request, user)
                mycapacity = Capacity.objects.all()
                data  = serializers.serialize('json', mycapacity)
                template = loader.get_template('select.html')
                data_myselection = Selection.objects.all()
                myselection  = serializers.serialize('json', data_myselection)
                context = {'mycapacity': data, 'me':me, 'myselection':myselection, }           
                def fun_one(end_t,me):
                    time_z = timezone('Asia/Tehran')
                    now_time = datetime.datetime.now( tz = time_z )
                    now = datetime.datetime.strptime(str(now_time)[:19], '%Y-%m-%d %H:%M:%S')
                    delay = (end_t - now).total_seconds()
                    time.sleep(delay)
                    register(me)
                thread.start_new_thread( fun_one, (end_t,me) )
                return HttpResponse(template.render(context, request))

                    
               
            else:
                messages.success(request, ("شما امکان ورود ندارید"))
                return HttpResponseRedirect(reverse('index')) 
        else:
            messages.success(request, ("نام کاربری یا رمز عبور اشتباه است"))
            return HttpResponseRedirect(reverse('index'))     
    else:
        messages.success(request, ("ابتدا وارد سایت شوید"))
        template = loader.get_template('index.html')
        return HttpResponseRedirect(reverse('index'))
    

def capacity(request):
    mycapacity = Capacity.objects.all()
    data  = serializers.serialize('json', mycapacity)
    template = loader.get_template('capacity.html')
    context = {'mycapacity': data,}
    return HttpResponse(template.render(context, request))

def selected(request):
    print(request.session.session_key)
    if (request.session.session_key != None):
        if request.method == "POST":
            raw_data = request.body
            body_unicode = raw_data.decode('utf-8')
            body = json.loads(body_unicode)
            key = list(body.keys())
            if key[0] == 'sel':
                if body['sel'][0]['c'] == '':
                    if body['sel'][0]['b'] == '':
                        pass
                    else:
                        select = Selection(item_fa = body['sel'][0]['a'], item_en = body['sel'][0]['d'], choice = body['sel'][0]['b'], iden = body['sel'][0]['i'], line_c = body['sel'][0]['line_c'])
                        select.save()
                else:
                    if body['sel'][0]['b'] == '':
                        select = Selection.objects.get(item_fa=body['sel'][0]['a'])
                        select.delete()
                    else:
                        select = Selection.objects.get(item_fa=body['sel'][0]['a'])
                        select.choice = body['sel'][0]['b']
                        select.save()
                                     
            else:
                instance = Selection.objects.all()
                instance.delete()
                if body['final'][0]['line'] == "N":
                    pass
                else:
                    select = Selection(item_fa = 'user', item_en = 'user', choice = request.user, iden = request.user, line_c = request.user )
                    select.save() 
                    select = Selection(item_fa = 'line', item_en = 'line', choice = body['final'][0]['line'], iden = body['final'][0]['line'] , line_c = body['final'][0]['line'])
                    select.save() 
            return JsonResponse({'status': 'OK'}, status=200)
        else:
            return JsonResponse({"error": "not found"}, status=404)
    else:
        return JsonResponse({"error": "not found", 'message': 'شخص دیگری وارد اکانت شما شده، مجددا وارد شوید'}, status=404)
    

def loggedout_manual(request):
    me =  Members.objects.get(student_id=request.user)
    logout(request)
    time_z = timezone('Asia/Tehran')
    now_time = datetime.datetime.now( tz = time_z )
    me.end_time = datetime.datetime.strptime(str(now_time)[:19], '%Y-%m-%d %H:%M:%S')
    me.save()
    register(me)
    messages.success(request, ("انتخاب های شما با موفقیت ثبت شد"))
    return HttpResponseRedirect(reverse('index'))


def register(me):
    selected_all = Selection.objects.all().values()
    if len(selected_all)>0:
        if selected_all[0]['choice'] == me.student_id:
            i = 1
            line_sel = selected_all[1]['choice']
            me.line = line_sel
            me.save() 
            unit_sel = '98 ' + line_sel+ '- ' + line_sel 
            capacity_sel = Capacity.objects.get(line = line_sel , unit = unit_sel)
            remain_sel = capacity_sel.remain
            remain_select = int(remain_sel) - 1
            capacity_sel.remain = remain_select
            capacity_sel.save()
            while i < len(selected_all)-1:
                i = i + 1
                item_fa = selected_all[i]['item_fa']
                item_en = selected_all[i]['item_en']
                hospital_sel = selected_all[i]['choice']
                setattr(me, item_en, hospital_sel)
                
                unit_sel = item_fa +"- "+ line_sel
                capacity_sel = Capacity.objects.get(line = line_sel , unit = unit_sel, hospital = hospital_sel)
                remain_sel = capacity_sel.remain
                remain_select = int(remain_sel) - 1
                setattr(capacity_sel, 'remain', remain_select)
                capacity_sel.save()
                me.save() 
                
                if item_en == "gynocology" and hospital_sel == "بهارلو" and capacity_sel.gender == "":
                    setattr(capacity_sel, 'gender', me.gender)
                    capacity_sel.save()
          
    instance = Selection.objects.all()
    instance.delete()
    

def pas(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:         
            login(request, user)
            return HttpResponseRedirect('change_password/')
        else:
            messages.success(request, ("نام کاربری یا رمز عبور اشتباه است"))
            return HttpResponseRedirect(reverse('index'))     
    else:
        messages.success(request, ("ابتدا وارد سایت شوید"))
        template = loader.get_template('index.html')
        return HttpResponseRedirect(reverse('index'))
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('change_password/')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('index')


# def userdata(request):
#     with open(r"C:\Users\So\Desktop\program\project\line\myworld\line\templates\csv\your_file.csv") as csv_file:
#         csvf = reader(csv_file)
#         data = []
#         for row in csvf:
#             if row[0] == '':
#                 break
#             else:
#                 user = User(username=row[0])
#                 user.set_password(row[1])
#                 data.append(user) 
#         User.objects.bulk_create(data)   
#     return JsonResponse('user csv is now working', safe=False)
