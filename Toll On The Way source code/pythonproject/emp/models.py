from django.db import models

class employdetails(models.Model):
    employeename=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    employeeID=models.CharField(max_length=250)
    adharnumber=models.CharField(max_length=250)   
    def __str__(self):
        return self.employeename
    
    
class TOLLLOCATIONS(models.Model):
    place=models.CharField(max_length=250)
    numberoflanes=models.CharField(max_length=250)
    numberofemployees=models.CharField(max_length=250)
    def __str__(self):
        return self.place
    
class VEHICLECHARGES(models.Model):    
    vehicletype=models.CharField(max_length=250)
    onewaycharge=models.CharField(max_length=250)
    twowaycharges=models.CharField(max_length=250)
    monthlypass=models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.vehicletype
  
    
    
    
       
