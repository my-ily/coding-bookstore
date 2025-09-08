from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from django.template import loader
import requests
# Create your views here.
from django.shortcuts import get_object_or_404

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Wishlist #from model class
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate , login

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('hero') 


def auth_login(request):
   if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    user=authenticate(request,username=username ,password=password )


    if user is not None:
       login(request,user)
#نقل المستخدم إلى صفحة ثانية (بعد تنفيذ حدث مثل تسجيل دخول
       return redirect("hero")
    
   return render(request,'auth_login.html')  
   

@csrf_exempt
def auth_reg(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # نحفظ المستخدم
            print("✅ النموذج صالح، جاري إنشاء المستخدم")
            login(request, user)  # نسجل دخوله مباشرة
            return redirect('hero')  # نوديه على صفحة الدفع مباشرة مثلاً
        else:
            print("❌ النموذج غير صالح")
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'auth_reg.html', {'form': form})
   #  return HttpResponse(template.render())




@login_required
def wishlist_view(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, "favorites.html", {"books": items})

@login_required
def add_to_wishlist(request, book_id):
    if request.method == "POST":
        title = request.POST.get("title", "")[:255]
        authors = request.POST.get("authors", "")[:255]
        thumbnail = request.POST.get("thumbnail", "")[:500]
        info_link = request.POST.get("infoLink", "")[:500]


     
        if not title:
            return JsonResponse({"status": "error", "message": "Missing title"}, status=400)

        wishlist_item, created = Wishlist.objects.get_or_create(
            user=request.user,
            book_id=book_id,
            defaults={
                "title": title,
                "authors": authors,
                "thumbnail": thumbnail,
                "info_link": info_link
            }
        )

        # if created:
        #     print("✅ Book added to wishlist")
        # else:
        #     print("⚠ Book already in wishlist")
        return redirect("favorites")
    return JsonResponse({"status": "error"}, status=400)


@login_required
def remove_from_wishlist(request, book_id):
    if request.method == "POST":
        Wishlist.objects.filter(user=request.user, book_id=book_id).delete()
    #     return JsonResponse({"status": "ok"})
    # return JsonResponse({"status": "error"}, status=400)
    return redirect("favorites")


def book_detail(request, book_id):
    url = f"https://www.googleapis.com/books/v1/volumes/{book_id}"
    response = requests.get(url)
    data = response.json()

    volume = data.get("volumeInfo", {})

    book = {
        "title": volume.get("title"),
        "authors": ", ".join(volume.get("authors", [])),
        "thumbnail": volume.get("imageLinks", {}).get("thumbnail", "https://via.placeholder.com/100"),
        "description": volume.get("description", "No description available."),
    }

    return render(request, "detail.html", {"book": book, "book_id": book_id})




def hero(request):
    return render(request, 'hero.html')


def Blog(request):
    return render(request ,'Blog.html')


def about(request):
    return render(request ,'about.html')

def favorites(request):
    return render(request ,'favorites.html')


def fetch_books(query, max_results=40, start_index=0):
    import requests
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,
        "maxResults": max_results,
        "startIndex": start_index
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status() 
        data = response.json()
    except Exception as e:
        print("Error fetching books:", e)
        data = {"items": []} 

    books = []
    for item in data.get("items", []):
        volume = item.get("volumeInfo", {})
        books.append({
            "id": item.get("id"),
            "title": volume.get("title"),
            "authors": ", ".join(volume.get("authors", [])),
            "thumbnail": volume.get("imageLinks", {}).get("thumbnail", "https://via.placeholder.com/150")
        })
    return books

def programming_books_view(request):
    books_page1 = fetch_books("programming", max_results=40, start_index=0)
    books_page2 = fetch_books("programming", max_results=40, start_index=40)
    all_books = books_page1 + books_page2
    return render(request, "AllBooks.html", {"all_books": all_books})




