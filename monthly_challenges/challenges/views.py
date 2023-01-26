from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
  "december":"Cook a New Recipe a Week"
}

# Creat a First View & URL

def index(request):
       list_items= ""
       list_months = list(monthly_challenges.keys())
       for month in list_months:
        cap_month = month.capitalize()
        month_path = reverse("my-challeng", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{cap_month}</a></li>"
        response_data = f"<ul>{list_items}</ul>"
       return HttpResponse(response_data)

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
             response_text = render_to_string("challenges/challenge.html")
             return HttpResponse(response_text)
       except:   
             return HttpResponseNotFound("<h1>This Month is not supported!</h1>")

            

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
