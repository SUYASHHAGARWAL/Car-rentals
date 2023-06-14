from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.db import connection
from rest_framework.decorators import api_view
from paynrentapp.serializer import categoryserializers
from paynrentapp.models import category
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def CategoryInterface(request):
    return render(request,'CategoryInterface.html')


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def CategorySubmit(request):
    if request.method == 'POST':
        category_serializers = categoryserializers(data=request.data)
        try:
            
            if category_serializers.is_valid():
                category_serializers.save()
                return render(request,'CategoryInterface.html',{"message":"record Submitted"})
               
            return render(request,"CategoryInterface.html",{"message":"Failed"})
        except Exception as e:
            print(e)
            return render(request,"CategoryInterface.html",{"message":"Failed"})


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def CategoryDisplay(request):
  try:
    if request.method == 'GET':
        list_category=category.objects.all()
        list_category_serializer=categoryserializers(list_category, many=True)
        records=tuple_to_dict.ParseDict(list_category_serializer.data)

        return render(request,'CategoryDisplay.html',{'data':records}) 
  except Exception as e:
      print("Error:",e)
      return render(request,'CategoryDisplay.html',{'data':{}}) 


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def DisplayByCategoryId(request):
    try:
        if request.method =='GET':
            q="select * from paynrentapp_category where id={0}".format(request.GET['id'])
            cursor=connection.cursor()
            cursor.execute(q)
            record=tuple_to_dict.ParseDictSingleRecord(cursor)
            return render(request,'DisplayById.html',{'data':record})
    except Exception as e:
        print("Error:",e)
        return render(request,'DisplayById.html',{'data':{}})


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def CategoryEdit(request):
    try: 
        if request.method=='GET':
          if request.GET['btn']=='edit':
            cat=category.objects.get(pk=request.GET['id'])
            cat.categoryname=request.GET['categoryname']
            cat.description=request.GET['description']
            cat.save()
          else:
            cat=category.objects.get(pk=request.GET['id'])
            cat.delete()
          return redirect('/api/categorydisplay')
    except Exception as e:
        print("Error",e)
        return redirect('/api/categorydisplay')



@xframe_options_exempt    
@api_view(['GET','POST'])
def DisplayCategoryIcon(request):
  try:
    if request.method == 'GET':
      
      return render(request,'display_category_icon.html',{'data':dict(request.GET)})
  except Exception as e:
     print("Error:",e)
     return render(request,'display_category_icon.html',{'data':{}})


@xframe_options_exempt    
@api_view(['GET','POST'])
def Category_Save_Icon(request):
  try:
    if request.method == 'POST':
      
       cat=category.objects.get(pk=request.POST['id'])
       cat.icon=request.FILES['icon']
       cat.save()
       return redirect('/api/categorydisplay')
  except Exception as e:
     print("Error:",e)
     return redirect('/api/categorydisplay')     

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def CategoryDisplayJSON(request):
  try:
    if request.method == 'GET':
        list_category=category.objects.all()
        list_category_serializer=categoryserializers(list_category, many=True)
        records=tuple_to_dict.ParseDict(list_category_serializer.data)

        return JsonResponse(records,safe=False)
  except Exception as e:
      print("Error:",e)
      return JsonResponse([],safe=False)