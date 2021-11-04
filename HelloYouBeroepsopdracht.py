import random
import os

def vraag1():
    print(''' 
    Je zet de tv aan en ziet dat er opstanden zijn in je land.
    A je negeert het B je wordt al een beetje angstig
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag2()
    elif inputText == "B" or inputText == "b":
        vraag3()
    

def vraag2():
    print(''' 
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
    print(''' 
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
    print(''' 
    Het is toch erger dan je dacht je vlucht gelijk weg.
    A je vluch ver weg in je land
    B je vlucht niet ver weg in je land
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag5()
    elif inputText == "B" or inputText == "b":
        vraag6()

def vraag5():
    print(''' 
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
    print(''' 
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
    print(''' 
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
        vraag15()

def vraag8():
    print(''' 
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
    print(''' 
   na een aantal dagen denk je toch verder te vluchten en gaat proberen
   de grens over te komen
   A Je gaat naar de grens
   B je probeert contact te zoeken met smokelaars
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag10()
    elif inputText == "B" or inputText == "b":
        vraag16()

def vraag10():
    print(''' 
    Je komt aan bij de grens en ziet veel soldaten
    A je loopt er naar toe
    B je gaat terug
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag10()
    elif inputText == "B" or inputText == "b":
        vraag16() 


def vraag11():
    print(''' 
    De soldaten vragen wat je hier komt doen
    A je zegt 
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag12()
    elif inputText == "B" or inputText == "b":
        vraag17()      

def vraag12():
    print(''' 
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
    print(''' 
   Doordat je tegen tribbelt wordt je meegenomen
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
    print(''' 
  Je bent aangekomen in de gevangenis
  A wacht 10 jaar
  B probeer weg tekomen
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag19()
    elif inputText == "B" or inputText == "b":
        vraag23()

def vraag15():
    print(''' 
   Je gaat proberen over de grens te komen
   A je gaat naar de grens
   B je probeert contact te zoeken met smokelaars
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag10()
    elif inputText == "B" or inputText == "b":
        vraag16()

def vraag16():
    print(''' 
    Je hebt een smokelaar gevonden die je wilt helpen.
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
    print('''
    Je hebt het betaald en ze brengen je over de grens 
    ''')
    vraag21()

def vraag1602():
    print('''
    Het is je gelukt om het te verlagen met 2000 euro. 
    Ze brengen je over de grens
    ''')
    vraag21()

def vraag17():
    print(''' 
  Je bent terug wat doe je.
  A je gaat naar de grens
  B je probeert contact te zoeken met smokelaars
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag10()
    elif inputText == "B" or inputText == "b":
        vraag16()

def vraag18():
    print(''' 
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
    print(''' 
   Je bent aangekomen in de gevangenis. Het is niet
   gelukt om over de grens te komen.
   A wacht 10 jaar
   B probeer weg te komen
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag20()
    elif inputText == "B" or inputText == "b":
        vraag23()

def vraag20():
    print(''' 
   Het is 10 jaar later en de grensen zijn en de grensen zijn
   een stuk minder streng bewaakt. Je kan naar de overkant
   A je gaat naar de overkant
   B je bedenkt je. je blijft tot de oorlog voorbij is
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag13()
    elif inputText == "B" or inputText == "b":
        vraag40()

def vraag21():
    print(''' 
   Je hoort van iemand dat je naar europa moet omdat het daar veilig is
   A ga daar naartoe
   B je blijft in het land waar je net bent aangekomen
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag25()
    elif inputText == "B" or inputText == "b":
        vraag22()

def vraag22():
    print(''' 
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

def vraag12():
    print(''' 
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

def vraag23():
    print(''' 
    Iemand in de gevangenis zei tegen je dat hij een manier weet
    om weg te komen. Ga je met hem mee.
    A ja
    B nee
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag13()
    elif inputText == "B" or inputText == "b":
        vraag2301

def vraag2301():
    print("Je wacht 10 jaar tot je vrij bent")
    vraag20()

def vraag24():
    print(''' 
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
        vraag17()

def vraag25():
    print(''' 
    Je ontsnapt.
    Aa je gaat naar de grens
    B je zoekt smokelaars op je wilt niet weer naar de
    gevangenis
     ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag16()
    elif inputText == "B" or inputText == "b":
        vraag2501()

def vraag2501():
    print('''
    je bent bij de grens en gaat naar de overkant
    ''')
    vraag21()

def vraag26():
    print(''' 
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
    print(''' 
   Je neemt de busu. Het duurt heel lang
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
    print("De bus rijd verder")
    vraag28()

def vraag28():
    print(''' 
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
    print(''' 
   Je hebt geen asiel gevraagd. Je zoekt iemand om bij te wonen.
   En hoopt dat je niet word terug gestuurd.
    ''')
    vraag40()

def vraag30():
    print(''' 
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
    print("Je komt aan in Europa en hoort dat je naar nederland moet gaan")
    vraag28()

def vraag3002():
    print("Iemand stopt voor je en brengt je het laatste stuk naar europa")
    vraag3001()

def vraag31():
    print(''' 
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
    print('''
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
    print(''' 
  Ze laten je toe.
  Je moet een inburgeringstest doen.
  A doe het
  B doe het niet
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag3303()
    elif inputText == "B" or inputText == "b":
        vraag17()

def vraag3303():
    print("Je moet het doen om in Nederland te kunnen wonen")

#def vraag34():
#    a = ["Haalt het", "Haalt het niet"]
#    print("Je doet het en je"+ (str(random.choice(a)):
#        print(a)
#    if inputText == "A" or inputText == "a":
#     vraag40()
#    elif inputText == "B" or inputText == "b": 
#        vraag35()

def vraag35():
    print(''' 
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
    print(''' 
    Je blijft in nederland en zoekt iemand om bij te wonen
    ''')
    vraag40()

def vraag37():
    print(''' 
    Je hebt asiel aangevraagd en doet een inburgeringstest.
    Je hebt de test gehaald
    ''')
    vraag40()


def vraag40():
    print("EINDE")

vraag1()


     


   
