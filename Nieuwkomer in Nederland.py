#Het keuze verhaal van een nieuwkomer in Nederland 

from time import sleep

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
yes = ["Y", "y", "Yes", "yes", "Ja", "ja"]
no = ["N", "n", "No", "no", "Nee", "nee"]

required = ("\nUse only A, B, C, or D\n")

while True: 
      #Intro 

      print("Dit is een verhaal ove Mustafa een Nieuwkomer in Nederland."
      "Mustafa wil vanwege oorlog naar Nederland vluchten. "
      "Mustafa moet verschillende keuzes maken om zijn eindbestemming te halen."
      "In dit verhaal zal jij de keuzes voor Mustafa gaan maken.")
      sleep(3)
      print("Mustafa ligt in zijn bed maar hij kan niet slapen. "
      "Hij hoort een hele harde knal verderop in de straat, hij wil kijken wat het is.")
      sleep(2)
      print("wat ga je doen?")
      print("A= Blijf je in je bed liggen en wachten tot de ochtend of B= ga je naar buiten en kijken wat er aan de hand is.")
      
      choice1 = input("A\n B\n")
      if choice1 == "A":
            print("")

      elif choice1 == "B":
            print