def candy():
    count=0
    candy=['Kit Kat','Snickers','Milky Way','Lollipops','M&M']
    print(candy[count])
    print('Do you want more candy?')
    candy_answer=input()
    while candy_answer=='yes':
        count+=1
        if count>4:
            count=0
        candy=['Kit Kat','Snickers','Milky Way','Lollipops','M&M']
        print(candy[count])
        print('Do you want more candy?')
        candy_answer=input()
    print("Ok, enjoy your candy")
def riddle1():
    print("Your first riddle is")
    print("The person who built it sold it.")
    print("The person who bought it never used it.")
    print("The person who used it never saw it. What is it?")
    answer1=input()
    while answer1.lower()!="coffin":
        print("Try again!")
        answer1=input()
    print("You solved the first riddle")
def riddle2():
    print("Your second riddle is")
    print("I am a body with a leg, an arm and a head, but I do not have flesh or eyeballs.")
    print("I am a ______")
    answer2=input()
    while answer2.lower()!="skeleton":
        print("Try again!")
        answer2=input()
    print("You solved the second riddle")
def riddle3():
    print("Your third riddle is")
    print("I have no feet to dance, I have no eyes to see, I have no life to live or die, but yet I do all three.")
    print("What am I?")
    answer3=input()
    while answer3.lower()!="fire":
        print("Try again!")
        answer3=input()
    print("You solved the third riddle")
    print("Only 7 more to go!")
def riddle4():
    print("Your fourth riddle is")
    print("I am wrapped, but I am not a gift. I am kept neatly in a chamber, and archeologists find me as a great treasure.")
    print("I am a ______")
    answer4=input()
    while answer4.lower()!="mummy":
        print("Try again!")
        answer4=input()
    print("You solved the fourth riddle")
def riddle5():
    print("Your fifth riddle is")
    print("If you see one flying around, you would better be careful at night, as some turn into vampires and will give your neck a big bite.")
    print("What are they?")
    answer5=input()
    while answer5.lower()!="bats":
        print("Try again!")
        answer5=input()
    print("You solved the fifth riddle")
def riddle6():
    print("Your sixth riddle is")
    print("Some people believe in me and others do not. At night I roam around and sometimes I float. If you hear a troubled noise coming from the ground, go run and hide from my creepy sound.")
    print("I am a ______")
    answer6=input()
    while answer6.lower()!="ghost":
        print("Try again!")
        answer6=input()
    print("You solved the sixth riddle")
    print("Only 4 more before the prize!")
def riddle7():
    print("Your seventh riddle is")
    print("I am tall when I am young, I am short when I am old, and every Halloween, I stand up inside jack-o-lantern. What am I?")
    print("I am a ______")
    answer7=input()
    while answer7.lower()!="candle":
        print("Try again!")
        answer7=input()
    print("You solved the seventh riddle")
def riddle8():
    print("Your eighth riddle is")
    print("You can find me from head to toe, I am a liquid, I make some people faint and I am in every living being you know. What am I?")
    print("I am ______")
    answer8=input()
    while answer8.lower()!="blood":
        print("Try again!")
        answer8=input()
    print("You solved the eighth riddle")
def riddle9():
    print("Your ninth riddle is")
    print("I have hundreds of ears, but I can not hear a thing. What am I?")
    print("I am a ______")
    answer9=input()
    while answer9.lower()!="cornfield":
        print("Try again!")
        answer9=input()
    print("You solved the ninth riddle")
    print("One more riddle before the prize!")
def riddle10():
    print("Your final riddle is")
    print("You can easily get me any time of year, but you have to specifically ask for me on Halloween—otherwise, you will end up empty handed. What am I?")
    print("I am ______")
    answer10=input()
    while answer10.lower()!="candy":
        print("Try again!")
        answer10=input()
    print("You solved the last riddle")
    print("Here have some candy!")
def start():
    riddle1()
    riddle2()
    riddle3()
    riddle4()
    riddle5()
    riddle6()
    riddle7()
    riddle8()
    riddle9()
    riddle10()
    candy()
print("Welcome to the riddle room")
print("You will have to solve these 10 riddles for a prize")
print("But fail and you will be trapped in the riddle room forever!")
print("Do you want to begin?")
answer=input()
if answer.lower()=="yes":
    print("Thank you for accepting the challenge!")
    start()
else:
    print("Goodbye")


