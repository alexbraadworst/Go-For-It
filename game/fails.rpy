label fail_1848_crackdown:
    scene bg classroom
    show prussia angry at center
    
    p "Woah woah woah wait there a minute. Crack down hard!??"
    p "Friedrich Wilhelm IV was a compassionate guy. He caved in to their demands and promised a liberal constitution with a future merger with the German nation-state! (Textbook pg. 434)"
    
    "Prussia-chan drops your grade to a 0!"
    "By the way, if you're salty about losing, remember to save next time..."

    $ MainMenu(confirm=False)()

label fail_state_crown:
    show prussia angry at center with vpunch
    
    p "Wait, why did I just say that?! My army isn't ready!"
    
    "Austria and Russia, terrified of a liberal, Prussian-led Germany, immediately mobilize."
    "Prussia is invaded on two fronts and utterly dismantled. The King is forced to abdicate."
    
    p "We needed to isolate Austria diplomatically and reform the army first! Did you sleep through the entire unit on Realpolitik?!"
    
    "HISTORICAL INACCURACY DETECTED. F IN AP EURO."
    
    # Kick them to the main menu!
    $ MainMenu(confirm=False)()