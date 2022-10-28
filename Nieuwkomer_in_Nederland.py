#Het keuze verhaal van Mustafa 

from ast import While
from time import sleep
 
#intro

print("Dit is een verhaal ove Mustafa een Nieuwkomer in Nederland."
      " Mustafa wil vanwege oorlog uit zijn land naar Nederland vluchten. "
      "Er zijn groepen rebellen die bombardamenten uitvoeren"
      "Mustafa moet verschillende keuzes maken om zijn eindbestemming te halen."
      "In dit verhaal zal jij de keuzes gaan maken.")
sleep(3)
print("Mustafa ligt in zijn bed maar hij kan niet slapen. "
      "Hij hoort een hele harde knal en voelt alles trillen , hij wil naar buiten om te kijken wat het is.")
sleep(2)
print("Blijf je in je bed liggen en wachten tot de ochtend of ga je naar buiten en kijken wat er aan de hand is.")
print("wat ga je doen?")

#vraag 1
def vraag1():
      #vraag 1 A
      choice1 = input("A\nB\n")
      if choice1 == "A":
            print("Oke je blijft liggen tot het ochtend word")
            sleep(2)
            print("Het is ochtend geworden, je hebt gelukkig nog kunnen slapen.")
            sleep(3)
            print("Je hoort allemaal mensen schreeuwen, je kleed je aan en gaat toch maar even buiten kijken."
            "Je schrikt heel erg, Heel veel huizen liggen plat en de straten zijn gebombardeerd.")
            sleep(5)
            print("verderop klink geschreeuw je gaat er naar toe en je ziet dat er mensen onder het puin liggen."
            "Wat ga je doen help je de mensen of ga je weg?")
            vraag2()

      elif choice1=="B":
            vraag6()
      else:
            vraag1()


#vraag2
#vraag2 A
def vraag2(): 
      choice2 = input("A\nB\n")
      if choice2 == "A":
            print("Je gaat naar de mensen toe om te helpen. \nDe mensen schreeuwen naar je ren weg het gebouw staat op instorten.\n Wat doe je ga je de mensen toch helpen of ga je snel weg?")
            vraag3()
      elif choice2=="B":
            vraag4()
      else:
            vraag2()


      #vraag3 
def vraag3():
      choice3 = input("A\nB\n")
      if choice3 == "A":
            print("Oke je gaat toch helpen."
            "Je probeert het puin opzij te schuiven maar het lukt niet."
            "Je trekt een harde keer aan het puin en alles valt naar beneden!")
      sleep(3)

      print("""""   
            █▄█ █▀█ █ █   ▄▀█ █▀█ █▀▀   █▀▄ █▀▀ ▄▀█ █▀▄      
             █  █▄█ █▄█   █▀█ █▀▄ ██▄   █▄▀ ██▄ █▀█ █▄▀""")

      sleep(3)
      print("Je hebt helaas niet de goede keuze gemaakt en hebt het niet overleeft...")
      sleep(2)
      print("Wil je het nog een keer proberen misschien kom je volgende keer verder!")

      opnieuw = input("Ja\nNee\n")

      if opnieuw == "Ja":
            print("Oke!")

      if opnieuw == "Nee":
            print("Oke probeer het later nog eens!")
      

      elif choice3=="B":
            vraag4()
      else:
            vraag3()
      #Einde 1




#vraag3
#vraag3 B
def vraag3(): 
      choice3 = input("A\nB\n")
      if choice3 == "B":
            vraag4()
      else:
            vraag3()

#vraag1
def vraag():
      choice1 = input("A\nB\n")
      if choice1 == "B":
            print("Oke je doet de gordijnen open en je ziet overal vuur en explosies."
            "Je weet dat het niet goed is en je naar de schuilbunker moet, of dat je moet vlucten"
            "Wat ga je doen")
      elif choice1=="B":
            vraag6()
      else:
            vraag1()

#vraag6
#vraag6 A
def vraag6():
      choice6 = input("A\nB\n")
      if choice6 == "A":
            print("Oke je pakt snel genoeg proviand en je gaat voor een paar dagen naar de schuilkelder.")
            vraag7()
      elif choice6=="B":
            pass
      else:
            vraag6()

#vraag7
def vraag7():
      print("Het lijkt er op dat het rustig is, en dat de aanvallen misschien zijn gestaakt"
            "Wil je alsnog vluchten of blijf je in de bunker schuilen? ")
      #vraag7 A
      choice7 = input("A\nB\n")
      if choice7 == "A":
            print("Het lijkt rustig dus je vlucht.")
            vraag4()
      elif choice7=="B":
            vraag9()
      else:
            vraag7()


#vraag7 B 
def vraag7(): 
      choice7 = input("A\nB\n")
      if choice7 == "B":
            print("Oke dan je blijft nog een paar dagen maar je hebt niet zo veel eten meer.")
      
            vraag6()
      elif choice7=="B":
            vraag6()
      else:
            vraag2()


#vraag6 B
def vraag6():
      choice6 = input("A\n B\n")
      if choice6 == "B":
            print("Oke je gaat snel naar je auto en vlugt")
      vraag4()

#vraag4 
def vraag4():
      print("Waar wil je heen vluchten?"
            "Je kan zo snel mogelijk naar de grens reizen maar dat duurt heel lang."
            "Of je kan naar het vliegveld gaan om te kijken of er reddingsvliegtuigen zijn")
      choice4 = input("A\nB\n")
      if choice4 == "A":
            print("Oke je wil met de auto naar de grens vluchten")
            vraag5()
      elif choice4 == "B":
            vraag8()
      else:
            vraag4()

#vraag5
def vraag5():
      print("Je bent na een lange reis bij de grens aangekomen, en je ziet controle"
            "Wat doe je ga je er gewoon naar toe en kijken of je er langs kan of ga je een andere weg zoeken?")
      #vraag5 A
      choice5 = input("A\nB\n")
      if choice5 == "A":
            print("Oke je gaat proberen er langs de controle te komen ")
            sleep(4)
            print("Helaas wordt je er niet langs gelaten en moet je omrijden")
            vraag5()
      elif choice5 == "B":
            vraag5B
      else:
            vraag5()


#vraag5 B
def vraag5B():
      print("Om te voorkomen dat je hellemaal word onderzocht ga je toch omrijden.")
      sleep(3)
      print("Na een lange tocht kom je bij de grens van Nederland!")
      sleep(4)
      print("Je bent eindelijk na een lange tocht bij je eindbestemming")
      sleep(3)
      print("Je vind een nieuwe baan en je bouwt een nieuw leven op!")
      print(""" ▄▄▄▄▄▄▄ ▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ 
            █       █   █  █  █ █      ██       █
            █    ▄▄▄█   █   █▄█ █  ▄    █    ▄▄▄█
            █   █▄▄▄█   █       █ █ █   █   █▄▄▄ 
            █    ▄▄▄█   █  ▄    █ █▄█   █    ▄▄▄█
            █   █▄▄▄█   █ █ █   █       █   █▄▄▄ 
            █▄▄▄▄▄▄▄█▄▄▄█▄█  █▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄█""")

      sleep(3)
      print("Wil je het nog een keer proberen misschien krijg je vlogende keer een ander einde!")

      opnieuw = input("Ja\nNee\n")

      if opnieuw == "Ja":
            print("Oke!")
            

      if opnieuw == "Nee":
            print("Oke probeer het later nog eens!")
      
      else:
            vraag5()
      #Einde 2



#vraag4 B
def vraag4B():
      choice4 = input("A\nB\n")
      if choice4 == "B":
            print("Oke je vlucht naar het vliegveld")
            vraag8()
      else:
            vraag4B()


      #vraag8
      def vraag8():
            print("Na een tijd rijden kom je op het vliegveld aan, je ziet dat het heel druk is vanwege evacuatie."
            "Er zijn evacuatie vliegtuigen uit verschillende landen zoals Nederland , Duitsland en Engeland."
            "Wat ga je doen wil je toch met de auto naar de grens of met het vliegtuig evacueren")


            choice8 = input("A\nB\n")
            if choice8 == "A":
                  print("Oke je gaat toch met de auto")
                  vraag5()
            elif choice8 == "B":
                  pass
            else:
                  vraag8()


#vraag8 B
def vraag8():

      print("Je gaat toch in de rij staan want je wil graag met het vliegtuig mee.")
      sleep(3)
      print("Na een paar uur in de rij te hebben gestaan kan je eindelijk met het evacuatie vliegtuig mee naar schiphol")
      sleep(4)
      print("Je bent veilig in Nederland aangekomen en je word goed opgevangen")
      sleep(3)
      print("De mensen zijn goed voor je en je krijgt een tijdelijk onderdak")
      sleep(2)
      print("Je krijgt de tijd om een nieuw leven op te bouwen en je krijgt alle hulp")
      sleep(2)
      print("Ook vind je een nieuwe baan en kan je weer op je zelf gaan wonen!")

      print(""" ▄▄▄▄▄▄▄ ▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ 
            █       █   █  █  █ █      ██       █
            █    ▄▄▄█   █   █▄█ █  ▄    █    ▄▄▄█
            █   █▄▄▄█   █       █ █ █   █   █▄▄▄ 
            █    ▄▄▄█   █  ▄    █ █▄█   █    ▄▄▄█
            █   █▄▄▄█   █ █ █   █       █   █▄▄▄ 
            █▄▄▄▄▄▄▄█▄▄▄█▄█  █▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄█""")

      sleep(3)
      print("Wil je het nog een keer proberen misschien krijg je vlogende keer een ander einde!")

      opnieuw = input("Ja\nNee\n")

      if opnieuw == "Ja":
            print("Oke!")
            

      if opnieuw == "Nee":
            print("Oke probeer het later nog eens!")
            
            vraag6()
      else:
            vraag8()
      #Einde 3



#vraag 9
def vraag9():
      print("Na een paar dagen zit je nog steeds in de bunker."
            "Je weet niet goed wat er aan de hand is omdat het de ene keer los barst en de andere keer hoor je niks"
            "Het kan zijn dat de rebellen op de loer liggen maar je kan hier niet altijd blijven. wat ga je doen?"
            "Blijf je in de bunker of ga je er uit?")

#vraag 9 A
def vraag9():
      choice9 = input("A\nB\n")
      if choice9 == "A":
            print("Je blijft in de bunker want je durft het toch niet aan om naar buiten te gaan.")
      sleep(5)
      print("Het gaat niet goed met je en je word helemaal raar in je hoofd")
      sleep(3)
      print("Je overlijd uit verhongering")

      sleep(3)
      print("Je hebt helaas niet de goede keuze gemaakt en hebt het niet overleeft...")
      sleep(2)
      print("Wil je het nog een keer proberen misschien kom je volgende keer verder!")

      opnieuw = input("Ja\nNee\n")

      if opnieuw == "Ja":
            print("Oke!")
         

      if opnieuw == "Nee":
            print("Oke probeer het later nog eens!")
      else:
            vraag9()  

#vraag9 B
def vraag9(): 
      choice9 = input("A\nB\n")
      if choice9 == "B":
            print("Je gaat snel uit de bunker")
            vraag4()
      else:
            vraag9()

#vraag10
def vraag10():
      print("Het ziet er naar uit dat de rebellen weg zijn uit de stad maar je weet het niet zeker"
            "Wat is een verstandige keuze blijf je in de stad of vlucht je alsnog?")


#vraag10 A
def vraag10():
      choice10 = input("A\nB\n")
      if choice10 == "A":
            print("Je blijft toch in je eigen land."
            "Helaas zijn de rebellen nog niet weg en het gebied waar je in woont is onder hun controle."
            "Je lijd nu een beperkt leven en de stad moet opnieuw worden opgebouwd")
      sleep(5)
      print("Het is een paar maanden verder en er is nog steeds geen hulp gekomen."
            "De stad is inmiddels wel weer een beetje opgebouwd, maar het ziet er voor nu uit dat je voorlopig zo moet leven")
      sleep(4)
      print("""
                              ^
                  _______    ^^^
                |xxxxxxx|  _^^^^^_
                |xxxxxxx| | [][]  |
            _____ _xxxxx| |[][][] |
            |++++++|xxxx| | [][][]|      
            |++++++|xxxx| |[][][] |
            |++++++|_________ [][]|
            |++++++|=|=|=|=|=| [] |
            |++++++|=|=|=|=|=|[][]|
      ______|++HH++|  _HHHH__|   _________   _________  _________
            _______________   ______________      ______________
      __________________  ___________    __________________    ____________""")


      sleep(3)
      print("Wil je het nog een keer proberen misschien krijg je vlogende keer een ander einde!")

      opnieuw = input("Ja\nNee\n")

      if opnieuw == "Ja":
            print("Oke!")
            

      if opnieuw == "Nee":
            print("Oke probeer het later nog eens!")

                
      elif choice10=="B":
            vraag()
      else:
            vraag10()   

      #Einde 5

#vraag10 B
def vraag10():
      choice10 = input("A\nB\n")
      if choice10 == "B":
            print("Oke je vlucht alsnog")
            vraag4()        
      elif choice10=="B":
            vraag4()
      else:
            vraag10()



vraag1()
