print("WELCOME TO कौन बनेगा करोड़पति!")
print("INSTRUCTIONS: you face up to 15 multiple-choice gk questions of increasing difficulty, aiming for the grand prize. as you progress, the monetary reward for each correct answer increases. the prize money is structured with 'safety nets' (usually at question 5, 10, 15). if you answer incorrectly after passing a safety net, you still walk away with the guaranteed amount. disclaimer: unlike the real program, this online version lacks lifelines.")
questions=[
    ["which day is observed as the world standard's day?","june 26","october 14","november 15","december 2",2],
    ["bahubali festival is related to?","islam","hinduism","buddhism","jainism",4],
    ["'international literacy day' is observed on?","september 22","september 8","november 28","may 2",2],
    ["the language of lakshadweep, a union territory of india is?","tamil","hindi","malayalam","telugu",3],
    ["what do the five rings of the olympics represent?","5 games","5 oceans","5 continents","5 languages",3],
    ["who is the author of 'manas ka-hans'","khushwant singh","amrit lal nagar","prem chand","jayashankar prasad",2],
    ["who is the author of the epic 'meghdoot'","valmiki","kalidas","banabhatta","vishakadatta",2],
    ["world health day is observed on?","april 7","march 6","march 15","april 28",1],
    ["'pongal' is a popular festival of which state?","kerala","tamil nadu","andhra pradesh","karnataka",2],
    ["which of the following muslim festivals is based on the holy quran","id-ul-fitr","id-ul-zuha","bakri-id","moharram",2],
    ["'rath yathra' is a famour festival at?","puri","madhura","ayodhya","dwaraka",1],
    ["onam is the famous festival of?","kerala","tamil nadu","andhra pradesh","karnataka",1],
    ["which one of the following is essentially a solo-dance?","kuchipudi","kathak","manipuri","mohiniattam",4],
    ["which one of the following is the folk dance of india?","manipuri","mohiniattam","kathakali","garba",4],
    ["nandyal is situated in?","karnataka","andhra pradesh","maharashtra","madhya pradesh",2]]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0

for i in range(0,len(questions)):
    question=questions[i]
    print(question[0])
    print(f"question for rs. {levels[i]}")
    print(f"a. {question[1]}   b. {question[2]}")
    print(f"c. {question[3]}   d. {question[4]}")

    reply=int(input("enter your answer (1-4) or 0 to 'quit': "))
    if (reply==0):
        break
    elif (reply==question[-1]):
        print("CORRECT ANSWER!\nyou have won rs.",levels[i])
        if (i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("WRONG ANSWER.")
        break
print(f"your take away prize money: ",money)
print("THANK YOU!")