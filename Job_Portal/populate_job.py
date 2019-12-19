import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Job_Portal.settings')

import django
django.setup()


from testapp.models import *
from faker import Faker
from random import *

fake=Faker()

def Phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead','Software Engeneer'))
        feligibility=fake.random_element(elements=('MCA','B.Tech','M.Tech','Phd'))
        faddress=fake.address()
        femail=fake.email()
        fphnumber=Phonenumbergen()

        bbsr_jobs_record=BBSR_JOBS.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phnumber=fphnumber)

        #hyd_jobs_record=HYD_JOBS.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phnumber=fphnumber)

        #bng_jobs_record=BNG_JOBS.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phnumber=fphnumber)


populate(30)
