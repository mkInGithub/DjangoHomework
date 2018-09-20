from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from ToDoList.models import ToDoList
from .forms import ToDoListForm
from django.utils import timezone


def index(request):
    now = datetime.datetime.now()
    task_list = ToDoList.objects.all()
    context = {
        "form": ToDoListForm(),
        "now": timezone.now(),
        "task_list": task_list,
    }
    return render(request, "index.html", context)


# 提交
@csrf_exempt
def submit_todolist(request):
    print("request received")
    if request.method == "POST":
        form = ToDoListForm(request.POST)
        if form.is_valid():
            form.save()
            # data = json.dumps([{"data1": "post success"}])
            data = "post gogogo"
            print("post success")
            # return HttpResponse(data, content_type='application/json')
            return HttpResponse('ok')
        else:
            data = 'form empty'
            return HttpResponse(data, content_type='application/txt')
    else:
        return index(request)

# 获取
def get_todolist(request):
    print('start')
    task_list = ToDoList.objects.all()
    return render(request,'index.html',{"task_list":task_list})
# def get_todolist(request):
#     print("get_todolist")
#     if request.is_ajax():
#         objects = ToDoList.objects.all()  # 准备好需要返回的setquery对象
#         data = get_json_objects(objects, ToDoList)  # 自定义函数(setquery对象,源数据库Model)#  用于setquery对象->>json格式
#         print(data)
#         return HttpResponse(data, content_type='application/json',)
#
#     else:
#         raise Http404()


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


def get_json_objects(model_queryset_objects, model):
    concrete_model = model._meta.concrete_model  # 获取源数据库的model原型,以减少数据库调用
    list_data = []
    for obj in model_queryset_objects:
        dict_data = {}
        for field in concrete_model._meta.local_fields:  # 在原型中获取field(字段)
            if field.name == 'id':  # 把django自带的没用的id的字段都Pass掉
                continue
            value = field.value_from_object(obj)  # 根据model的obj获取对应字段的值
            dict_data[field.name] = value  # {author:"Tom",title:"Cars"}
        list_data.append(dict_data)
        # [{'author':"Tom",'title':"Cars"}, {'author':"Tom",'title':"Cars"}]

    data = json.dumps(list_data, cls=DateEncoder)  # 把list变成json文件
    return data
