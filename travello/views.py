from django.shortcuts import render
from .models import destination
# Create your views here.
def index(request):
    
    # dest1=destination()
    # dest1.name='Mumbai'
    # dest1.desc="The city which never sleep"
    # dest1.img= 'destination_1.jpg'
    # dest1.price="$700"
    # dest1.offer=False

    # dest2=destination()
    # dest2.name='Hyderabad'
    # dest2.desc="First Biryani ,Then Shervani"
    # dest2.img= 'destination_2.jpg'
    # dest2.price="$650"
    # dest2.offer= True
    
    # dest3=destination()
    # dest3.name='Bengaluru'
    # dest3.desc="The city of IT Industry"
    # dest3.img= 'destination_3.jpg'
    # dest3.price="$800"
    # dest3.offer=False
   
    # dests=[dest1,dest2,dest3]
    dests=destination.objects.all()
    
    return render(request,'index.html',{'dests':dests})