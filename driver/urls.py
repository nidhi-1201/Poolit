from django.urls import path
from . import views
app_name = 'driver'


urlpatterns = [
	path('' , views.driverHome , name = "driverHome"),
	path('driverInfo' , views.driverInfo , name = "driverInfo"),
	path('driveProcess' ,views.searchRider , name = "searchRider"),
	path('accept' ,views.acceptRider , name = "acceptRider" ),
	path('end', views.endRide , name ="endRide"),
]
