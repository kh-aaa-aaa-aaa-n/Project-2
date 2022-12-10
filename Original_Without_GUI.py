def main() -> None:
    """
    Asks a series of questions to get the Latin translation for a Dungeons & Dragons spell.
    """
    # FIXME: The way I have the dictionary looping designed, there is a problem where it loops through
    #        all the letters of a spell, if there's only one listed in the tuple.
    #        While I could try to fix this in the code, it would be far easier and far more effective
    #        long-term to just add spells to the dictionary.
    # The nested dictionaries the whole program relies on.
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
    
    # TODO: Create an option where the user can ask for the translation of a specific spell.
    
    # Prints the first menu.
    print('Choose a class:')
    print('-' * 25)
    
    # Gets the class selection and makes sure it's a valid input.
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
    
    # Prints the second menu.
    print('\n\nChoose a spell level:')
    print('-' * 25)
    
    # Gets the spell level selection and makes sure it's a valid input.
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
    
    # Prints the third menu.
    print('\n\nChoose a spell:')
    print('-' * 25)
    spells_dict_travel = spells['English'][class_selection][spell_level_selection]
    for pos, val in enumerate(spells_dict_travel):
        print(f'{val} - {pos}\n')
    
    # Gets the spell selection index and makes sure it's a valid input.
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
    
    # Uses the spell selection index to find the equivalent in the Latin path.
    print(f'\n\n{spells_dict_travel[spell_selection]} in Latin:')
    print('-' * 25)
    print(spells['Latin'][class_selection][spell_level_selection][spell_selection])

if __name__ == '__main__':
    main()