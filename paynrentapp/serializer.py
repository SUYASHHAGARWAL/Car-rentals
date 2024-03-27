from rest_framework import serializers
from paynrentapp.models import category
from paynrentapp.models import subcategory
from paynrentapp.models import Vehicle
from paynrentapp.models import Administrator
from paynrentapp.models import Agencies
from paynrentapp.models import User
from paynrentapp.models import Drivers

class categoryserializers(serializers.ModelSerializer):
    class Meta:
        model=category
        fields=('id','categoryname','description')
    
class subcategoryserializers(serializers.ModelSerializer):
    class Meta:
        model=subcategory 
        fields=('id','categoryid','companyname','subcategoryname','description')

class Vehicleserializers(serializers.ModelSerializer):
    class Meta:
        model=Vehicle
        fields=('id','agencyid','categoryid','subcategoryid','modelyear','variant','price','insured','registrationno','ownername','mobileno','colour','fueltype','no_of_seats','transmissiontype','picture','city','picture2','picture3','picture4','picture5')
    
class AdminstratorSerializer(serializers.ModelSerializer):
 class Meta:
        model = Administrator
        fields = ('id','adminname','mobileno','emailid','password')

class agencyserialiser(serializers.ModelSerializer):
    class Meta:
        model=Agencies
        fields=('id','Agencyname','mobileno','emailid','password')
    
class userserialiser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','Username','UserEmail','password','mobileno','AadharNumber','licenceNumber')

class driverserializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields=('id','name','email','mobileno','AadharNumber','licenceNumber','appointed_to_someone')