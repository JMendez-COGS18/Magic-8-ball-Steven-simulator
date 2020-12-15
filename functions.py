#Hello, thank you for comming. I present to you my magical 8 ball simulator!
#please enjoy



#To begin, I needed import random so the code can choose any of these answers from 1-14 that I created.
import random

Answer1 = "Signs point to yes. 👍( ͡◉ ‿ ͡◉👍)"

Answer2 = "I do not see why I would say no. 👍( ◉︠ ‿ ︡◉👍)"

Answer3 = "Since you asked nicely, of course. 👍( ◉︡ ‿ ◉︠ 👍)"

Answer4 = "Haha okay, I can tell you're excited so sure. (っ ◉︡ ‿ ◉︠ )っ🎔"

Answer5 = "We'll let time decide this one so 50/50. ¯\_( ͡~ ͜ʖ ͡°)_/¯"

Answer6 = "Of course! ☜ ( ͡❛ ͜ʖ ͡❛)"

Answer7 = "Haha please do not ask again. ʕ ◉︡ ‿ ◉︠ ʔ"

Answer8 = "Heck no! ʕ ◉︡ 👅 ◉︠ ʔ"

Answer9 = "I'm truly sorry...I don't think you want to know. 【 ͡👁️ ͜ʖ ͡👁️】"

Answer10 = "Man can't even tell you that, I'm just different. ¯\_( ͠ಠ ͜ʖ ͠ಠ )_/¯"

Answer11 = "You know who else asked that? My mom. ʕ ͠◉ 👅 ͡◉ʔ"

Answer12 = "I missed the part where that's my problem. ʕ ͠◉ Ĺ̯ ͡◉ʔ"

Answer13 = "That's crazy. But que pasa? 【▀̿ ̿̀ ͜ʖ ́▀̿ ̿ 】"

Answer14 = "I like you, so why not lol. ☻♥ "


#In this part below, I created this so that the user can input hwatever name they want to call themselves and so that the 8 ball or Steven, can be responsive to what the sa. I added thi o this code can be fun and interactive.

Name_of_curiosity = input("( ͡◉ ‿ ͡◉) Oh hello there, did not expect to see anyone around this time. My name is Steven but most people call me the magical 8 ball haha. Well enter your name, this helps me sink into the many alternate timelines to give you a concrete answer: ")
input(Name_of_curiosity + ", Ahh yess! I knew you would come here. Get it? Sorry my humors all ROUND up. Hahah because I'm a ball. Well anyways, ask away.. ")

#Lastly, this part of the code is what uses the random I imported so it can give a reply to whatever the user may have asked and it can be picked at random that way it is never the same answer. 
Fate = random.randint(1,14)

if Fate == 1:
    answer = Answer1
elif Fate ==2:
    answer = Answer2
elif Fate ==3:
    answer = Answer3
elif Fate ==4:
    answer = Answer4
elif Fate ==5:
    answer = Answer5
elif Fate ==6:
    answer = Answer6
elif Fate ==7:
    answer = Answer7
elif Fate ==8:
    answer = Answer8
elif Fate ==9:
    answer = Answer9
elif Fate ==10:
    answer = Answer10
elif Fate ==11:
    answer = Answer11
elif Fate ==12:
    answer = Answer12
elif Fate ==13:
    answer = Answer13
elif Fate ==14:
    answer = Answer14
    
#This part of the code is what will output the reply to the question asked. I also decided to add text art to give Steven a personality. Just to make this funny.

print('*****************************')
print('( ͡◉ ͜ʖ ͡◉)')
print('*****************************')

print("(¯`v´¯) hmm let me look into the future, give me a second yea? Here is some hearts for being so patient ♥♥♥♥♥♥♥♥")

print('( ͡◉ ͜ʖ ͡◉)')
    
print("The Magic 8 ball of all knowing, Steven, says: ", answer)
