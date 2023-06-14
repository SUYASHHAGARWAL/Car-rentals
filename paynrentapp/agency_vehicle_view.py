from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
from rest_framework.decorators import api_view
from paynrentapp.serializer import Vehicleserializers
from paynrentapp.models import Vehicle
from paynrentapp.models import Agencies

from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def AgencyVehicleInterface(request):
  if request.method == 'GET':
    print("\n\n\nNEW INTERFACE")
    q = " select * from paynrentapp_agencies where id = {0}".format(p)    
    print("this is new interface")
    cursor = connection.cursor()
    cursor.execute(q)
    records = tuple_to_dict.ParseDictMultipleRecord(cursor)
    print("xxxxxxxxxx",records)
    if(records):
        return render(request,"AgencyVehicleInterface.html",{'data':records[0]})
    else:
        return render(request,"AgencyVehicleInterface.html",{'data':records})

        
        

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def AgencyVehicleSubmit(request):
    if request.method == 'POST':
        print("NEW INterface")
        VehicleSerializer = Vehicleserializers(data=request.data)
        if VehicleSerializer.is_valid():
            VehicleSerializer.save()
            print(VehicleSerializer)
            return render(request,"AgencyVehicleInterface.html",{'message':"Record Submitted Sucessfully"})
        return render(request,"AgencyVehicleInterface.html",{'message':"Fail to Submit Record"})

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def AgencyVehicleDisplay(req):
    try:
        if req.method == 'GET':
            q = "select * from paynrentapp_agencies where mobileno='{0}' and password='{1}'".format(req.GET['mobileno'],req.GET['password'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            if(record):
                print(record)
                print("dscdhfaydcsvyc",record[0]['id'])
                global p
                p=record[0]['id']
                q = " select V.*,( select C.categoryname from paynrentapp_category C where C.id = V.categoryid) as categoryname,( select A.Agencyname from paynrentapp_agencies A where A.id = V.agencyid) as agencyname, ( select S.subcategoryname from paynrentapp_subcategory S where S.id = V.subcategoryid) as subcategoryname from paynrentapp_vehicle V where V.agencyid = {0}".format(p)
                print("this is new interface")
                cursor = connection.cursor()
                cursor.execute(q)
                records = tuple_to_dict.ParseDictMultipleRecord(cursor)
                print("xxxxxxxxxx",records)
                return render(req,"AgencyVehicleDisplay.html",{'data':records})
            else:
                return render(req,"AgenciesSignup.html",{'message':"No record found"})
    except Exception as e:
        print("Error : " ,e)
        return render(req,"AgencyVehicleDisplay.html",{'data':{}}) 

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def DeleteVehicle(request):
    try :
        if request.method == 'GET' :
            vehicle = Vehicle.objects.get(pk=request.GET['id'])
            vehicle.delete()
            return redirect('/api/agencyvehicledisplay')
    except Exception as e:
        print("Error :" ,e)
        return redirect('/api/agencyvehicledisplay')
    

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def CheckAgencyLogin(request):
    try:
        if request.method == 'GET':
            q = "select * from paynrentapp_agencies where mobileno='{0}' and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print(record)
            print("dscdhfaydcsvyc",record[0]['id'])
            global p
            p=record[0]['id']
            if(len(record)==0):
                return render(request,"AdminLogin.html",{'message':'Invalid id or pass'})
            else:
                return render(request,"DashBoard2.html", {'data':record[0]})
            
    except Exception as e:
        print("Error : ",e)
        # return render(request,"Dashboard.html",{'data':[],'status':False})