from django.db import models
import datetime
from django.contrib.auth.models import User

class part(models.Model):
    COMMODITIES = (
    ('Rotatives Fan', 'Rotatives Fan'),
    ('Rotatives Compressor', 'Rotatives Compressor'),
    ('Rotatives Shaft', 'Rotatives Shaft'),
    ('Rotatives Turbine', 'Rotatives Turbine'),
    )
    engines = (('Tay', 'Tay'),('BR700', 'BR700'),('BR710', 'BR710'),
    ('BR725', 'BR725'),('BR700NG', 'BR700NG'),('RB3043', 'RB3043'),)
    Partnumber=models.CharField(max_length=26,unique=True)
    Partname=models.CharField(max_length=26,null=True)
    Supplier=models.CharField(max_length=26)
    Commodity=models.CharField(max_length=26, choices=COMMODITIES)
    Engine=models.CharField(max_length=26, choices=engines, null=True)

    def __str__(self):
        return self.Partnumber

class con(models.Model):
    decision = (
        ('Open', 'Open'),('ACAT3', 'Accept CAT3'),
        ('ACAT2', 'Accept CAT2'),
        ('ACAT1', 'Accept CAT1'),
        ('ACATX', 'Accept CATX'),
        )
    Conc_Number=models.CharField(max_length=26,unique=True)
    Description=models.CharField(max_length=260,blank=True,null=True)
    partnumber=models.ForeignKey(part,on_delete=models.CASCADE,null=True)
    Drawing_issue=models.CharField(max_length=2,blank=True,null=True)
    Quantity=models.CharField(max_length=10,blank=True,null=True)
    DP=models.BooleanField(default=False,)
    Indate=models.DateField()
    Outdate=models.DateField(blank=True,null=True)
    CreatedDate=models.DateTimeField(auto_now_add=True,null=True)
    UpdatedDate=models.DateTimeField(auto_now=True,null=True)
    Decision=models.CharField(max_length=26,choices=decision,null=True)
    User=models.ForeignKey(User,on_delete=models.CASCADE,)

    def __str__(self):
        return self.Conc_Number

class item(models.Model):
    features = (('Curvic', 'Curvic'),('Hole', 'Hole'),('Entire part', 'Entire part'),('rear wall', 'rear wall'),)
    requirement = (('Diameter', 'Diameter'),('Length', 'Length'),('Position', 'Position'),('RQSC', 'RQSC'),)
    unit = (('mm', 'mm'),('degree', 'degree'),('inch', 'inch'),)
    rootcause = (('Salvage', 'Salvage'),('Process capability', 'Process capability'),('Human error', 'Human error'),)
    Conc_Number= models.ForeignKey(con,on_delete=models.CASCADE)
    Number = models.CharField(max_length=26)
    Description=models.CharField(max_length=260,null=True,blank=True)
    SNumber = models.CharField(max_length=26)
    Feature=models.CharField(max_length=26,choices=features)
    Requirement=models.CharField(max_length=26,choices=requirement)
    Mpos=models.CharField(max_length=26,blank=True)
    Grid=models.CharField(max_length=26,blank=True)
    Nom=models.CharField(max_length=26,blank=True)
    Tol=models.CharField(max_length=26,blank=True)
    Actual=models.CharField(max_length=26,blank=True)
    Unit=models.CharField(max_length=26,choices=unit)
    Rootcause=models.CharField(max_length=26,choices=rootcause)
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    CreatedDate=models.DateTimeField(auto_now_add=True,null=True)
    UpdatedDate=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.Number
