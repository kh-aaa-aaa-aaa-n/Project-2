# TODO: Put everything into a GUI once I figure out how to store/represent the nested dictionaries.
# def main():
spells = {'English': {
                      'Warlock': {
                                  'Cantrip': ('Eldritch Blast', 'Minor Illusion'), 
                                  '1st Level': ('Illusory Script'), 
                                  '2nd Level': ('Darkness')}, 
                      'Wizard': {
                                 'Cantrip': ('Friends'), 
                                 '1st Level': ('Shield'), 
                                 '2nd Level': ('Darkness')}}, 
          'Latin': {
                    'Warlock': {
                                'Cantrip': ('Dryegnum Missilis', 'Parvus Illūsiō'), 
                                '1st Level': ('Vānum Scrīptum'), 
                                '2nd Level': ('Cālīgō')}, 
                    'Wizard': {
                               'Cantrip': ('Amīcī'), 
                               '1st Level': ('Scūtum'), 
                               '2nd Level': ('Cālīgō')}}}

print('Choose a class:')
print('_________________________')
class_selection = input('Warlock - 0\nWizard - 1\nClass: ')
while True:
    if class_selection == '0' or class_selection == 'Warlock':
        class_selection = 'Warlock'
        break
    elif class_selection == '1' or class_selection == 'Wizard':
        class_selection = 'Wizard'
        break
    else:
        class_selection = input('\nInvalid input. Choose one of the given options.\n')

print('\n\nChoose a spell level:')
print('_________________________')
spell_level_selection = input('Cantrip - 0\n1st Level - 1\n2nd Level - 2\nSpell Level: ')
while True:
    if spell_level_selection == '0' or spell_level_selection == 'Cantrip':
        spell_level_selection = 'Cantrip'
        break
    elif spell_level_selection == '1' or spell_level_selection == '1st Level':
        spell_level_selection = '1st Level'
        break
    elif spell_level_selection == '2' or spell_level_selection == '2nd Level':
        spell_level_selection = '2nd Level'
        break
    else:
        spell_level_selection = input('\nInvalid input. Choose one of the given options.\n')

print('\n\nChoose a spell:')
print('_________________________')
spells_dict_travel = spells['English'][class_selection][spell_level_selection]
for pos, val in enumerate(spells_dict_travel):
    print(f'{val} - {pos}\n')

spell_selection = input('Spell: ')
loop = True
while loop:
    for i in range(pos + 1):
        if spell_selection == f'{i}' or spell_selection == f'{spells_dict_travel[i]}':
            spell_selection = i
            loop = False
            break
    if loop:
        spell_selection = input('\nInvalid input. Choose one of the given options.\n')
    else:
        break

print('\n\nChosen spell in Latin:')
print('_________________________')
print(spells['Latin'][class_selection][spell_level_selection][spell_selection])

# if __name__ == '__main__':
#     main()