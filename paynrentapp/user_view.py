from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.db import connection
from rest_framework.decorators import api_view 
from paynrentapp.serializer import Vehicleserializers
from paynrentapp.models import Vehicle
from paynrentapp.models import User
from paynrentapp.serializer import userserialiser
from . import tuple_to_dict
import json
import datetime
from django.views.decorators.clickjacking import xframe_options_exempt
# import razorpay
from django.conf import settings


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def new(req):
    return render(req,'index.html')

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def Index(request): 
    return render(request,"index.html",{'message':''})

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def ShowVehicleList(request):
    userdata={'mobilenum':'','city':request.GET['city'],'startdate':request.GET['startdate'],'enddate':request.GET['enddate'],'days':request.GET['dh'],'option':request.GET['option']}
    request.session["USERDATA"] = userdata
    d = userdata['days'].split(":")
    userdata['dys']=d[0]
    userdata['hrs']=d[1]
    print("\n\n\n\n\n",d[0],d[1])
    request.session["USERDATA"] = userdata

    return JsonResponse(userdata, safe=False)

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def Index2(request):
    userdata = request.session["USERDATA"]
    q="select * from paynrentapp_vehicle where city='{0}'".format(userdata['city'])
    print(q)
    cursor = connection.cursor()
    cursor.execute(q)
    records = tuple_to_dict.ParseDictSingleRecord(cursor)
    # print("xxxxxxxxxx",records)
    return render(request,"Index2.html",{'userdata':userdata,'record':records})

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def Index3(request):
    userdata = request.session["USERDATA"]

    vehicles=request.GET['vehicles']
    selected_vehicles=json.loads(vehicles)
    # print("\n\n\n",selected_vehicles)
    st = datetime.datetime.strptime(userdata['startdate'],"%Y/%m/%d %H:%M")
    et = datetime.datetime.strptime(userdata['enddate'],"%Y/%m/%d %H:%M")
    userdata['startdate'] = datetime.datetime.strftime(st,"%a %d %b %Y")
    userdata['enddate'] = datetime.datetime.strftime(et,"%a %d %b %Y")
    d = userdata['days'].split(":")
    print("\n\n\n\n",d[0],d[1])
    userdata['days'] = d[0] + " Days , " + d[1] + " Hours"
    userdata['fare'] = selected_vehicles['price']
    hr = int(selected_vehicles['price'])//24
    userdata['amount'] = int(d[0])*int(selected_vehicles['price'])+(hr*int(d[1]))
    userdata['netamount'] = userdata['amount'] + 600 + 600
    # print("\n\nssssss",selected_vehicles)
    # return render(request,"Index3.html",{'userdata':userdata})
    q= "select picture, picture2 , picture3, picture4, picture5 from paynrentapp_vehicle where subcategoryid={}".format(selected_vehicles['subcategoryid'])
    # print(q)
    cursor = connection.cursor()
    cursor.execute(q)
    records = tuple_to_dict.ParseDictMultipleRecord(cursor)
    # print("xxxxxxxxxx\n\n",records)
    if(userdata['option'] =='With Driver' ):
        qry = "select * from paynrentapp_Drivers where appointed_to_someone ='no'"
        cursor = connection.cursor()
        cursor.execute(qry)
        rtd = tuple_to_dict.ParseDictMultipleRecord(cursor)
        if(rtd):
            print("hp rha h apooint")
            print(rtd)
            return render(request,"Index3.html",{'vehicles':selected_vehicles,'userdata':userdata,'records':records,'dprofile':rtd[0]})
        return render(request,"Index3.html",{'vehicles':selected_vehicles,'userdata':userdata,'records':records})
    else:
        return render(request,"Index3.html",{'vehicles':selected_vehicles,'userdata':userdata,'records':records})


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def SetMobileandemail(request):
    userdata = request.session["USERDATA"]
    userdata['mobileno']=request.GET['mobileno']
    userdata['emailaddress']=request.GET['emailid']
    userdata['amount']=request.GET['amount']
   
    request.session["USERDATA"] = userdata
    return JsonResponse(userdata, safe=False)

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def VehicleDisplayForUser(request):
    try:
        if request.method == 'GET':
            userdata = request.session["USERDATA"]

            # print("iiiiiiiiiiiiiiiiiiiiiiiiiiiii\n",request.GET['param'])
            if(request.GET['param']=="all"):
                q = "select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname,(select S.companyname from paynrentapp_subcategory S where S.id=V.subcategoryid) as companyname from paynrentapp_vehicle V where city='{}'".format(userdata['city'])
            
            else:
                # q = "select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname,(select S.companyname from paynrentapp_subcategory S where S.id=V.subcategoryid) as companyname from paynrentapp_vehicle V where V.subcategoryid in (select id from paynrentapp_subcategory where companyname in ({}) or fueltype in ({}) or transmissiontype in ({}) )".format(request.GET['param'])
                q = "select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname,(select S.companyname from paynrentapp_subcategory S where S.id=V.subcategoryid) as companyname from paynrentapp_vehicle V where V.subcategoryid in (select id from paynrentapp_subcategory where  subcategoryname in ({}) or (companyname in ({}) or fueltype in ({})) or transmissiontype in ({}) )".format(request.GET['param'],request.GET['param'],request.GET['param'],request.GET['param'])
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            # print("xxxxxxxxxx",records)
            return JsonResponse(records,safe=False)
    except Exception as e: 
        print("Error : " ,e)
        return JsonResponse(records,safe=False)

@xframe_options_exempt    
@api_view(['GET','POST','DELETE']) 
def Usersignup(req):
    userdata = req.session["USERDATA"]

    return render(req,"Index4.html",{'userdata':userdata})


@api_view(['GET', 'POST', 'DELETE'])
def Index2Modify(request):
    userdata = request.session["USERDATA"]
    userdata['city'] = request.GET['city']
    userdata['startdate'] = request.GET['startdate']
    userdata['enddate'] = request.GET['enddate']
    userdata['days'] = request.GET['days']
    request.session["USERDATA"] = userdata
    d = userdata['days'].split(":")
    userdata['dys']=d[0]
    userdata['hrs']=d[1]
    print("\n\n\n\n\n",d[0],d[1])

    print("Dayyysss :",userdata['days'])
    return JsonResponse(userdata, safe=False)


@xframe_options_exempt    
@api_view(['GET','POST','DELETE']) 
def UsersData(req):
    if req.method == 'POST':
        us_srlsr = userserialiser(data=req.data)
        print(req.data)
        print(us_srlsr)
        try:
            if us_srlsr.is_valid():
                us_srlsr.save()
                return render(req,"Index4.html",{"message":"Data saved"})
            return render(req,"Index4.html",{"message":"Failed"})

        except Exception as e:
            print("Error",e)
            return render(req,"Index4.html",{"message":"Failed"})

    return render(req,"Index4.html")

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def CheckUserLogin(request):
    try:
        print("HI")
        userdata = request.session["USERDATA"]
        print("HI")
        amt = userdata['amount']
        # client = razorpay.Client(auth=(settings.KEY,settings.SECRET))
        # payment = client.order.create({'amounttt':amt,'currency':'INR'})
        # context = {'payment': payment}
        # print(payment)
        if request.method == 'GET':
            q = "select * from paynrentapp_user where mobileno='{0}' and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            if(record):

                print(record)
                print("dscdhfaydcsvyc",record[0]['id'])
                return render(request,"Index4.html",{'message':'Data Matched','userdata':userdata})
            else:
                return render(request,"Index4.html", {'message':'Invalid Id or pass'})
            
    except Exception as e:
        print("Error : ",e)
        # return render(request,"Dashboard.html",{'data':[],'status':False})


#select_related()
#prefetch_relate()