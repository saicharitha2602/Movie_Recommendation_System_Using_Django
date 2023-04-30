from django.db.models import Q
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from .import forms
from .forms import RegistrationForm, CategoryForm, MovieForm
from .models import User, Category, Movie, SearchHistory


def indexfunction(request):
    return HttpResponse("Index Page")

def checkadmin(request):
    if request.method == "POST":
        aid = request.POST['aid']
        apwd = request.POST['apwd']
        if aid == 'admin' and apwd == 'admin':
            return redirect("adminhome")
        else:
            return HttpResponse("LoginInvalid")

def adminhome(request):
    return render(request, "adminhome.html")

def userlogin(request):
    return render(request, "userlogin.html")

def checkuser(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        # select * from user_table where username=uname and password=pwd
        flag=User.objects.filter(Q(username__iexact=uname) & Q(password__iexact=pwd)) # returns object if present
        if flag:
            request.session['uname']=uname #creating session object
            return redirect("userhome")
        else:
            return HttpResponse("Login Invalid")
    else:
        return render("userlogin.html")
    return render("userlogin.html")

def userreg(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # all values in form are saved to table
            return redirect('userlogin')
    else:
        form = RegistrationForm()
    return render(request, 'userreg.html', {'form': form})

def adminlogin(request):
    return render(request, "adminlogin.html")

def userhome(request):
    uname=request.session['uname'] #retrieving session variable
    return render(request, "userhome.html",{'uname':uname})

def addcategory(request):
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()  # all values in form are saved to table
            return HttpResponse("category added successfully")
    else:
        form = CategoryForm()
    return render(request, 'addcategory.html', {'form': form})


def viewcategory(request):
    category=Category.objects.all() # select from user_table
    count=Category.objects.all().count() #select count(*) from user_table
    return render(request, "viewcategory.html",{'category':category,'count':count})

def addmovie(request):
    """categories = forms.ModelChoiceField(queryset=Category.objects.all())"""
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form1 = form.save(commit=False)
            temp1 = request.POST.get('Genre')
            print(temp1)
            temp2=Category.objects.get(id=temp1)
            form1.Genre_name=temp2.category
            hero= request.POST['hero']
            heroine = request.POST['heroine']
            if hero=='':
                form1.hero='NA'
            if heroine=='':
                form1.heroine='NA'
            form1.save()
            """return HttpResponse("Movie added successfully")"""
            return render(request,"success.html")
    else:
        form = MovieForm()
    return render(request, 'addmovie.html', {'form': form})

def viewmovies(request):
    movies = Movie.objects.all()
    count = Movie.objects.all().count()
    return render(request, "viewmovies.html", {'movies': movies,'count':count})

def search(request):
    uname = request.session['uname']
    if request.method == "POST":
        search = request.POST.get('search_item')
        # select * from user_table where username=uname and password=pwd
        flag=Movie.objects.filter(Q(movie_name__icontains=search) | Q(hero__icontains=search) | Q(heroine__icontains=search) |Q(Genre_name__icontains=search))
 # returns object if present
        if flag:
            results=Movie.objects.filter(Q(movie_name__icontains=search) | Q(hero__icontains=search) | Q(heroine__icontains=search) |Q(Genre_name__icontains=search))
            for r in results:
                form=SearchHistory()
                form.username=uname
                form.movie_name=r.movie_name
                form.hero=r.hero
                form.heroine=r.heroine
                form.Director=r.Director
                form.Genre_name=r.Genre_name
                form.save()
            return render(request,"searchresults.html",{"results":results})
        else:
            return HttpResponse("Search Not Found")
    else:
        return render(request,"search.html")
    return render(request,"search.html")

def userlog(request):
    uname = request.session['uname']
    userlog=SearchHistory.objects.filter(username=uname)
    return render(request, "userlog.html", {'userlog': userlog})

def analysis(request):
    uname = request.session['uname']
    categories=Category.objects.all()
    userlog = SearchHistory.objects.filter(username=uname)
    frequency=[]
    for i in categories:
        count=0
        for j in userlog:
            if i.category==j.Genre_name:
                count=count+1
        frequency.append(count)
        zippedList = zip(categories, frequency)
    return render(request,"analysis.html",{'zippedList':zippedList})

def recommendations(request):
    uname = request.session['uname']
    #fetch top 10 observations
    temp=SearchHistory.objects.filter(username=uname).order_by('-timestamp')[:10]
    count=temp.count()
    list=[]
    #if no.of rows<10,fetch top 5 movies based on ratings
    if count<10:
        list.append(Movie.objects.all().order_by('-Rating')[:5])
    else:
        #get the frequency of each category from search log
        l1=[]
        l2=[]
        l3=[]
        categories = Category.objects.all()
        for i in categories:
            count=0
            for j in temp:
                if i.category==j.Genre_name:
                    count=count+1
            #based on frequency,add the genre to respective cluster
            if count>=7:
                l3.append(i)
            elif count>=3 and count<7:
                l2.append(i)
            else:
                l1.append(i)
        #conditions to check which clusters are created
        if len(l3)>0:
            cluster=l3
        elif len(l2)>0:
            cluster=l2
        else:
            cluster=l3
        list=[]
        #based on cluster created,fetch top3 movies from each genre
        for i in cluster:
            res=Movie.objects.filter(Genre_name=i).order_by('-Rating')[:3]
            list.append(res)
    return render(request,"sample.html",{'list':list})

def viewdetails(request,id):
    movie=Movie.objects.get(id=id)
    return render(request,"movie.html",{'movie':movie})

def adminlogout(request):
    return render(request, "adminlogin.html")

def userlogout(request):
    return render(request, "userlogin.html")


