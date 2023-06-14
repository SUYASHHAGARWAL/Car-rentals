from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
from rest_framework.decorators import api_view
from paynrentapp.serializer import Vehicleserializers
from paynrentapp.models import Vehicle
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def VehicleInterface(request):
    return render(request,"VehicleInterface.html")


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def VehicleSubmit(request):
    if request.method == 'POST':
        VehicleSerializer = Vehicleserializers(data=request.data)
        if VehicleSerializer.is_valid():
            VehicleSerializer.save()
            return render(request,"VehicleInterface.html",{'message':"Record Submitted Sucessfully"})
        return render(request,"VehicleInterface.html",{'message':"Fail to Submit Record"})


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def VehicleDisplay(request):
    try:
        if request.method == 'GET':
            list_vehicle = Vehicle.objects.all()
            list_vehicle_serializers = Vehicleserializers(list_vehicle,many=True)
            records = tuple_to_dict.ParseDict(list_vehicle_serializers.data)
            q = " select V.*,( select C.categoryname from paynrentapp_category C where C.id = V.categoryid) as categoryname,( select A.Agencyname from paynrentapp_agencies A where A.id = V.agencyid) as agencyname, ( select S.subcategoryname from paynrentapp_subcategory S where S.id = V.subcategoryid) as subcategoryname from paynrentapp_vehicle V"            
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print("xxxxxxxxxx",records)
            

            return render(request,"VehicleDisplay.html",{'data':records})
    except Exception as e:
        print("Error : " ,e)
        return render(request,"VehicleDisplay.html",{'data':{}})  


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def VehicleDisplayById(request):
    try:
        if request.method == 'GET':
            q = "select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname from paynrentapp_vehicle V where id={0}".format(request.GET['id'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictSingleRecord(cursor)
            print("xxxxxxxxxx",record)
            return render(request,"VDisplayById.html",{'data':record})
    except Exception as e:
        print("Error : ",e)
        return render(request,"VDisplayById.html",{'data':record})


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def EditVehicle(request):
    try :
        if request.method == 'GET' :
            if request.GET['btn'] == 'Edit' :
                vehicle = Vehicle.objects.get(pk=request.GET['id'])
                vehicle.categoryid = request.GET['categoryid']
                vehicle.subcategoryid = request.GET['subcategoryid']
                vehicle.modelyear = request.GET['modelyear']
                vehicle.variant = request.GET['variant']
                vehicle.price = request.GET['price']
                vehicle.insured = request.GET['insured']
                vehicle.registrationno = request.GET['registrationno']
                vehicle.ownername = request.GET['ownername']
                vehicle.mobileno = request.GET['mobileno']
                vehicle.colour = request.GET['color']
                vehicle.fueltype = request.GET['fueltype']
                vehicle.no_of_seats = request.GET['no_of_seats']
                vehicle.transmissiontype = request.GET['transmissiontype']
                vehicle.save()
            else :
                vehicle = Vehicle.objects.get(pk=request.GET['id'])
                vehicle.delete()
            return redirect('/api/vehicledisplay')
    except Exception as e:
        print("Error :" ,e)
        return redirect('/api/vehicledisplay')


@xframe_options_exempt        
@api_view(['GET','POST','DELETE'])
def DisplayVehicleIcon(request):
    try :
        if request.method == 'GET':
            return render(request,"Vehicle_Display_Icon.html",{'data':request.GET})
    except Exception as e:
        print("Error : ",e)
        return render(request,"Vehicle_Display_Icon.html",{'data':[]})


@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def SaveVehicleIcon(request):
    try :
        if request.method == 'POST':
            vehicle = Vehicle.objects.get(pk=request.POST['id'])
            vehicle.icon = request.FILES['icon']
            vehicle.save()
            return redirect('/api/vehicledisplay')
    except Exception as e:
        print("Error : ",e)
        return redirect('/api/vehicledisplay')