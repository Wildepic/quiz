


def q1():
    print("Wer ist Ceaser")
    print("[1]Der Feldherr der Gallien errobert hat")
    print("[2]Ein Galler der Rom errobert hat")

def q2():
    print("Wer ist der erste Kaiser von Rom")
    print("[1]Julius Ceaser")
    print("[2]Octavian")

def q3():
    print("Wer ist Hannibal")
    print("[1]Ein Kannibal")
    print("[2]Ein Pun Feldherr")

def q4():
     print("Wer ist scipio")
     print("[1]Der Feldherr in den zweiten Pun Krieg")
     print("[2]Ein Pun Feldherr")

def q5():
     print("Was fur system ist nicht in Rom")
     print("[1]Dictatur")
     print("[2]Kaiserzeit")

Answer2 = 0

q1() 
option = int(input("Antwort:"))  
if option == 1: 
    print("Richtig")
    a1 = 1
    q2()
    option2 = int(input("Antwort:")) 
    if option2 == 2:
        print("Richtig")
        Answer2 = 1
    if option2 == 1:
        print("Falsch") 
if option == 2:  
    print("Falsch")  
    a1 = 0
    q2()
    option = int(input("Antwort:")) 
    if option == 1:
        print("Falsch")
        

    if option == 2:
        print("Richtig")
        Answer2 = 1 

q3()    
option3 = int(input("Antwort:"))  
if option3 == 1:
    print("Falsch")
    answer3 = 0

if option3 == 2:
    answer3 = 1
    print("Richtig")

q4()    
option4 = int(input("Antwort:"))  
if option4 == 1:
    print("Richtig")
    answer5 = 1

if option4 == 2:
    answer5 =0
    print("Falsch")    

q5()    
option5 = int(input("Antwort:"))  
if option5 == 1:
    print("Richtig")
    answer6 = 1

if option5 == 2:
    answer6 =0
    print("Falsch")    


m1 = (a1 + Answer2 + answer3 + answer5 + answer6)
print(m1 , "Sind richtig beantwordete Fragen von 5")