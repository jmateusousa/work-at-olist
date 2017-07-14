#Libraries
from django.shortcuts import render
from django.core.files.uploadedfile import UploadedFile
from .models import Category, Channel, SubCategory
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core import serializers
import csv

#vision responsible for redecorating the initial template.
def index(request):
    return render(request, 'importcsv/index.html')

#vision responsible for rendering all the page for manipulation of the template
def api(request):
    allchannel = Channel.objects.all()
    onlycs = Channel.objects.get(pk=1).category_channel.all()[:1]
    context = {
        'allchannel': allchannel,
        'onlycs':onlycs,
    }
    return render(request, 'importcsv/api.html', context)

#vision responsible to do upload the file .csv which includes all categorys
def uploadcsv(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='importcsv/media')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'importcsv/uploadcsv.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'importcsv/uploadcsv.html')

#vision responsible for updating categories and subcategories of a channel that already exists in the database
#or creating a new channel with its categories and sub categories if it does not
def importcategories(request):
    if request.method == 'POST':
        channelalt = request.POST['channel_name']
        channel_filter = Channel.objects.filter(name=channelalt)
        uploaded = UploadedFile(open('importcsv/media/category.csv', 'r'), 'category.csv')
        if len(channel_filter) > 0:
            #update channel
            pk_channel = channel_filter[0].pk
            Channel.objects.get(pk=pk_channel).category_channel.all().delete()

            for [line] in csv.reader(uploaded.file):
                data = line.split('/')
                category_name = data[0]
                subcategory_name = data[1]
                Channel.objects.get(pk=pk_channel).category_channel.create(name=category_name, description='New Category')
                category_filter = Category.objects.filter(name=category_name).latest('id')
                pk_category = category_filter.pk
                Category.objects.get(pk=pk_category).sub_category.create(name=subcategory_name, description='New Sub-Category')

            return render(request, 'importcsv/uploadcsv.html', {
                'category_filter': category_filter
            })
        else:
            #create new channel
            newchannel = Channel(name=channelalt, description='New Channel')
            newchannel.save()
            for [line] in csv.reader(uploaded.file):

                data = line.split('/')
                category_name = data[0]
                subcategory_name = data[1]
                newchannel.category_channel.create(name=category_name, description='New Category')
                category_filter = Category.objects.filter(name=category_name).latest('id')
                pk_category = category_filter.pk
                Category.objects.get(pk=pk_category).sub_category.create(name=subcategory_name, description='New Sub-Category')

            return render(request, 'importcsv/uploadcsv.html', {
                'category_filter': category_filter
            })
