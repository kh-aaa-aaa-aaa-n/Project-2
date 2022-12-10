# I'm going to try to write the program with various different data storage varieties such as csv, SQL
# database(s), and nested dictionaries. I'll probably go with the database once I figure it out as you
# could more easily make changes and expand later on.
#
# Everything is also still in early prototype mode as much of the code is hardcoded rather than the actual
# implementation I'm going for, so I'll fix that when I figure out how and un-hardcode the program.
from tkinter import Tk, Frame, Label, Button, StringVar, Radiobutton, OptionMenu

class DndEnLaSpellDict:  
    """
    Represents the details for a DndEnLaSpellDict object.
    """
    def __init__(self) -> None:
        """
        Constructor to initialize a DndEnLaSpellDict instance.
        """
        # TODO: Create an option where the user can ask for the translation of a specific spell.
        
        # Creates the main/root window
        self.window = Tk()
        self.window.title('English to Latin D&D Spell Dictionary')
        self.window.geometry('375x175')
        self.window.resizable(False, False)
        
        # Creates all the frames used inside the main window
        self.title_frame = Frame(self.window)
        self.selection_frame = Frame(self.window)
        self.translation_frame = Frame(self.window)
        
        # Creates the label in title_frame
        self.title_label = Label(self.title_frame, text = 'English to Latin D&D Spell Dictionary',
                                 pady = 15)
        
        # Creates the label in translation_frame
        self.translation_label = Label(self.translation_frame, pady = 10)
        
        # Creates the button in selection_frame
        self.translate_button = Button(self.selection_frame, text = 'Translate',
                                       command = self.clicked_translate)
        
        # TODO: Implement a reset button
        # self.reset_button = Button(self.selection_frame, text = 'Reset')
        # self.reset_button.grid()
        
        # Creates the radio buttons in selection_frame
        self.selected = StringVar()
        self.selected.set('English')
        self.english_radiobutton = Radiobutton(self.selection_frame, text = 'English', value = 'English',
                                 variable = self.selected)
        self.latin_radiobutton = Radiobutton(self.selection_frame, text = 'Latin', value = 'Latin',
                                 variable = self.selected)
        
        # FIXME: Temporary implementation of the option menus and selection system
        # Creates the option menus in selection_frame
        self.classes = ['Warlock', 'Wizard']
        self.chosen_class = StringVar()
        self.chosen_class.set(self.classes[0])
        self.class_select_om = OptionMenu(self.selection_frame, self.chosen_class, *self.classes)
        
        self.spell_levels = ['Cantrip', '1st Level', '2nd Level']
        self.chosen_level = StringVar()
        self.chosen_level.set(self.spell_levels[0])
        self.level_select_om = OptionMenu(self.selection_frame, self.chosen_level, *self.spell_levels,
                                          command = self.spell_level_choice)
        
        self.eng_second_level = ['Darkness']
        self.chosen_eng_spell = StringVar()
        self.chosen_eng_spell.set(self.eng_second_level[0])
        self.eng_second_level_om = OptionMenu(self.selection_frame, self.chosen_eng_spell,
                                              *self.eng_second_level)
        
        self.eng_first_level = ['Illusory Script']
        self.chosen_eng_spell = StringVar()
        self.chosen_eng_spell.set(self.eng_first_level[0])
        self.eng_first_level_om = OptionMenu(self.selection_frame, self.chosen_eng_spell,
                                             *self.eng_first_level)
        
        self.eng_cantrips = ['Eldritch Blast', 'Minor Illusion']
        self.chosen_eng_spell = StringVar()
        self.chosen_eng_spell.set(self.eng_cantrips[0])
        self.eng_cantrip_om = OptionMenu(self.selection_frame, self.chosen_eng_spell, *self.eng_cantrips)
        
        # TODO: Implement Latin to English support
        # self.lat_cantrips = ['Dryegnum Missilis', 'Parvus Illūsiō']
        # self.chosen_lat_spell = StringVar()
        # self.chosen_lat_spell.set(self.lat_cantrips[0])
        # self.lat_cantrip_om = OptionMenu(self.selection_frame, self.chosen_lat_spell, *self.lat_cantrips)
        
        # self.lat_first_level = ['Vānum Scrīptum']
        # self.chosen_lat_spell = StringVar()
        # self.chosen_lat_spell.set(self.lat_first_level[0])
        # self.lat_first_level_om = OptionMenu(self.selection_frame, self.chosen_lat_spell,
        #                                      *self.lat_first_level)
        
        # self.lat_second_level = ['Cālīgō']
        # self.chosen_lat_spell = StringVar()
        # self.chosen_lat_spell.set(self.lat_second_level[0])
        # self.lat_second_level_om = OptionMenu(self.selection_frame, self.chosen_lat_spell,
        #                                       *self.lat_second_level)
        
        # Packs title_label in title_frame
        self.title_label.pack()
        
        # Packs translation_label in translation_frame
        self.translation_label.pack()
        
        # Puts the button, radio buttons, and option menus in selection_frame with grid
        self.translate_button.grid(row = 1, column = 2, padx = 2, pady = 5)
        self.english_radiobutton.grid(row = 0, column = 0, pady = 5)
        self.latin_radiobutton.grid(row = 0, column = 2, pady = 5)
        self.class_select_om.grid(row = 0, column = 1, padx = 2, pady = 5)
        self.level_select_om.grid(row = 1, column = 0, padx = 2, pady = 5)
        self.eng_cantrip_om.grid(row = 1, column = 1, padx = 2, pady = 5)
        
        # Packs the frames to the main window
        self.title_frame.pack()
        self.selection_frame.pack()
        self.translation_frame.pack()
    
    # TODO: Implement non-hardcoded version of clicked_translate
    def clicked_translate(self) -> None:
        """
        Takes the chosen spell and projects its translation onto the frame.
        """
        spell: str = self.chosen_eng_spell.get()
        
        # FIXME: Herdcoded. Add proper implementation.
        #        Also, have it display special characters properly
        if spell == 'Darkness':
            self.translation_label.config(text = 'Darkness in Latin is: Caligo')
        elif spell == 'Illusory Script':
            self.translation_label.config(text = 'Illusory Script in Latin is: Vanum Scriptum')
        elif spell == 'Eldritch Blast':
            self.translation_label.config(text = 'Eldritch Blast in Latin is: Dryegnum Missilis')
        elif spell == 'Minor Illusion':
            self.translation_label.config(text = 'Minor Illusion in Latin is: Parvus Illusio')
    
    def spell_level_choice(self, x = '') -> None:
        """
        Sets the OptionMenu to the chosen level.
        
        :param x: I honestly don't know why this is here or why it works, but it's required for the
                  implementation to work properly. Don't touch it, or it may break the function.
        """
        level: str = self.chosen_level.get()
        
        # FIXME: Instead of forgetting and adding back to the grid, have it actually change the values
        #        in a single option menu
        self.eng_cantrip_om.grid_forget()
        self.eng_first_level_om.grid_forget()
        self.eng_second_level_om.grid_forget()
        if level == 'Cantrip':
            self.eng_cantrip_om.grid(row = 1, column = 1, padx = 2, pady = 5)
            self.chosen_eng_spell.set(self.eng_cantrips[0])
        elif level == '1st Level':
            self.eng_first_level_om.grid(row = 1, column = 1, padx = 2, pady = 5)
            self.chosen_eng_spell.set(self.eng_first_level[0])
        elif level == '2nd Level':
            self.eng_second_level_om.grid(row = 1, column = 1, padx = 2, pady = 5)
            self.chosen_eng_spell.set(self.eng_second_level[0])
    
    def start(self) -> None:
        """
        Engages the loop to open and keep the window on.
        """
        self.window.mainloop()

if __name__ == '__main__':
    DndEnLaSpellDict().start()