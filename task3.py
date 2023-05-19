#DS-Task-4

#task: Design a program that determines the award a person competing in a triathlon will receive'
swimming = input('Please enter the finish time for swimming in minutes: ')
cycling = input('Please enter the finish time for cycling in minutes: ')
running = input('Please enter the finish time for running in minutes: ')
triathlon = int(swimming) + int(cycling) + int(running)
print(f'The participant\'s total time was {triathlon} minutes.')


#store times and correcsponding awards in list
provincial_colours = 100
provincial_half_colours = 105
provincial_scroll = 110

if triathlon <= provincial_colours:
        print('The participant has won the Provincial Colours award.')

elif triathlon <= provincial_half_colours and triathlon >= provincial_colours:
        print('The participant has won the Provincial Half Colours award.')

elif triathlon <= provincial_scroll and triathlon >= provincial_half_colours:
        print('The participant has won the Provincial Scroll award.')

else: 
    print('No award for the participant.')
