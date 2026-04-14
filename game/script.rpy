# Declare characters used by this game. The color argument colorizes the
# name of the character.
default year = 1848
default action_points = 8
default actions_taken_this_year = []
default max_ap = 8
default played_events = []

# stats
default blood = 10
default iron = 10
default threat = 0

# starting affection for each state (out of 100)
default suitor_relations = {
    "Bavaria": 30,                 # Dramatic, leans toward Austria
    "Baden-Wurttemberg": 30,       # Follows Bavaria's lead
    "Hesse": 50,                   # Completely indecisive (dead center)
    "Saxony": 10,                  # Austria's bestie, hates you
    "Hanover": 20,                 # cut-off nepo baby
    "Mecklenburg-Vorpommern": 80,  # Quiet farm girl already in love
    "Schleswig": 40,               # The half-Danish half of the duo
    "Holstein": 40                 # The fully German half
}




# The game starts here.

label start:   
    scene black
    
    "This is a game about the Unification of Germany."

    "It runs from the Revolutions of 1848 all the way to up to 1871."

    "You are Prussia, one of the strongest German states around, and a state with a feared army and a rapidly growing economy."
    
    show prussia smug at center 
    with easeinright
    
    p "Hola."

    "Throughout this game, you must use your wits and skills of persuasion to become the unifier of Germany."

    "You are, however, not alone."

    "In the post-Congress of Vienna world, you must tread lightly to avoid arousing the intervention of the Great Powers."

    "Remember to save often, because if you make the wrong choice it'll be game over :)"

    "Sigh... A version that lets you do alt-history might come later. But it's EHAP, so..."

    "We love you Ms Garafola... please give us a 100..."

    "Everything in the 'historical choices' section of each menu is an actual historical event that could be of importance to you."

    "They'll be important for game progression, so keep an eye out!"

    "If you don't manage to get through all of them, you can always play through them in another playthrough. You don't need to complete all of them to win."

    show prussia joyful
    p "Don't take this too seriously, and best of luck!"

    jump turn_start


label turn_start:

    if year == 1848:
        play music ["music/revolutionaryetude.ogg"] fadeout 2.0 fadein 1.0 if_changed
        
    elif year == 1851:
        play music ["music/diemoldau.ogg",] fadeout 2.0 fadein 1.0 if_changed
        
    elif year == 1862:
        play music ["music/hohenfriedberger.ogg", "music/vondertann.ogg", "music/grussankiel.ogg", "music/petersburger.ogg"] fadeout 2.0 fadein 1.0 if_changed
    
    elif year == 1867:
        play music ["music/koniggratzermarch.ogg", "music/altekameraden.ogg"] fadeout 2.0 fadein 1.0 if_changed

    elif year == 1870:
        play music ["preussensgloria.ogg"] fadeout 2.0 fadein 1.0 if_changed

    # create the label name for the current year
    $ expected_label = "event_" + str(year)

    # check if the event exists + haven't played it yet
    if renpy.has_label(expected_label) and year not in played_events:
        
        # mark as played so it doesn't loop infinitely
        $ played_events.append(year) 
        
        # call the event + will return here when finished.
        call expression expected_label

    # will display the screen and pause until a Return() action is triggered
    scene bg prussia office
    call screen main_turn_screen
    
    $ chosen_action = _return 

    if chosen_action == "advance_year":
        $ year += 1
        $ action_points = max_ap
        $ actions_taken_this_year = []
        
        jump turn_start

    else:
        $ action_points -= chosen_action["cost"].get("ap", 0)

        $ actions_taken_this_year = actions_taken_this_year + [chosen_action["target"]]

        if "reward" in chosen_action:
            $ blood += chosen_action["reward"].get("blood", 0)
            $ iron += chosen_action["reward"].get("iron", 0)
            $ threat += chosen_action["reward"].get("threat", 0)
            $ max_ap += chosen_action["reward"].get("max_ap", 0)
            
            # loops through every state in suitor list.
            python:
                for state in suitor_relations.keys():
                    reward_key = "affection_" + state
                    if reward_key in chosen_action["reward"]:
                        suitor_relations[state] += chosen_action["reward"][reward_key]
                        
                        # Cap affection at 100 and prevent it from dropping below 0
                        if suitor_relations[state] > 100:
                            suitor_relations[state] = 100
                        elif suitor_relations[state] < 0:
                            suitor_relations[state] = 0

    $ target_label = chosen_action["target"]
    jump expression target_label

    # Loop back to the start of the turn
    jump turn_start
