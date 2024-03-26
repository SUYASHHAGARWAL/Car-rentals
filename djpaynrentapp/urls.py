"""djpaynrentapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from paynrentapp import category_view
from paynrentapp import subcategory_view
from paynrentapp import Vehicle_view
from paynrentapp import admin_login
from paynrentapp import user_view
from paynrentapp import agency_vehicle_view


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^/',user_view.new),
    re_path(r'^api/categoryinterface',category_view.CategoryInterface),
    re_path(r'^api/categorysubmit',category_view.CategorySubmit),
    re_path(r'^api/categorydisplay',category_view.CategoryDisplay),
    re_path(r'^api/display_category_by_id',category_view.DisplayByCategoryId),
    re_path(r'^api/categoryedit',category_view.CategoryEdit),
    re_path(r'^api/display_category_icon',category_view.DisplayCategoryIcon),
    re_path(r'^api/cat_save_icon',category_view.Category_Save_Icon),
    re_path(r'^api/displaycategoryjson',category_view.CategoryDisplayJSON),
    re_path(r'^api/json_displaycategory',category_view.CategoryDisplayJSON),



    
    re_path(r'^api/subcategoryinterface',subcategory_view.SubCategoryInterface),
    re_path(r'^api/subcategorysubmit',subcategory_view.SubCategorySubmit),
    re_path(r'^api/subcategorydisplay',subcategory_view.SubCategoryDisplay),
    re_path(r'^api/display_subcategory_by_id',subcategory_view.DisplayBySubcategoryId),
    re_path(r'^api/editsubcategory',subcategory_view.SubCategoryEdit),
    re_path(r'^api/display_subcategory_icon',subcategory_view.DisplaySubCategoryIcon),
    re_path(r'^api/subcat_save_icon',subcategory_view.Subcategory_save_icon),
    re_path(r'^api/jsondisplaysubcategory',subcategory_view.DisplayBySubcategoryJSON),




    re_path(r'^api/vehicleinterface',Vehicle_view.VehicleInterface),
    re_path(r'^api/vehiclesubmit',Vehicle_view.VehicleSubmit),
    re_path(r'^api/vehicledisplay',Vehicle_view.VehicleDisplay),
    re_path(r'^api/displayvehiclebyid',Vehicle_view.VehicleDisplayById),
    re_path(r'^api/vehicleedit',Vehicle_view.EditVehicle),
    re_path(r'^api/vehicleicondisplay',Vehicle_view.DisplayVehicleIcon),
    re_path(r'^api/savevehicleicon',Vehicle_view.SaveVehicleIcon),    



    re_path(r'^api/loginpage',admin_login.AdminLogin),
    re_path(r'^api/displaybtn',admin_login.AdminLogin1),
    re_path(r'^api/checkadminlogin',admin_login.CheckAdminLogin),
    re_path(r'^api/showvehiclelist',user_view.ShowVehicleList),
    re_path(r'^api/agencysignuplogin',admin_login.AgencySignupLogin),
    re_path(r'^api/agencysubmit',admin_login.Agencysubmit),
    re_path(r'^api/agencydisplay',admin_login.AgencyDisplay), 
    re_path(r'^api/checkagencylogin',agency_vehicle_view.CheckAgencyLogin),



    re_path(r'^api/index',user_view.Index),
    re_path(r'^api/test',user_view.VehicleDisplayForUser),
    re_path(r'^api/twoindex',user_view.Index2),
    re_path(r'^api/displayvehiclelist',user_view.Index3), 
    re_path(r'^api/setmobileemail',user_view.SetMobileandemail), 

    re_path(r'^api/agecyvehicledisplay',agency_vehicle_view.AgencyVehicleDisplay), 
    re_path(r'^api/agencyvehiclesubmit',agency_vehicle_view.AgencyVehicleSubmit), 
    re_path(r'^api/agencyvehicleinterface',agency_vehicle_view.AgencyVehicleInterface), 
    re_path(r'^api/deleteagency',admin_login.AgencyDelete),
        re_path(r'^api/usersignup',user_view.Usersignup),
        re_path(r'^api/userdataindb',user_view.UsersData),
        re_path(r'^api/checkuserlogin',user_view.CheckUserLogin),
        re_path(r'^api/modifyindex2',user_view.Index2Modify),

 



    ]