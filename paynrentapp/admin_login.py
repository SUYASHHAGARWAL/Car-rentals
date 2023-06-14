from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
from rest_framework.decorators import api_view
from paynrentapp.serializer import AdminstratorSerializer
from paynrentapp.models import Administrator
from django.views.decorators.clickjacking import xframe_options_exempt
from paynrentapp.serializer import agencyserialiser
from paynrentapp.models import Agencies



from . import tuple_to_dict

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def AdminLogin(request):
    return render(request,"AdminLogin.html")
@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def AdminLogin1(request):
    print("HELOOOOOO")
    return render(request,"AdminLogin.html")

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def CheckAdminLogin(request):
    try:
        if request.method == 'GET':
            q = "select * from paynrentapp_administrator where (mobileno='{0}' or emailid='{0}') and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            if(len(record)==0):
                return render(request,"AdminLogin.html",{'message':'Invalid id or pass'})
            else:
                return render(request,"DashBoard.html",{'data':record[0]})
            
    except Exception as e:
        print("Error : ",e)
        return render(request,"Dashboard.html",{'data':[],'status':False})
   
# @api_view(['GET','POST','DELETE'])
# def UserSignup(request):
#     if request.method=='POST':
#         customer_serializers = CustomersSerializer(data=request.data)
#         try:
#             if customer_serializers.is_valid():
#                 customer_serializers.save()
#                 return render(request,'SubCategoryInterface.html',{'message':"record submitted"})
#         except Exception as e:
#             print(e)
#             return render(request,"SubCategoryInterface.html",{"message":"Failed"})

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def AgencySignupLogin(request):
    return render(request,"AgenciesSignup.html")

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Agencysubmit(request):
    if request.method == 'POST':
        agency_serialiser = agencyserialiser(data=request.data)
        if agency_serialiser.is_valid():
            agency_serialiser.save()
            return render(request,"AgenciesSignup.html",{'message':"Signup Succesful"})
        return render(request,"AgenciesSignup.html",{'message':"Signup failed"})

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def AgencyDisplay(req):
  try:
    if req.method == 'GET':
        list_category=Agencies.objects.all()
        list_category_serializer=agencyserialiser(list_category, many=True)
        records=tuple_to_dict.ParseDict(list_category_serializer.data)

        return render(req,'AgenciesDisplay.html',{'data':records}) 
  except Exception as e:
      print("Error:",e)
      return render(req,'AgenciesDisplay.html',{'data':{}})

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def AgencyDelete(request):
    try: 
        if request.method=='GET':
            cat=Agencies.objects.get(pk=request.GET['id'])
            cat.delete()
            return redirect('/api/agecyvehicledisplay')
    except Exception as e:
        print("Error",e)
        return redirect('/api/agecyvehicledisplay')