from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string

# creat a dictonary for all months

monthly_challenges  = {
  "january":"eat no meat for entire month!",
  "february":"walk for at least 20 minutes every day!",
  "march":"learn Django for at least 20 minutes every day!",
  "april":"No Retail Shopping",
  "may":"Avoid Social Media While Working",
  "june":"Make One New Connection a Week",
  "july":"Work Breaks into Your Daily Routine",
  "august":"Read a Chapter of a Book a Day",
  "september": "Start a Blog (and Post Once a Week)",
  "october":"Start a YouTube Channel",
  "november":"Try a New Workout At Home",
  "december": None
}

# Creat a First View & URL

def index(request):
       list_items= ""
       list_months = list(monthly_challenges.keys())
       return render(request, "challenges/index.html", {
              "months": list_months
              
       })

def monthly_challeng_bu_number(request, month):
       months_numbers = list(monthly_challenges.keys())
       if month > len(months_numbers):
            return HttpResponseNotFound("<h1>This Month is not Found</h1>")
       redirect_month = months_numbers[month -1]
       redirect_path = reverse("my-challeng", args=[redirect_month])
       return HttpResponseRedirect(redirect_path)

def monthly_challeng(request, month):
       try:
             challenge_text = monthly_challenges[month]
             return render(request, ("challenges/challenge.html"), {
              "text": challenge_text,
              "month_name": month
             })
             # WE CAN USE THE RENDER FUNTION INSTEAD THE RENDER TO STRING FUNTIONS

             #response_text = render_to_string("challenges/challenge.html")
             #return HttpResponse(response_text)
       except:   
             raise Http404()

            

#def index(request):
  #return HttpResponse("This Works!")

#def february(request):
  #return HttpResponse("this also works")

#def monthly_challeng(request, month):
       #challeng_text = None
      # if month == "january":
              #challeng_text = "eat no meat for entire month!"     
       #elif month == "fabruary":
             # challeng_text = "walk for at least 20 minutes every day!" 
       #elif month == "march":
               #challeng_text = "learn Django for at least 20 minutes every day!"
       #else:
              # return HttpResponseNotFound("This month is not supported!")       
      #return HttpResponse(challeng_text)             

# Create your views here.
