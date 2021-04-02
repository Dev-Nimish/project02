from  django.http import HttpResponse
import os 
 
currentdir = os.path.abspath(__file__)
parentdir = os.path.dirname(currentdir)
mainparent = os.path.dirname(parentdir)

def index1(request):
    content = os.path.join(mainparent,"sample.html")
    fp  = open(content,"r")
    data = fp.read()
    return HttpResponse(data)