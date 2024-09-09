from django.shortcuts import render,redirect
from .models import ImageModel
from .forms import ImageForm
from ultralytics import YOLO
from Mlapi.settings import BASE_DIR
import shutil
import os
global modeli
path=os.path.join(BASE_DIR,'model','best.pt')
modeli = YOLO(path)


def delete_folder(mydir):
    try:
        shutil.rmtree(mydir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


def home(request):
    ImageModel.objects.all().delete()
    
    form=ImageForm()
    content={
        'form':form,
    }
    
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            #deleting folder so that ml model doesn't create another predict folder
            path1=os.path.join(BASE_DIR,'daku','predict')
            path2=os.path.join(BASE_DIR,'media','images')
            delete_folder(path1)
            #deleting all images with image folder so that the naming scheme of this images always remains image.jpg and there remains only one image
            delete_folder(path2)
            #image=str(form.cleaned_data['image'])
            p=os.path.join(path2,'image.jpg')
            ap=form.save()
            modeli.predict(source=p, show=True, save=True, hide_labels=True , hide_conf=False, conf=0.5, save_txt=False, save_crop=False, line_thickness=2,project="C:\mlModel\Mlapi\daku")
            content['object']=ap
            return render(request,'api/form.html',content)
    else:
        form=ImageForm()
        return render(request,'api/form.html',content)
    

def process(request):

    content={
        "object":ImageModel.objects.all().first()
    }
    return render(request,'api/display.html',content)