from django.shortcuts import render, redirect
from pytube import YouTube
# Create your views here.


def index(request):
    """
    In this function we will take the url from the frontend ,
    we will check weather it is a valid url and if valid
    we will print the title of the video and will download the video in the present working directory.
    We can also try to redirect the page to enter the url again , if the page is not valid .
    we will also try to log the status of the video .
    we will be downloading the video with the help of the pytube library.
    After successfully downloading the video we will be redirecting to the home page.
    Further more improvements will be added in the project
    """
    # checking if the method is post
    if request.method == 'POST':
        print("enter hogya!!")
        link = request.POST['link']
        print("chal gya !!")
        # creating the object of the link
        print(link)
        try:
            # object creation using YouTube
            # which was imported in the beginning
            yt = YouTube(link)
        except:
            print("Connection Error")
        print("object_bangya")
        # print(yt.title)
        # print("title ban gya")
        # # Reducing the resolution of the video
        # yt.streams.get_lowest_resolution()
        print("Starting downloading.......")
        yt.streams.first().download()
        print("Download Completed.........")
        # returning to the HTML page
        return render(request, 'index.html')
    return render(request, 'index.html')

