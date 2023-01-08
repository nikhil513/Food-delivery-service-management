from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
from matplotlib import pyplot as plt
# Create your views here .
p = Menu()


listD = [["abhishek","mia2",0,0]]
list  = []
list1 = []
list2 = []
list3 = []
list4 = []
listA = []
listP2 =[]
listP1 =[]
listc = [["cus1","123","c@gmail.com"],["cus2","123","d@gmail.com"]]
listM =[["manager","man123"]]
listR =[["amigos","amigos123","1","Amigos Restaurant"],["pfc","pfc123","2","PAN Loop Food Center"],["citybites","city123","3","City Bites"],
["heritage","her123","4","Heritage Restaurant"],["miamore","mia123","5","Mia more"],]
#Editing Menu for Amigos
def edit(request):
    p.vegA = int(request.GET["veg"])
    p.nonA = int(request.GET["non"])
    p.chicA= int(request.GET["chic"])
    p.fishA = int(request.GET["fish"])
    p.rotiA = int(request.GET["roti"])
    p.saladA = int(request.GET["salad"])
    p.panerA = int(request.GET["pan"])
    p.curryA = int(request.GET["mix"])
    return render(request,"restaurant1.html",{'p_veg':p.vegA, 'p_non':p.nonA, 'p_fish':p.fishA, 'p_chic':p.chicA,
                          'p_roti':p.rotiA, 'p_salad':p.saladA, 'p_pan':p.panerA, 'p_mix':p.curryA,'error':"Successfully edited"})
#Editing Menu for PFC
def edit1(request):
    p.rotiP = int(request.GET["roti"])
    p.chicP = int(request.GET["chic"])
    p.chicfriP= int(request.GET["ch"])
    p.butP = int(request.GET["non"])
    p.friP = int(request.GET["veg"])
    p.babyP = int(request.GET["bab"])
    return render(request,"restaurant2.html",{'proti':p.rotiP, 'pnon':p.butP, 'pbab':p.babyP, 'pveg':p.friP,
     'pch':p.chicfriP, 'pchic':p.chicP})
#Editing Menu for City Bites
def edit2(request):
    p.rotiC = int(request.GET["roti"])
    p.chicC = int(request.GET["chic"])
    p.chicfriC= int(request.GET["ch"])
    p.butC = int(request.GET["non"])
    p.friC = int(request.GET["veg"])
    p.babyC = int(request.GET["bab"])
    return render(request,"restaurant3.html",{'proti':p.rotiC, 'pnon':p.butC, 'pbab':p.babyC, 'pveg':p.friC,
     'pch':p.chicfriC, 'pchic':p.chicC})
#Editing Menu for Heritage
def edit3(request):
    p.rotiH = int(request.GET["roti"])
    p.chicH = int(request.GET["chic"])
    p.chicfriH= int(request.GET["ch"])
    p.butH = int(request.GET["non"])
    p.babyH = int(request.GET["bab"])
    return render(request,"restaurant4.html",{'proti':p.rotiH, 'pnon':p.butH, 'pbab':p.babyH,
     'pch':p.chicfriH, 'pchic':p.chicH})
#Editing Menu for Miamore
def edit4(request):
    p.rotiM = int(request.GET["roti"])
    p.chicM = int(request.GET["chic"])
    p.chicfriM= int(request.GET["ch"])
    p.butM = int(request.GET["non"])
    p.babyM = int(request.GET["bab"])
    return render(request,"restaurant5.html",{'proti':p.rotiM, 'pnon':p.butM, 'pbab':p.babyM,
     'pch':p.chicfriM, 'pchic':p.chicM})

#Redirect to home page
def home(request):
    return render(request, "home.html")
#Redirect to login page
def login(request):
    return render(request, "Login.html")

#To fill details of order
def Amigos(request):
    return render(request,"Amigos.html",{'p_veg':p.vegA, 'p_non':p.nonA, 'p_fish':p.fishA, 'p_chic':p.chicA,
     'p_roti':p.rotiA, 'p_salad':p.saladA, 'p_pan':p.panerA, 'p_mix':p.curryA})
#Finding the total amount and storing details of order
def BillA(request):
    v1 = int(request.GET["veg"])*p.vegA
    v2 = int(request.GET["non"])*p.nonA
    v3 = int(request.GET["chic"])*p.chicA
    v4 = int(request.GET["fish"])*p.fishA
    v5 = int(request.GET["roti"])*p.rotiA
    v6 = int(request.GET["mix"])*p.curryA
    v7 = int(request.GET["pan"])*p.panerA
    v8 = int(request.GET["salad"])*p.saladA
    sum = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8
    
    p.a1 = p.a1 + int(request.GET["veg"])
    p.a2 = p.a2 + int(request.GET["non"])
    p.a3 = p.a3 +int(request.GET["chic"])
    p.a4 = p.a4 + int(request.GET["fish"])
    p.a5 = p.a5 + int(request.GET["roti"])
    p.a6 = p.a6 + int(request.GET["mix"])
    p.a7 = p.a7 + int(request.GET["pan"])
    p.a8 = p.a8 + int(request.GET["salad"])
    if sum == 0:
        return render(request,"Amigos.html",{'p_veg':p.vegA, 'p_non':p.nonA, 'p_fish':p.fishA, 'p_chic':p.chicA,
     'p_roti':p.rotiA, 'p_salad':p.saladA, 'p_pan':p.panerA, 'p_mix':p.curryA, 'error': "Please select atleast one item"})
    sum = float(sum*((100+p.ma-p.da)/100))
    sum = round(sum,2)
    A = "Name :  " + p.name
    p.priceA = sum
    p.nA = p.nA + 1
    k = [" "," ","","",p.name,"","Amigos"]
    list.append(k)
    k = [" "," ","","",p.name,"",A]
    list.append(k)
    k = ["order No ",p.nA,"" , "",p.name,"",""]
    list.append(k)
    k = ["OTP ",p.otp,"","",p.name,"",""]
    list.append(k)
    if v1 != 0:
        k = ["Veg Biraiyani",request.GET["veg"], p.otp, p.nA,p.name,"",""]
        list.append(k)
    if v2 != 0:
        k = ["Chicken Biriyani",request.GET["non"],p.otp, p.nA,p.name,"",""]
        list.append(k)
    if v3 != 0:
        k = ["Chicken curry",request.GET["chic"], p.otp, p.nA,p.name,"",""]
        list.append(k)
    if v4 != 0:
        k = ["Fish Curry",request.GET["fish"], p.otp, p.nA,p.name,"",""]
        list.append(k)
    if v5 != 0:
        k = ["Roti",request.GET["roti"], p.otp, p.nA,p.name,"",""]
        list.append(k)
    if v6 != 0:
        k = ["Mixed Veg Curry",request.GET["mix"], p.otp, p.nA,p.name,"",""]
        list.append(k)
    if v7 != 0:
        k = ["Paneer Biriyani",request.GET["pan"], p.otp, p.nA,p.name,"",""]
        list.append(k)
    if v8 != 0:
        k = ["Onion Salad",request.GET["salad"], p.otp, p.nA,p.name,"",""]
        list.append(k)
    k= [" "," ","","",p.name,sum,"Total"]
    list.append(k)
    k =["------","------","----","----","----","----",""]
    list.append(k)
    p.otp = p.otp + 2
    return render(request,"bill1.html",{'total':sum})

#To fill details of order
def PFC(request):
    return render(request,"PFC.html",{'proti':p.rotiP, 'pnon':p.butP, 'pbab':p.babyP, 'pveg':p.friP,
     'pch':p.chicfriP, 'pchic':p.chicP}) 

#Finding the total amount and storing details of order
def BillP(request):
    u1 = int(request.GET["roti"])*p.rotiP
    u2 = int(request.GET["non"])*p.butP
    u3 = int(request.GET["bab"])*p.babyP
    u4 = int(request.GET["veg"])*p.friP
    u5 = int(request.GET["chic"])*p.chicP
    u6 = int(request.GET["ch"])*p.chicfriP
    k = [p.rotiP,request.GET["roti"],p.butP,request.GET["non"],p.chicP,request.GET["chic"],p.chicfriP,request.GET["ch"],
    p.friP,request.GET["veg"],p.babyP,request.GET["bab"],]
    listP1.append(k)
    p.p1 = p.p1 + int(request.GET["roti"])
    p.p2 = p.p2 + int(request.GET["non"])
    p.p3 = p.p3 +  int(request.GET["bab"])
    p.p4 = p.p4 + int(request.GET["veg"])
    p.p5 = p.p5 + int(request.GET["chic"])
    p.p6 = p.p6 + int(request.GET["ch"])
    net = u1 + u2 + u3 + u4 + u5 + u6
    if net == 0:
        return render(request,"PFC.html", {'proti':p.rotiP, 'pnon':p.butP, 'pbab':p.babyP, 'pveg':p.friP,
     'pch':p.chicfriP, 'pchic':p.chicP})
    net =  float(net*((100+p.mp-p.dp)/100))
    net = round(net,2)
    p.nP = p.nP + 1
    A = "Name :  " + p.name
    k = [" "," ","","",p.name,"","PFC"]
    list1.append(k)
    k = [" "," ","","",p.name,"",A]
    list1.append(k)
    k = ["order No ",p.nP,"","",p.name,"",""]
    list1.append(k)
    k = ["OTP ",p.otp1,"","",p.name,"",""]
    list1.append(k)
    p.otp1 = p.otp1 + 2
    if u1 != 0:
        k = ["Roti",request.GET["roti"],"","",p.name,"",""]
        list1.append(k)
    if u2 != 0:
        k = ["Butter non",request.GET["non"],"","",p.name,"",""]
        list1.append(k)
    if u3 != 0:
        k = ["Baby corn curry",request.GET["bab"],"","",p.name,"",""]
        list1.append(k)
    if u4 != 0:
        k = ["Veg fried Rice",request.GET["veg"],"","",p.name,"",""]
        list1.append(k)
    if u5 != 0:
        k = ["Chicken Tikka",request.GET["chic"],"","",p.name,"",""]
        list1.append(k)
    if u6 != 0:
        k = ["Chicken Fried rice",request.GET["ch"],"","",p.name,"",""]
        list1.append(k)
    k= [" "," ","","",p.name,net,"Total"]
    list1.append(k)
    k =["------","------","----","----","----","----",""]
    list1.append(k)
    p.priceP = net
    return render(request,"bill2.html",{'total':net})

#To fill details of order
def CityBites(request):
    return render(request,"City.html",{'proti':p.rotiC, 'pnon':p.butC, 'pbab':p.babyC, 'pveg':p.friC,
     'pch':p.chicfriC, 'pchic':p.chicC})
    
#Finding the total amount and storing details of order
def BillC(request):
    u1 = int(request.GET["roti"])*p.rotiC
    u2 = int(request.GET["non"])*p.butC
    u3 = int(request.GET["bab"])*p.babyC
    u4 = int(request.GET["veg"])*p.friC
    u5 = int(request.GET["chic"])*p.chicC
    u6 = int(request.GET["ch"])*p.chicfriC
    k = [p.rotiC,request.GET["roti"],p.butC,request.GET["non"],p.chicC,request.GET["chic"],p.chicfriC,request.GET["ch"],
    p.friC,request.GET["veg"],p.babyC,request.GET["bab"],]
    listP1.append(k)
    total = u1 + u2 + u3 + u4 + u5 + u6
    p.c1 = p.c1 + int(request.GET["roti"])
    p.c2 = p.c2 + int(request.GET["non"])
    p.c3 = p.c3 + int(request.GET["bab"])
    p.c4 = p.c4 + int(request.GET["veg"])
    p.c5 = p.c5 + int(request.GET["chic"])
    p.c6 = p.c6 + int(request.GET["ch"])
    if total == 0:
        return render(request,"City.html",{'proti':p.rotiC, 'pnon':p.butC, 'pbab':p.babyC, 'pveg':p.friC,
     'pch':p.chicfriC, 'pchic':p.chicC})
    total = float(total*((100+p.mf-p.df)/100))
    total = round(total,2)
    p.nC = p.nC + 1
    A = "Name :  " + p.name
    k = [" "," ","","",p.name,"","City Bites"]
    list2.append(k)
    k = [" "," ","","",p.name,"",A]
    list2.append(k)
    k = ["order No ",p.nC,"","",p.name,"",""]
    list2.append(k)
    k = ["OTP ",p.otp2,"","",p.name,"",""]
    list2.append(k)
    p.otp2 = p.otp2 + 2
    if u1 != 0:
        k = ["Veg Noodles",request.GET["roti"],"","",p.name,"",""]
        list2.append(k)
    if u2 != 0:
        k = ["Egg Noodles",request.GET["non"],"","",p.name,"",""]
        list2.append(k)
    if u3 != 0:
        k = ["Chicken Noodles",request.GET["bab"],"","",p.name,"",""]
        list2.append(k)
    if u4 != 0:
        k = ["Masala Dosa",request.GET["veg"],"","",p.name,"",""]
        list2.append(k)
    if u5 != 0:
        k = ["Plain Dosa",request.GET["chic"],"","",p.name,"",""]
        list2.append(k)
    if u6 != 0:
        k = ["Onion Dosa",request.GET["ch"],"","",p.name,"",""]
        list2.append(k)
    k= [" "," ","","",p.name,total,"Total"]
    list2.append(k)
    k =["------","------","----","----","----","----",""]
    list2.append(k)
    p.priceC = total
    return render(request,"bill3.html",{'total':total})

#To fill details of order
def Heritage(request):
    return render(request,"Heritage.html",{'proti':p.rotiH, 'pnon':p.butH, 'pbab':p.babyH,
     'pch':p.chicfriH, 'pchic':p.chicH})

#Finding the total amount and storing details of order
def BillH(request):
    u1 = int(request.GET["roti"])*p.rotiH
    u2 = int(request.GET["non"])*p.butH
    u3 = int(request.GET["bab"])*p.babyH
    u5 = int(request.GET["chic"])*p.chicH
    u6 = int(request.GET["ch"])*p.chicfriH
    k = [p.rotiH,request.GET["roti"],p.butH,request.GET["non"],p.chicH,request.GET["chic"],p.chicfriH,request.GET["ch"],
    p.babyH,request.GET["bab"]]
    listP1.append(k)
    total = u1 + u2 + u3 + u5 + u6
    p.h1 = p.h1 + int(request.GET["roti"])
    p.h2 = p.h2 + int(request.GET["non"])
    p.h3 = p.h3 + int(request.GET["bab"])
    p.h4 = p.h4 + int(request.GET["chic"])
    p.h5 = p.h5 +  int(request.GET["ch"])
    if total == 0:
        return render(request,"Heritage.html",{'proti':p.rotiH, 'pnon':p.butH, 'pbab':p.babyH,
     'pch':p.chicfriH, 'pchic':p.chicH})
    total =  float(total*((100+p.mh-p.dh)/100))
    total = round(total,2)
    p.nH = p.nH + 1
    A = "Name :  " + p.name
    k = [" "," ","","",p.name,"","Heritage"]
    list3.append(k)
    k = [" "," ","","",p.name,"",A]
    list3.append(k)
    k = ["order No ",p.nH,"","",p.name,"",""]
    list3.append(k)
    k = ["OTP ",p.otp3,"","",p.name,"",""]
    list3.append(k)
    p.otp3 = p.otp3 + 2
    if u1 != 0:
        k = ["Butter Scotch",request.GET["roti"],"","",p.name,"",""]
        list3.append(k)
    if u2 != 0:
        k = ["StrawBerry",request.GET["non"],"","",p.name,"",""]
        list3.append(k)
    if u3 != 0:
        k = ["Vanilla",request.GET["bab"],"","",p.name,"",""]
        list3.append(k)
    if u5 != 0:
        k = ["Chocolate",request.GET["chic"],"","",p.name,"",""]
        list3.append(k)
    if u6 != 0:
        k = ["Mixed Flavor",request.GET["ch"],"","",p.name,"",""]
        list3.append(k)
    k= [" "," ","","",p.name,total,"Total"]
    list3.append(k)
    k =["------","------","----","----","----","----",""]
    list3.append(k)
    p.priceH = total
    return render(request,"bill4.html",{'total':total})

#To fill details of order
def Miamore(request):
    return render(request,"Miamore.html",{'proti':p.rotiM, 'pnon':p.butM, 'pbab':p.babyM,
     'pch':p.chicfriM, 'pchic':p.chicM})
    
#Finding the total amount and storing details of order
def BillM(request):
    u1 = int(request.GET["roti"])*p.rotiM
    u2 = int(request.GET["non"])*p.butM
    u3 = int(request.GET["bab"])*p.babyM
    u5 = int(request.GET["chic"])*p.chicM
    u6 = int(request.GET["ch"])*p.chicfriM
    k = [p.rotiM,request.GET["roti"],p.butM,request.GET["non"],p.chicM,request.GET["chic"],p.chicfriM,request.GET["ch"],
    p.babyM,request.GET["bab"]]
    listP1.append(k)
    total = u1 + u2 + u3 + u5 + u6
    p.m1 = p.m1 + int(request.GET["roti"])
    p.m2 = p.m2 + int(request.GET["non"])
    p.m3 = p.m3 + int(request.GET["bab"])
    p.m4 = p.m4 + int(request.GET["chic"])
    p.m5 = p.m5 +  int(request.GET["ch"])
    if total == 0:
        return render(request,"Miamore.html",{'proti':p.rotiM, 'pnon':p.butM, 'pbab':p.babyM,
     'pch':p.chicfriM, 'pchic':p.chicM})
    total =  float(total*((100+p.mm-p.dm)/100))
    total = round(total,2)
    p.nM = p.nM + 1
    A = "Name :  " + p.name
    k = [" "," ","","",p.name,"","Mia more"]
    list4.append(k)
    k = [" "," ","","",p.name,"",A]
    list4.append(k)
    k = ["order No ",p.nM,"","",p.name,"",""]
    list4.append(k)
    k = ["OTP ",p.otp4,"","",p.name,"",""]
    list4.append(k)
    p.otp4 = p.otp4 + 2
    if u1 != 0:
        k = ["Dark Chocolate",request.GET["roti"],"","",p.name,"",""]
        list4.append(k)
    if u2 != 0:
        k = ["Black Forest",request.GET["non"],"","",p.name,"",""]
        list4.append(k)
    if u3 != 0:
        k = ["Chocolate cake",request.GET["bab"],"","",p.name,"",""]
        list4.append(k)
    if u5 != 0:
        k = ["Caramel Cake",request.GET["chic"],"","",p.name,"",""]
        list4.append(k)
    if u6 != 0:
        k = ["OreO",request.GET["ch"],"","",p.name,"",""]
        list4.append(k)
    k= [" "," ","","",p.name,total,"Total"]
    list4.append(k)
    k =["------","------","----","----","----","----",""]
    list4.append(k)
    p.priceM = total
    return render(request,"bill5.html",{'total':total})

#Finding previous orders of amigos
def requests(request):
    if p.nA != 0:
        return render(request,"Request.html",{'list': list})
    else :
        return render(request,"Request.html",{'list': list, 'error':"no previous history found"})

#Findings previous orders of pfc
def requests1(request):
    if p.nP != 0:
        return render(request,"Request1.html",{'list': list1})
    else :
        return render(request,"Request1.html",{'list': list1, 'error':"no previous history found"})

#Findings previous orders of city bites
def requests2(request):
    if p.nC != 0:
        return render(request,"Request2.html",{'list': list2})
    else :
        return render(request,"Request2.html",{'list': list2, 'error':"no previous history found"})

#Findings previous orders of heritage
def requests3(request):
    if p.nH != 0:
        return render(request,"Request3.html",{'list': list3})
    else :
        return render(request,"Request3.html",{'list': list3, 'error':"no previous history found"})

#Findings previous orders of miamore
def requests4(request):
    if p.nM != 0:
        return render(request,"Request4.html",{'list': list4})
    else :
        return render(request,"Request4.html",{'list': list4, 'error':"no previous history found"})

#Printing bar graph of total food items sold by amigos for amigos
def stats(request):
    b =['Veg Biryani','Chicken Biryani','Chicken Curry','Fish Curry','Roti','Mixed Veg curry','Paneer Biryani','Onion Salad']
    a =[p.a1,p.a2,p.a3,p.a4,p.a5,p.a6,p.a7,p.a8]
    plt.bar(b, a)
    plt.show()
    return render(request,"restaurant1.html",{'p_veg':p.vegA, 'p_non':p.nonA, 'p_fish':p.fishA, 'p_chic':p.chicA,
                          'p_roti':p.rotiA, 'p_salad':p.saladA, 'p_pan':p.panerA, 'p_mix':p.curryA})

#Printing bar graph of total food items sold by amigos for manager
def statsMa(request):
    b =['Veg Biryani','Chicken Biryani','Chicken Curry','Fish Curry','Roti','Mixed Veg curry','Paneer Biryani','Onion Salad']
    a =[p.a1,p.a2,p.a3,p.a4,p.a5,p.a6,p.a7,p.a8]
    plt.bar(b, a)
    plt.show()
    return render(request,"manager.html")

#Printing bar graph of total food items sold by pfc for pfc
def stats1(request):
    b =['Roti','Butter Non','Baby Corn Curry','Veg Fried Rice','Chicken Tikka','Chicken Fried Rice',]
    a =[p.p1,p.p2,p.p3,p.p4,p.p5,p.p6,]
    plt.bar(b, a)
    plt.show()
    return render(request,"restaurant2.html",{'proti':p.rotiP, 'pnon':p.butP, 'pbab':p.babyP, 'pveg':p.friP,
     'pch':p.chicfriP, 'pchic':p.chicP})

#Printing bar graph of total food items sold by pfc for manager
def statsMp(request):
    b =['Roti','Butter Non','Baby Corn Curry','Veg Fried Rice','Chicken Tikka','Chicken Fried Rice',]
    a =[p.p1,p.p2,p.p3,p.p4,p.p5,p.p6,]
    plt.bar(b, a)
    plt.show()
    return render(request,"manager.html")

#Printing bar graph of total food items sold by city bites for city bites
def stats2(request):
    b =['Veg Noodles','Egg Noodles','Chicken Noodles','Masala Dosa','Plain Dosa','Onion Dosa',]
    a =[p.c1,p.c2,p.c3,p.c4,p.c5,p.c6,]
    plt.bar(b, a)
    plt.show()
    return render(request,"restaurant3.html",{'proti':p.rotiC, 'pnon':p.butC, 'pbab':p.babyC, 'pveg':p.friC,
     'pch':p.chicfriC, 'pchic':p.chicC})

#Printing bar graph of total food items sold by citybites for manager
def statsMc(request):
    b =['Veg Noodles','Egg Noodles','Chicken Noodles','Masala Dosa','Plain Dosa','Onion Dosa',]
    a =[p.c1,p.c2,p.c3,p.c4,p.c5,p.c6,]
    plt.bar(b, a)
    plt.show()
    return render(request,"manager.html",)

#Printing bar graph of total food items sold by heritage for heritage
def stats3(request):
    b =['Butter Scotch','Strawberry','Vanilla','Chocolate','Mixed Flavour',]
    a =[p.h1,p.h2,p.h3,p.h4,p.h5,]
    plt.bar(b, a)
    plt.show() 
    return render(request,"restaurant4.html",{'proti':p.rotiH, 'pnon':p.butH, 'pbab':p.babyH,
     'pch':p.chicfriH, 'pchic':p.chicH})

#Printing bar graph of total food items sold by heritage for manager
def statsMh(request):
    b =['Butter Scotch','Strawberry','Vanilla','Chocolate','Mixed Flavour',]
    a =[p.h1,p.h2,p.h3,p.h4,p.h5,]
    plt.bar(b, a)
    plt.show() 
    return render(request,"manager.html")

#Printing bar graph of total food items sold by Miamore for Miamore
def stats4(request):
    b =['Dark Chocolate','Black Forest','Chocolate Cake','Caramel cake','Oreo',]
    a =[p.m1,p.m2,p.m3,p.m4,p.m5,]
    plt.bar(b, a)
    plt.show() 
    return render(request,"restaurant5.html",{'proti':p.rotiM, 'pnon':p.butM, 'pbab':p.babyM,
     'pch':p.chicfriM, 'pchic':p.chicM})

#Printing bar graph of total food items sold by maimore for miaamore
def statsMm(request):
    b =['Dark Chocolate','Black Forest','Chocolate Cake','Caramel cake','Oreo',]
    a =[p.m1,p.m2,p.m3,p.m4,p.m5,]
    plt.bar(b, a)
    plt.show() 
    return render(request,"manager.html",)

#For signin for different users
def user(request):
    if (request.GET["User type"] == 'Customer'):
        c1 = request.GET["username"]
        c2 = request.GET["pass"]
        g = 0
        for i in listc:
            if c1 == i[0] and c2 == i[1] :
                g = 1
                p.name = c1
                return render(request,"base.html",{'rating1':p.ra,'rating4':p.rh,'rating2':p.rp,'rating3':p.rf,'rating5':p.rm,'name':p.name})
        if g!=1:  
            return render(request,"Login.html",{'error':"Invalid Creditionals"})
    else :
        if(request.GET["User type"] == 'restaurants'):
            a1 = request.GET["username"]
            a2 = request.GET["pass"]
            for i in listR:
                if a1 == i[0] and a2 == i[1] :
                    if i[2] == '1':
                        return render(request,"restaurant1.html",{'p_veg':p.vegA, 'p_non':p.nonA, 'p_fish':p.fishA, 'p_chic':p.chicA,
                        'p_roti':p.rotiA, 'p_salad':p.saladA, 'p_pan':p.panerA, 'p_mix':p.curryA})
                    if i[2] == '2':
                        return render(request,"restaurant2.html",{'proti':p.rotiP, 'pnon':p.butP, 'pbab':p.babyP, 'pveg':p.friP,
                        'pch':p.chicfriP, 'pchic':p.chicP})
                    if i[2] == '3':
                        return render(request,"restaurant3.html",{'proti':p.rotiC, 'pnon':p.butC, 'pbab':p.babyC, 'pveg':p.friC,
                        'pch':p.chicfriC, 'pchic':p.chicC})
                    if i[2] == '4':
                        return render(request,"restaurant4.html",{'proti':p.rotiH, 'pnon':p.butH, 'pbab':p.babyH,
                        'pch':p.chicfriH, 'pchic':p.chicH})
                    if i[2] == '5':
                        return render(request,"restaurant5.html",{'proti':p.rotiM, 'pnon':p.butM, 'pbab':p.babyM,
                        'pch':p.chicfriM, 'pchic':p.chicM})
            
            return render(request,"Login.html",{'error':"Invalid Creditionals"})
        if (request.GET["User type"] == 'Manager'):
            m1 = request.GET["username"]
            m2 = request.GET["pass"]
            if m1 == listM[0][0] and m2 == listM[0][1]:
                return render(request,"manager.html")
            else:
                return render(request,"Login.html",{'error':"Invalid Creditionals"})
        if (request.GET["User type"] == 'Delivery agent'):
            c1 = request.GET["username"]
            c2 = request.GET["pass"]
            g = 0
            for i in listD:
                if c1 == i[0] and c2 == i[1] :
                    g = 1
                    p.named = c1
                    return render(request,"deliveryagent.html",{'name':p.named})
                if g!=1:  
                    return render(request,"Login.html",{'error':"Invalid Creditionals"})


#for signup for different users
def signup(request):
    if (request.GET["User Type"] == 'Customer'):
        return render(request,"signup.html")
    else: 
        return render(request,"signupd.html")

#storing details of new customer registered
def create(request):
    e1 = request.GET["email"]
    e2 = request.GET["Username"]
    e3 = request.GET["psw"]
    if e1[-10:] != "@gmail.com":
        return render(request,"signup.html",{'error':"Invalid Email"})
    else:
        for i in listc:
            if i[2] == e1:
                return render(request,"signup.html",{'error':"Email already exists"})  
        e = [e2,e3,e1]
        listc.append(e)
        return render(request,"Login.html")

#storing details of new delivery agent registered
def create1(request):
    e1 = request.GET["email"]
    e2 = request.GET["Username"]
    e3 = request.GET["psw"]
    if e1[-10:] != "@gmail.com":
        return render(request,"signupd.html",{'error':"Invalid Email"})
    else:
        for i in listc:
            if i[2] == e1:
                return render(request,"signupd.html",{'error':"Email already exists"})  
        e = [e2,e3,e1,0,0]
        listD.append(e)
        return render(request,"Login.html")

#function to edit tax and discounts by manager
def edittax(request):
    return render(request,"taxdis.html",{'v':p.ma,'s':p.da,'p':p.mp,'m':p.dp,'n':p.mf,
    'g':p.df,'d':p.mh,'a':p.dh,'x':p.mm,'o':p.dm})

#storing the changes made by manager 
def save(request):
    p.ma = request.GET["v"]
    p.da = request.GET["s"]
    p.mp = request.GET["p"]
    p.dp = request.GET["m"]
    p.mf = request.GET["n"]
    p.df = request.GET["g"]
    p.mh = request.GET["d"]
    p.dh = request.GET["a"]
    p.mm = request.GET["x"]
    p.dm = request.GET["o"]
    return render(request,"saved.html")

#Back to manager page
def back(request):
    return render(request,"manager.html")
#Back to login
def back1(request):
    return render(request,"Login.html")
#Back to base page
def back2(request):
    return render(request,"base.html",{'rating1':p.ra,'rating4':p.rh,'rating2':p.rp,'rating3':p.rf,'rating5':p.rm,'name':p.name})
#Back to base page
def back3(request):
    return render(request,"base.html",{'rating1':p.ra,'rating4':p.rh,'rating2':p.rp,'rating3':p.rf,'rating5':p.rm,'name':p.name})
#Back to base page
def back4(request):
    return render(request,"base.html",{'rating1':p.ra,'rating4':p.rh,'rating2':p.rp,'rating3':p.rf,'rating5':p.rm,'name':p.name})
#Back to base page
def back5(request):
    return render(request,"base.html",{'rating1':p.ra,'rating4':p.rh,'rating2':p.rp,'rating3':p.rf,'rating5':p.rm,'name':p.name})
#Back to base page
def back6(request):
    return render(request,"base.html",{'rating1':p.ra,'rating4':p.rh,'rating2':p.rp,'rating3':p.rf,'rating5':p.rm,'name':p.name})
#Back to amigos page
def back7(request):
    return render(request,"restaurant1.html",{'p_veg':p.vegA, 'p_non':p.nonA, 'p_fish':p.fishA, 'p_chic':p.chicA,
                          'p_roti':p.rotiA, 'p_salad':p.saladA, 'p_pan':p.panerA, 'p_mix':p.curryA})
#Back to pfc page
def back8(request):
    return render(request,"restaurant2.html",{'proti':p.rotiP, 'pnon':p.butP, 'pbab':p.babyP, 'pveg':p.friP,
     'pch':p.chicfriP, 'pchic':p.chicP})
#Back to city bites 
def back9(request):
    return render(request,"restaurant3.html",{'proti':p.rotiC, 'pnon':p.butC, 'pbab':p.babyC, 'pveg':p.friC,
     'pch':p.chicfriC, 'pchic':p.chicC})
#Back to heritage
def back10(request):
    return render(request,"restaurant4.html",{'proti':p.rotiH, 'pnon':p.butH, 'pbab':p.babyH,
     'pch':p.chicfriH, 'pchic':p.chicH})
#Back to miamore
def back11(request):
    return render(request,"restaurant5.html",{'proti':p.rotiM, 'pnon':p.butM, 'pbab':p.babyM,
     'pch':p.chicfriM, 'pchic':p.chicM}) 
#Back to manager home page
def back12(request):
    return render(request,"manager.html")
#Back to manager home page
def back13(request):
    return render(request,"manager.html") 
#Back to manager home page
def back14(request):
    return render(request,"base.html",{'rating1':p.ra,'rating4':p.rh,'rating2':p.rp,'rating3':p.rf,'rating5':p.rm,'name':p.name})
#Back to manager home page
def back15(request):
    return render(request,"manager.html") 

#Back to Login home page
def logout(request):
    return render(request,"Login.html")

#Function to see list of customers by manager
def seecus(request):
    return render(request,"customer.html",{'list':listc})

#Function to see list of restaurants by manager
def seeres(request):
    return render(request,"restaurants.html",{'list':listR})

#Function to see list of deliveryagents by manager
def seedel(request):
    return render(request,"deliveryagents.html",{'list':listD})

#Function to rate restaurant and delivery agent
def review1(request):
    if p.nA != 0:
        if int(request.GET["r"]) <6 and int(request.GET["r"]) >0 and int(request.GET["d"]) <6 and int(request.GET["d"]) >0:
            p.ra = ( p.ra * p.nA + int(request.GET["r"]))/(p.nA + 1)
            p.ra = round(p.ra,2)
            return render(request,"base.html",{'rating1':p.ra,'rating4':p.rh,'rating2':p.rp,'rating3':p.rf,'rating5':p.rm,'name':p.name})
        else :
            return render(request,"bill1.html",{'total': p.priceA,'error':"rate between 1 to 5"})

#Function to rate restaurant and delivery agent
def review2(request):
    if p.nP != 0:
        if int(request.GET["r"]) <6 and int(request.GET["r"]) >0:
            p.rp = ( p.rp * p.nP + int(request.GET["r"]))/(p.nP + 1)
            p.rp = round(p.rp,2)
            return render(request,"base.html",{'rating1':p.ra,'rating4':p.rh,'rating2':p.rp,'rating3':p.rf,'rating5':p.rm,'name':p.name})
        else :
            return render(request,"bill2.html",{'total': p.priceP,'error':"rate between 1 to 5"})

#Function to rate restaurant and delivery agent
def review4(request):
    if p.nH != 0:
        if int(request.GET["r"]) <6 and int(request.GET["r"]) >0:
            p.rh = ( p.rh * p.nH + int(request.GET["r"]))/(p.nH + 1)
            p.rh = round(p.rh,2)
            return render(request,"base.html",{'rating1':p.ra,'rating4':p.rh,'rating2':p.rp,'rating3':p.rf,'rating5':p.rm,'name':p.name})
        else :
            return render(request,"bill4.html",{'total': p.priceH,'error':"rate between 1 to 5"})

#Function to rate restaurant and delivery agent
def review3(request):
    if p.nC != 0:
        if int(request.GET["r"]) <6 and int(request.GET["r"]) >0:
            p.rf = ( p.rf * p.nC + int(request.GET["r"]))/(p.nC + 1)
            p.rf = round(p.rf,2)
            return render(request,"base.html",{'rating1':p.ra,'rating4':p.rh,'rating2':p.rp,'rating3':p.rf,'rating5':p.rm,'name':p.name})
        else :
            return render(request,"bill3.html",{'total': p.priceC,'error':"rate between 1 to 5"})

#Function to rate restaurant and delivery agent
def review5(request):
    if p.nM != 0:
        if int(request.GET["r"]) <6 and int(request.GET["r"]) >0:
            p.rm = ( p.rm * p.nM + int(request.GET["r"]))/(p.nM + 1)
            p.rm = round(p.rm,2)
            return render(request,"base.html",{'rating1':p.ra,'rating4':p.rh,'rating2':p.rp,'rating3':p.rf,'rating5':p.rm,'name':p.name})
        else :
            return render(request,"bill5.html",{'total': p.priceM,'error':"rate between 1 to 5"})

#Function to see previous orders made by a particular customers        
def prevorders(request):
    prevorders1 = []
    for i in list:
        if list and i[4] == p.name:
            k =["Amigos","","","",""]
            prevorders1.append(k)
            break
    for i in list :
        if p.name == i[4] :
            k = [i[0],i[1],i[2],i[3],i[4]]
            prevorders1.append(k)
    for i in list1:
        if list1 and i[4] == p.name:
            k =["PFC","","","",""]
            prevorders1.append(k)
            break        
    for i in list1 :
        if p.name == i[4] :
            k = [i[0],i[1],i[2],i[3],i[4]]
            prevorders1.append(k)
    for i in list2:
        if list2 and i[4] == p.name:
            k =["City Bites","","","",""]
            prevorders1.append(k)
            break
    for i in list2 :
        if p.name == i[4] :
            k = [i[0],i[1],i[2],i[3],i[4]]
            prevorders1.append(k)
    for i in list3:
        if list3 and i[4] == p.name:
            k =["Heritage","","","",""]
            prevorders1.append(k)
            break
    for i in list3 :
        if p.name == i[4] :
            k = [i[0],i[1],i[2],i[3],i[4]]
            prevorders1.append(k)
    for i in list4:
        if list4 and i[4] == p.name:
            k =["Miamore","","","",""]
            prevorders1.append(k)
            break
    for i in list4 :
        if p.name == i[4] :
            k = [i[0],i[1],i[2],i[3],i[4]]
            prevorders1.append(k)
    return render(request,"prevorders.html",{'list1':prevorders1})

#Printing bills by amigos
def printbill1(request):
    return render(request,"printbill1.html",{'list':list})
#Printing bills by pfc 
def printbill2(request):
    return render(request,"printbill1.html",{'list':list1})
#Printing bills by city bites
def printbill3(request):
    return render(request,"printbill1.html",{'list':list2})
#Printing bills by heritage
def printbill4(request):
    return render(request,"printbill1.html",{'list':list3})
#Printing bills by miamore
def printbill5(request):
    return render(request,"printbill1.html",{'list':list4})
  







