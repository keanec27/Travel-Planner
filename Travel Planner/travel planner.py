import webbrowser
countries=["Australia","Japan","France","South Africa",
           "Italy","Indonesia","Spain","United States of America",
           "Greece","South America","West Africa","East Africa",
           "North Africa","Georgia","Russia","China(Not Available due to Corona virus)",
           "Turkey","Philippines","New Zealand","Thailand",
           "Norway","Vietnam"]

my_dict={"Australia":["Sydney","Melbourne","Canberra","Perth","Brisbane"],
         "Japan":["Tokyo","Kyoto","Yokohama","Hiroshima","Nagasaki"],
         "France":["Paris","Cannes","Lyon","Marseille","Lyon"],
         "South Africa":["Cape Town","Bloemfontein","Durban","East London","Johannesburg",],
         "Italy":["Rome","Venice","Florence","Pisa","Naples"],
          "Indonesia":["Bali","Ubud","Jakarta","Kuta"],
         "Spain":["Barcelona","Madrid","Seville","Granada","Valencia"],
         "United States of America":["New York","Los Angeles","Las Vegas","San Francisco","Washington, D.C."],
         "Greece":["Athens","Santorini","Mykonos","Crete Region","Rhodes"],
         "South America":["Brazil","Chile","Argentina","Colombia","Peru"],
         "West Africa":["Nigeria","Benin"," Burkina Faso", "Cameroon", "Cabo Verde"],
         "East Africa":["Tanzania", "Kenya", "Uganda", "Rwanda"," Burundi","South Sudan"],
          "North Africa":["Plazas de soberanía","Ceuta","Melilla","Canary Islands","Madeira"],
         "Georgia":["Tbilisi","Batumi","Mtskheta","Stepantsminda","Kutaisi"],
         "Russia":["Moscow","Saint Petersburg","Lake Baikal","Kazan","Yekaterinburg"],
         "China(Not Available due to Corona virus)":["Beijing","Shanghai","Chengdu","Guangzhou","Lhasa"],
         "Turkey":["Istanbul","Cappadocia","Pamukkale","Antalya","Izmir"],
         "Philippines":["Manila","Boracay","Cebu City","Bohol","El Nido"],
         "New Zealand":["Milford Sound","Mount Cook","Waitomo","Lake Tekapo","Franz Josef Glacier"],
         "Thailand":["Bangkok","Phuket","Ko Samui","Pattaya City","Ko Tao"],
         "Norway":["Oslo","Bergen","Tromso","Geirangerfjord","Flam"],
         "Vietnam":["Hạ Long Bay","Ho Chi Minh City","Hanoi","Hoi An","Hue"]}

hotelname=""
planename=""

print("***********************")

print("*WELCOME TO TRIP PLANNER*")

print("***********************\n")

name=input("Hello there! What is your name? ")

print("\nOh hey, "+name+"! Nice to meet you!")

print("\nOur services extend to various countries. Right now, we can offer you a quality time in one of the following:\n")

i=1

for c in my_dict.keys():
     print(str(i)+". "+str(c))
     i+=1
     print()

country=int(input("So, which country are you interested in? Please type in the index number: "))

my_country=countries[country-1]

print()

print(my_country+" is an amazing choice indeed! In "+my_country+" we offer a tour in one of the following cities:\n")
i=1
for v in my_dict[my_country]:
    print(str(i)+". "+str(v))
    i+=1
print()

city=int(input("So tell us! Which city do you plan do go to? Enter its index number: "))
my_city=my_dict[my_country][city-1]

print()

print("So you want to go to "+my_city+"? That is an awesome choice!")
info=input("Do you want to know more about "+my_city+"?(Y/N) ")

if(info=='y' or info=='Y'):
    url_city="https://en.wikipedia.org/wiki/"+my_city
    webbrowser.open_new_tab(url_city)
elif(info=='n' or info=='N'):
    print("It seems you already know about "+my_city+"! Awesome")
nop=int(input("\nSo, "+name+". You must be bringing along a few people atleast, right? To help us plan your trip better, "
                            "please tell us how many people you're bringing with you: "))
if(nop==0):
    print("\nOh! So it's more like a solo trip!")
else:
    print("\nOh so it's the "+str(nop+1)+" going together! All of you will have a great time together!")

days=int(input("For how many days are you planning to stay in "+my_city+"?" ))
budget=int(input("\nHow much money in AED are you planning to carry? "))

if(country==1):
    factor=0.40

elif(country==2):
    factor=29.64

elif(country==3):
    factor=0.25

elif(country==4):
    factor=4.03

elif(country==5):
    factor=0.25

elif(country==6):
    factor=3,735.40

elif(country==7):
    factor=0.25

elif(country==8):
    factor=0.27

elif(country==9):
    factor=0.25

elif(country==10):
    factor=1.16

elif(country==11):
    factor=0.41

elif(country==12):
    factor=628.673

elif(country==13):
    factor=159.54

elif(country==14):
    factor=0.77

elif(country==15):
    factor=17.18

elif(country==16):
    factor=1.90

elif(country==17):
    factor=1.62

elif(country==18):
    factor=13.81

elif(country==19):
    factor=0.42

elif (country ==20):
    factor=8.43

elif (country ==21):
    factor=2.51

elif (country ==22):
    factor=6329.01

print(str(budget)+" AED is around "+str(int(budget*factor))+" in "+my_country+"'s native currency")
if budget<500000:
    print("\nThis much money is sufficient! You'll spend around "+str(int(budget*factor/days))+" per day on average.")
else:
    print("\nThis much money is more than enough for you to enjoy this trip to the fullest!")
hotelbooked=False
print("\nNow let's see the Hotel's where you could be staying for the trip!")
choice=input("Shall we? (Y/N)")

def book_hotel(choice):
    global hotelbooked
    global hotelname
    if(choice=='N' or choice=='n'):
        print("\nOkay then we'll come back to this step later on!")
    elif(choice=='y' or choice=='Y'):
        print("\nWhich of the following sites do you prefer?")
        site = int(input("1.Le Meridien\n2.Marriott\n3.Hilton\n4.Booking.com\n5.trivago\n6.Yatra.com\nChoice: "))
        if (site == 1):
            url = "https://le-meridien.marriott.com/"
            hotelname="Le Meridien"
        elif (site == 2):
            url = "https://www.marriott.com/default.mi"
            hotelname="Marriott"
        elif (site == 3):
            url = "https://explorehotels.hilton.com/en_gb/landing/?location=25.204663,55.27077&radius=25&title=Dubai,_UAE&tracking=OM,MB,DLP_EMEAx&campaign_id=Default&WT.srch=1&WT.mc_id=zIMDPDA0EMEA1MB2PSH3PPC_Google_search4cid992557122_aid49269459516_me_kkwd-3645597134375Brand_Cluster6MULTIBR7en&utm_source=Google&utm_medium=ppc&utm_campaign=paidsearch&campaignid=992557122&adgroupid=49269459516&targetid=kwd-364559713437&gclsrc=aw.ds&"
            hotelname="Hilton"
        elif (site == 4):
            url = "https://www.booking.com/index.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaAKIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4ArHIs-wFwAIB;sid=f1581273cee9c93549cda1462e8dbff6;keep_landing=1&sb_price_type=total&"

        elif(site==5):
            url = "https://www.trivago.ae/"

        elif (site == 6):
            url = "https://www.yatra.com/ae"
        info2 = input("Proceed to webiste?(Y/N) ")
        if (info2 == 'y' or info2 == 'Y'):
            webbrowser.open_new_tab(url)
        hotelbooked=True

book_hotel(choice)

print("\nNow let's go ahead and book the tickets.")

flightbooked=False

def book_flight():
    global flightbooked
    global planename
    print("\nWhich of the following sites do you prefer?")

    site=int(input("1.Emirates\n2.Etihad\n3.Lufthansa\n4.Singapore Airlines\n5.Private Jet\n6.Qantas Airways\n7.Qatar Airways \nChoice: "))

    if(site==1):
        url="https://fly4.emirates.com/CAB/IBE/SearchAvailability.aspx?gclid=Cj0KCQiApt_xBRDxARIsAAMUMu9rS8VKCywDOj7bKgmxwpcgDArpLZhNA3w2yJnzE9mmgab9gnT0xgQaAto-EALw_wcB&gclsrc=aw.ds"
        planename="Emirates"
    elif(site==2):
        url="https://www.etihad.com/en-ae/?CID=PPC-UAE-GOOGLE&gclid=Cj0KCQiApt_xBRDxARIsAAMUMu-jkAsA8lfNkBbfxL9jiWkNuZZhwh9M44SGX2XwPnb9pWHXMl-CmMgaAt2bEALw_wcB&gclsrc=aw.ds"
        planename="Etihad"
    elif(site==3):
        url="https://www.lufthansa.com/ae/en/flight-search"
        planename="Lufthansa"
    elif(site==4):
        url="https://www.singaporeair.com/en_UK/sg/home?ds_rl=1245134&ds_rl=1245134&gclid=Cj0KCQiApt_xBRDxARIsAAMUMu9kdeQoZWf1DGQcTEXUmd8BPZrdT3karES6ikPm6W6s4sTdJAqW5vsaAnqfEALw_wcB&gclsrc=aw.ds#/book/bookflight"
        planename="Singapore Airlines"
    elif(site==5):
        url="https://privatejetcharter.ae/"
        planename="Private Jet"
    elif (site == 6):
        url = "https://www.qantas.com/us/en.html"
        planename = "Qantas Airways"
    elif (site == 7):
        url = "www.qatarairways.com/"
        planename = "Qatar Airways"

    info2=input("Proceed to webiste?(Y/N) ")
    if(info2=='y' or info2=='Y'):
        webbrowser.open_new_tab(url)
        book=input("\nDid you find your desired seat or plane? (Y/N): ")
        if(book=='n' or book=='N'):
            book_flight()
        else:
            flightbooked=True
            print("\nOkay that's great!")
    else:
        print("\nOkay we'll do that later!")

book_flight()

if(hotelbooked==False):
    choice=input("\nWould you like to book the Hotel Room now? (Y/N): ")
    if(choice=='Y' or choice=='y'):
        print("\nOkay let's go!")
        book_hotel(choice)
    else:
        print("Alright then!")

if(flightbooked == False):
    choice = input("\nWould you like to book the Flight tickets now? (Y/N): ")
    if (choice == 'Y' or choice == 'y'):
        print("\nOkay let's go!")
        book_flight()
print()

print("YOUR TOTAL PACKAGE")
print("------------------")
print("Your selected country is",my_country)
print("-----------------------------------")
print("Your selected city is",my_city)
print("-----------------------------------")
print("The number of days you will be staying",days)
print("-----------------------------------")
print("The amount you are travelling with is",budget)
print("-----------------------------------")
print("You are bringing along",nop,"people")
print("-----------------------------------")
print("You will be staying in",hotelname)
print("-----------------------------------")
print("You will be travelling through",planename)
print("-----------------------------------")
print("We genuinely hope you have an amazing trip and return home with plenty of unforgettable moments! Hope you'll think of us next time when you wish to travel once again. See you later, " + name + "!")
print("")

























