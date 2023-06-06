from django.shortcuts import render, redirect

from .models import Picture


def upload_view(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        for image in images:
            Picture.objects.create(image=image)
        return redirect('gallery')
    return render(request, 'upload.html')


def gallery_view(request):
    pictures = Picture.objects.all()
    return render(request, 'gallery.html', {'pictures': pictures})


def annotation_view(request, picture_id):
    picture = Picture.objects.get(pk=picture_id)
    if request.method == 'POST':
        annotation = request.POST.get('annotation')
        picture.annotation = annotation
        picture.save()
        return redirect('gallery')
    return render(request, 'annotation.html', {'picture': picture})
