import random
import time
import os
import sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./1000)

def slowprint2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10000)

def vraag1():
    os.system("cls")
    slowprint(''' 
    Je zet de tv aan en ziet dat er opstanden zijn in je land.
    A je negeert het 
    B je wordt al een beetje angstig
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag2()
    elif inputText == "B" or inputText == "b":
        vraag3()
    

def vraag2():
    os.system("cls")
    slowprint(''' 
    De volgende dagen zie je dat het steeds onrustiger wordt,
    later hoor je een grote knal en zie je dat het oorlog is.
    A Je vlucht de stad uit en hoopt dat er ergens anders geen oorlog is
    B Je blijft thuis en wacht tot het over is.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag5()
    elif inputText == "B" or inputText == "b":
        vraag4()
    

def vraag3():
    os.system("cls")
    slowprint(''' 
    Je vlucht de stad uit.
    A je vlucht ver weg in je land
    B je vlucht niet ver weg in je land
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag5()
    elif inputText == "B" or inputText == "b":
        vraag6()
        

def vraag4():
    os.system("cls")
    slowprint(''' 
    Het is toch erger dan je dacht je vlucht gelijk weg.
    A je vlucht ver weg in je land
    B je vlucht niet ver weg in je land
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag5()
    elif inputText == "B" or inputText == "b":
        vraag6()

def vraag5():
    os.system("cls")
    slowprint(''' 
    Na lang reizen naar een andere stad zie je dat het daar er net zo slecht aan toe is.
    De oorlog is dus een stuk groter dan je dacht
    A je vlucht naar de andere kant van je land
    B je probeert zo snel mogelijk je land uit te komen
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag7()
    elif inputText == "B" or inputText == "b":
        vraag26()

def vraag6():
    os.system("cls")
    slowprint(''' 
    Je vlucht maar je was niet ver genoeg gevlucht. Je wordt
    opgepakt omdat je probeerde te vluchten
    A stribbel tegen
    B Ga mee
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag13()
    elif inputText == "B" or inputText == "b":
        vraag14()
    
def vraag7():
    os.system("cls")
    slowprint(''' 
    Je zoekt de snelste  weg naar de andere kant ban je land je kan kiezen
    tussen de bus en het vliegtuig
    A je kiest de bus
    B je kiest het vliegtuig
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag8()
    elif inputText == "B" or inputText == "b":
        vraag21()

def vraag8():
    os.system("cls")
    slowprint(''' 
    Na 15 uur in de bus ben je eindelijk aangekomen. Hier is nog
    geen oorlog maar het is hier wel al onrustig
    A je wacht af
    B je reist gelijk verder
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag9()
    elif inputText == "B" or inputText == "b":
        vraag15()

def vraag9():
    os.system("cls")
    slowprint(''' 
   na een aantal dagen denk je toch verder te vluchten en gaat proberen
   de grens over te komen
   A Je gaat naar de grens
   B je probeert contact te zoeken met smokkelaars
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag10()
    elif inputText == "B" or inputText == "b":
        vraag16()

def vraag10():
    os.system("cls")
    slowprint(''' 
    Je komt aan bij de grens en ziet veel soldaten
    A je loopt er naar toe
    B je gaat terug
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag11()
    elif inputText == "B" or inputText == "b":
        vraag17() 


def vraag11():
    os.system("cls")
    slowprint(''' 
    De soldaten vragen wat je hier komt doen
    A je zegt dat je de grens over wilt
    B je gaat terug
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag12()
    elif inputText == "B" or inputText == "b":
        vraag17()      

def vraag12():
    os.system("cls")
    slowprint(''' 
   De soldaten zeggen dat dat niet kan
   A je stribbelt tegen
   B je gaat terug
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag13()
    elif inputText == "B" or inputText == "b":
        vraag17()

def vraag13():
    os.system("cls")
    slowprint(''' 
   Doordat je tegen stribbelt wordt je meegenomen
   A vraag waar je naartoe wordt gebracht
   B zeg niks
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag18()
    elif inputText == "B" or inputText == "b":
        vraag18()

def vraag14():
    os.system("cls")
    slowprint(''' 
  Je bent aangekomen in de gevangenis
  A wacht 10 jaar
  B probeer weg tekomen
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag2301()
    elif inputText == "B" or inputText == "b":
        vraag23()

def vraag15():
    os.system("cls")
    slowprint(''' 
   Je gaat proberen over de grens te komen
   A je gaat naar de grens
   B je probeert contact te zoeken met smokkelaars
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag10()
    elif inputText == "B" or inputText == "b":
        vraag16()

def vraag16():
    os.system("cls")
    slowprint(''' 
    Je hebt een smokkelaar gevonden die je wilt helpen.
    Ze willen dat je 5000 euro betaald
    A je betaald het
    B je probeert te onderhandelen
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag1601()
    elif inputText == "B" or inputText == "b":
        vraag1602()

def vraag1601():
    os.system("cls")
    slowprint('''
    Je hebt het betaald en ze brengen je over de grens 
    ''')
    print("")
    print("wacht 3 seconden")
    time.sleep(3)
    vraag21()

def vraag1602():
    os.system("cls")
    slowprint('''
    Het is je gelukt om het te verlagen met 2000 euro. 
    Ze brengen je over de grens
    ''')
    print("")
    print("wacht 3 seconden")
    time.sleep(3)
    vraag21()

def vraag17():
    os.system("cls")
    slowprint(''' 
  Je bent terug wat doe je.
  A je gaat naar de grens
  B je probeert contact te zoeken met smokkelaars
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag10()
    elif inputText == "B" or inputText == "b":
        vraag16()

def vraag18():
    os.system("cls")
    slowprint(''' 
   Ze zeggen dat je naar de gevangenis word gebracht omdat je niet gehoorzaamde
   A zeg dat je het er niet mee eens bent
   B zeg niks
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag19()
    elif inputText == "B" or inputText == "b":
        vraag19()

def vraag19():
    os.system("cls")
    slowprint(''' 
   Je bent aangekomen in de gevangenis. Het is niet
   gelukt om over de grens te komen.
   A wacht 10 jaar
   B probeer weg te komen
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag2301()
    elif inputText == "B" or inputText == "b":
        vraag23()

def vraag20():
    os.system("cls")
    slowprint(''' 
   Het is 10 jaar later en de grensen zijn
   een stuk minder streng bewaakt. Je kan naar de overkant
   A je gaat naar de overkant
   B je bedenkt je. je blijft tot de oorlog voorbij is
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag21()
    elif inputText == "B" or inputText == "b":
        vraag40()

def vraag21():
    os.system("cls")
    slowprint(''' 
   Je hoort van iemand dat je naar europa moet omdat het daar veilig is
   A ga daar naartoe
   B je blijft in het land waar je net bent aangekomen
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag27()
    elif inputText == "B" or inputText == "b":
        vraag22()

def vraag22():
    os.system("cls")
    slowprint(''' 
   Je blijft in het land waar je net bent aangekomen
   vraag je asiel aan?
   A ja
   B nee
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag32()
    elif inputText == "B" or inputText == "b":
        vraag29()

def vraag23():
    os.system("cls")
    slowprint(''' 
    Iemand in de gevangenis zei tegen je dat hij een manier weet
    om weg te komen. Ga je met hem mee.
    A ja
    B nee
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag24()
    elif inputText == "B" or inputText == "b":
        vraag2301()

def vraag2301():
    os.system("cls")
    slowprint("Je wacht 10 jaar tot je vrij bent")
    print("")
    print("je wacht 10 jaar")
    time.sleep(3)
    print("nee grapje eigenlijk maar 10 seconden")
    time.sleep(10)
    vraag20()

def vraag24():
    os.system("cls")
    slowprint(''' 
  Hij verteld je dat je in de nacht weg kan komen door een
  gat in het hek
  A je doet het
  B je doet het niet
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag25()
    elif inputText == "B" or inputText == "b":
        vraag2301()

def vraag25():
    os.system("cls")
    slowprint(''' 
    Je ontsnapt.
    Aa je gaat naar de grens
    B je zoekt smokkelaars op je wilt niet weer naar de
    gevangenis
     ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag2501()
    elif inputText == "B" or inputText == "b":
        vraag2501()

def vraag2501():
    os.system("cls")
    slowprint('''
    je bent bij de grens en gaat naar de overkant
    ''')
    print("")
    print("wacht 3 seconden")
    time.sleep(3)
    vraag21()

def vraag26():
    os.system("cls")
    slowprint(''' 
   Je neemt het vliegtuig waar vlieg je naartoe
   A Nederland
   B Griekenland
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag28()
    elif inputText == "B" or inputText == "b":
        vraag31()

def vraag27():
    os.system("cls")
    slowprint(''' 
   Je neemt de bus. Het duurt heel lang
   uit eindelijk stopt de bus
   A je wacht tot de bus gaat rijden
   B je gaat uit de bus
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag2701()
    elif inputText == "B" or inputText == "b":
        vraag30()

def vraag2701():
    os.system("cls")
    print("De bus rijd verder")
    print("")
    print("wacht 3 seconden")
    time.sleep(3)
    vraag28()

def vraag28():
    os.system("cls")
    slowprint(''' 
   Je bent aangekomen in Nederland
   A je vraagt asiel
   B je vraagt geen asiel
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag32()
    elif inputText == "B" or inputText == "b":
        vraag37()

def vraag29():
    os.system("cls")
    slowprint(''' 
   Je hebt geen asiel gevraagd. Je zoekt iemand om bij te wonen.
   En hoopt dat je niet word terug gestuurd.
    ''')
    print("")
    print("wacht 3 seconden")
    time.sleep(3)
    vraag40()

def vraag30():
    os.system("cls")
    slowprint(''' 
   De bus rijd opeens weg je moet ander vervoer zoeken.
   A je gaat lopen
   B je zoekt iemand die je kan brengen
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag3001()
    elif inputText == "B" or inputText == "b":
        vraag3002()

def vraag3001():
    os.system("cls")
    slowprint("Je komt aan in Europa en hoort dat je naar nederland moet gaan")
    print("")
    print("wacht 3 seconden")
    time.sleep(3)
    vraag28()

def vraag3002():
    os.system("cls")
    slowprint("Iemand stopt voor je en brengt je het laatste stuk naar europa")
    print("")
    print("wacht 3 seconden")
    time.sleep(3)
    vraag3001()

def vraag31():
    os.system("cls")
    slowprint(''' 
    Je komt aan in griekenland maar ze willen dat je verder gaat in europa.
    A ga naar nederland
    B ga naar belgië
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag28()
    elif inputText == "B" or inputText == "b":
        vraag37()

def vraag32():
    os.system("cls")
    slowprint('''
    Je vraagt om asiel, maar ze zeggen dat je waarschijnlijk word
    afgewezen
    A je gaat slijmen
    B je word terug gestuurd
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag33()
    elif inputText == "B" or inputText == "b":
        vraag37()

def vraag33():
    os.system("cls")
    slowprint(''' 
  Ze laten je toe.
  Je moet een inburgeringstest doen.
  A doe het
  B doe het niet
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag34()
    elif inputText == "B" or inputText == "b":
        vraag3303()

def vraag3303():
    os.system("cls")
    slowprint("Je moet het doen om in Nederland te kunnen wonen")
    vraag33()

def vraag34():
    os.system("cls")
    a = ["Haalt het", "Haalt het", "Haalt het", "Haalt het", "Haalt het", "Haalt het niet"]
    i = a[random.randint(0,5)]
    slowprint("Je doet het en je "+ (str(i)))
    if i == "Haalt het":
        vraag4001()
    elif i == "Haalt het niet": 
        vraag35()

def vraag35():
    os.system("cls")
    slowprint(''' 
    Je hoort dat je weg moet. Je vraagt of je echt niet kan blijven
    maar ze zeggen dat je echt terug moet. 
    A je blijft in nederland
    B je gaat naar belgië je hoorde dat ze daar minder streng zijn
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag36()
    elif inputText == "B" or inputText == "b":
        vraag37()

def vraag36():
    os.system("cls")
    slowprint(''' 
    Je blijft in nederland en zoekt iemand om bij te wonen
    ''')
    vraag40()

def vraag37():
    os.system("cls")
    slowprint(''' 
    Je hebt asiel aangevraagd en doet een inburgeringstest.
    Je hebt de test gehaald
    ''')
    print("")
    print("wacht 3 seconden")
    time.sleep(3)
    vraag40()


def vraag40():
    os.system("cls")
    slowprint2('''
                   ========================================================
                   |   EEEEEEEEE   EE   EEE   EE   EEEEEE     EEEEEEEEE  |
                   |   EE          EE   EE E  EE   EE    EE   EE         |
                   |   EEEEEEEEE   EE   EE  E EE   EE    EE   EEEEEEEEE  |
                   |   EE          EE   EE   EEE   EE    EE   EE         |
                   |   EEEEEEEEE   EE   EE    EE   EEEEEE     EEEEEEEEE  |     
                   ========================================================
    ''')
    time.sleep(5)

def vraag4001():
    os.system("cls")
    slowprint("Je hebt de inburgeringstest gehaald!")
    print("")
    print("wacht 3 seconden")
    time.sleep(3)
    vraag40()

slowprint('''   Beroeps opdracht vluchtelingen verhaal
            Boi Lipmann SD1B
        druk op enter om te starten ''')
input()
os.system("cls")
vraag1()


     


   
