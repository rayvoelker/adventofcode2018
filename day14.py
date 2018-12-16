recipes = '824501'
score = '37'

recipes_list = list(recipes)
scoreboard = list()
scoreboard.append('3')
scoreboard.append('7')

# scoreboard_slice = len(recipes)
# # scoreboard_test = '37824501'

elf1 = 0
elf2 = 1

# print(scoreboard)

recipes_test = '5158916779'
recipes_list = list(recipes_test)

while True:
    if recipes_list == scoreboard[max(0, len(scoreboard) - 10):]:
        print('found!')
        break

    score = list(str(int(scoreboard[elf1]) + int(scoreboard[elf2])))
    for i in range(len(score)):
        scoreboard.append(score[i]) 
    
    elf1 = (elf1 + int(scoreboard[elf1]) + 1) % len(scoreboard)
    elf2 = (elf2 + int(scoreboard[elf2]) + 1) % len(scoreboard)

print('scoreboard: {}'.format(scoreboard))