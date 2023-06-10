from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from paynrentapp.serializer import subcategoryserializers
from paynrentapp.models import subcategory
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def SubCategoryInterface(request):
    return render(request,'SubCategoryInterface.html')


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def SubCategorySubmit(request):
    if request.method == 'POST':
        subcategory_serializers = subcategoryserializers(data=request.data)
        try:
            if subcategory_serializers.is_valid():
                subcategory_serializers.save()
                return render(request,'SubCategoryInterface.html',{'message':"record submitted"})
            else:
                return render(request,'SubCategoryInterface.html',{'message':"failed"})

        except Exception as e:
            print(e)
            return render(request,"SubCategoryInterface.html",{"message":"Failed"})


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def SubCategoryDisplay(request):
    try:
        if request.method=='GET':
            list_subcategory=subcategory.objects.all()
            list_subcategory_serializer=subcategoryserializers(list_subcategory,many=True)
            record=tuple_to_dict.ParseDict(list_subcategory_serializer.data)
            return render(request,'SubCategoryDisplay.html',{'data':record})
    except Exception as e:
        print(e)
        return render(request,'SubCategoryDisplay.html',{'data':{}})


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def DisplayBySubcategoryId(request):
    try:
        if request.method=='GET':
            q="select * from paynrentapp_subcategory where id={0}".format(request.GET['id'])
            print(q)
            cursor=connection.cursor()
            cursor.execute(q)
            record=tuple_to_dict.ParseDictSingleRecord(cursor)
            print(record)
            return render(request,'SDisplayById.html',{'data':record})
    except Exception as e:
        print("Error:",e)
        return render(request,'SDisplayById.html',{'data':{}})

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def DisplayBySubcategoryJSON(request):
    try:
        if request.method=='GET':
            q="select * from paynrentapp_subcategory where categoryid={0}".format(request.GET['cddid'])
            print("\n\n\n\n\n",q)
            cursor=connection.cursor()
            cursor.execute(q)
            record=tuple_to_dict.ParseDictMultipleRecord(cursor)
            print(record)
            return JsonResponse(data=record,safe=False)
    except Exception as e:
        print("Error:",e)
        return JsonResponse([],safe=False)


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def SubCategoryEdit(request):
    try:
        if request.method=='GET':
            if request.GET['btn']=='edit':
                subcat=subcategory.objects.get(pk=request.GET['id'])
                subcat.categoryid=request.GET['categoryid']
                subcat.companyname=request.GET['companyname']
                subcat.subcategoryname=request.GET['subcategoryname']
                subcat.description=request.GET['description']
                subcat.save()
            else:
                subcat=subcategory.objects.get(pk=request.GET['id'])
                subcat.delete()
            return redirect('/api/subcategorydisplay')
    except Exception as e:
        print("Error",e)
        return redirect('/api/subcategorydisplay')

@xframe_options_exempt    
@api_view(['GET','POST'])
def DisplaySubCategoryIcon(request):
  try:
    if request.method == 'GET':
      
      return render(request,'display_subcategory_icon.html',{'data':dict(request.GET)})
  except Exception as e:
     print("Error:",e)
     return render(request,'display_subcategory_icon.html',{'data':{}})

@xframe_options_exempt    
@api_view(['GET','POST'])
def Subcategory_save_icon(request):
  try:
    if request.method == 'POST':
       subcat=subcategory.objects.get(pk=request.POST['id'])
       subcat.icon=request.FILES['icon']
       subcat.save()
       return redirect('/api/subcategorydisplay')
  except Exception as e:
     print("Error:",e)
     return redirect('/api/subcategorydisplay')