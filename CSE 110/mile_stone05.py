print('Welcome to ChoiceMaker!\n')

#First level

while True:
    answer_1 = input('You are going to a class on campus, so there are two ways to make it to the class: the FAST WAY or the NORMAL WAY. Which one do you want? ')
    choice = str.upper(answer_1)
    if choice == 'FAST WAY':
        print('NICE CHOICE!')
        break
    elif choice == 'NORMAL WAY':
        print('You may arrive late for the class, so you must walk a faster!')
        break
    else:
        print('That is not an option...')
        

#Second level

while True:
    answer_2 = input('''\nYou got out of the room to go to the class, but there are people in the apartment. They are some of your best friends and 
they invited you to watch a movie and eat pizza with them... 
You can choose: say ANOTHER TIME, GRAB A PIZZA, WATCH MOVIE FOR 5 MIN, ASK FOR A RIDE, or TALK WITH YOUR FRIENDS. Which one? ''')
    choice2 = str.upper(answer_2)
    if choice2 == 'ANOTHER TIME':
        print('Perfect! you will arrive on time, but you lost watching a movie and eat pizza.')
        break
    elif choice2 == 'GRAB A PIZZA':
        print('You will have to eat it while you are walking, but you have a pizza! NOW RUN!!!')
        break
    elif choice2 == 'WATCH MOVIE FOR 5 MIN':
        print('You will probably be late but you will enjoy 5 minutes of the movie with your friends.')
        break
    elif choice2 == 'ASK FOR A RIDE':
        print('You will probably get on time, but it is not sure someone will give you a ride because they will watch a movie and eat pizza...')
        break
    elif choice2 == 'TALK WITH YOUR FRIENDS':
        print('Your social life will become better but your grades not...')
        break
    else:
        print('That is not an option...')

#Third level

while True:
    answer_3 = input('''\nYour class starts in 10 mins so you have the following options: 
RUN, WALK NORMAL, JUST STAY IN THE APARTMENT, RELAX AND THINK ABOUT LIFE, PLAY VIDEOGAMES, GET A NAP, WALK TO THE LIBRARY, GO TO TUTORING, 
GO FOR A WALK, or GO PLAY BASKETBALL. Choose one!  ''')
    choice3 = str.upper(answer_3)
    if choice3 == 'RUN':
        end = print('You made it!! but... The class was canceled by the professor... So, you can just go back home and enjoy maybe the movie with the pizza.')
        print('THANK YOU FOR PLAYING')
        break
    elif choice3 == 'WALK NORMAL':
        print('You are gonna be late! RUNN!! Because you decide to do not run, you arrived late to the class and had a penalty by the professor.')
        print('THANK YOU FOR PLAYING')
        break
    elif choice3 == 'JUST STAY IN THE APARTMENT':
        print('You are lazy but you will be able to see the material on Canvas at least... The internet of the apartment just got bad so you do not have internet.')
        print('THANK YOU FOR PLAYING')
        break
    elif choice3 == 'RELAX AND THINK ABOUT LIFE':
        print('REALLY? YOUR LIFE IS PASSING NOW... GO TO CLASS AND LEARN!!!')
        print('THANK YOU FOR PLAYING')
        break
    elif choice3 == 'PLAY VIDEOGAMES':
        print('The power in the apartment went off and it will not come back for 3 hours... GOOD LUCK WITH THAT!')
        print('THANK YOU FOR PLAYING')
        break
    elif choice3 == 'GET A NAP':
        print('You got the Nap! but... There is already midnight...')
        print('THANK YOU FOR PLAYING')
        break
    elif choice3 == 'WALK TO THE LIBRARY':
        print('You found a good friend that invited you to a party tonight! You had so much fun and found possibles dates.')
        print('THANK YOU FOR PLAYING')
        break
    elif choice3 == 'GO TO TUTORING':
        print('You review and learned the material of the class you did not attended. You got an A on the next exam for that class!')
        print('THANK YOU FOR PLAYING')
        break
    elif choice3 == 'GO FOR A WALK':
        print('You got free MCDONALS because you found an old best friend. You went back to the apartment with you friend and got fun playing Video Games')
        print('THANK YOU FOR PLAYING')
        break
    elif choice3 == 'GO PLAY BASKETBALL':
        print('You found the best team to go play basketball and you had the best time eveer!')
        print('THANK YOU FOR PLAYING')
        break
    else:
        print('SORRY, but you could learn the lesson about not choosing one of the options...')
        
