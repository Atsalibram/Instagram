from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
#@login_required(login_url='/accounts/login')
#def homepage (request):
#    current_user = request.user
#    all_images = Image.objects.all()
#    comments = Comments.objects.all()
#    likes = Likes.objects.all()
#    profile = Profile.objects.all()
#    print(likes)
#    return render(request,'home.html',locals())
#