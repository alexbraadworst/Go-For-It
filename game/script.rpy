# Declare characters used by this game. The color argument colorizes the
# name of the character.
default year = 1848
default action_points = 8
default max_ap = 8
default played_events = [] # A list to track which years we've already seen

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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    
    "This is a game about the Unification of Germany."

    "You are Prussia, one of the strongest German states around, and a state with a feared army and a rapidly growing economy."

    "Throughout this game, you must use your wits and skills of persuasion to become the unifier of Germany."

    "You are, however, not alone."

    "In the post-Congress of Vienna world, you must tread lightly to avoid arousing the intervention of the Great Powers."

    "Remember to save often, because if you make the wrong choice it'll be game over :)"

    "Sigh... A version that lets you do alt-history might come later. But it's EHAP, so..."

    "Best of luck!"

    jump turn_start

    # This ends the game.

label turn_start:
    

    # create the label name for the current year
    $ expected_label = "event_" + str(year)

    # 3. Check if the event exists + haven't played it yet
    if renpy.has_label(expected_label) and year not in played_events:
        
        # Mark as played so it doesn't loop infinitely
        $ played_events.append(year) 
        
        # Call the event, will return here when finished.
        call expression expected_label

    # This will display the screen and pause until a Return() action is triggered
    scene bg prussia office
    call screen main_turn_screen
    
    $ chosen_action = _return 

    if chosen_action == "advance_year":
        $ year += 1
        $ action_points = max_ap # Replace 5 with whatever their max AP should be!
        
        # Jumping back to the top triggers the next year's historical events
        jump turn_start
    
    # --- DEDUCT ACTION POINTS ---
    $ action_points -= chosen_action["cost"].get("ap", 0)

    # --- APPLY PROGRESSION & THREAT ---
    if "reward" in chosen_action:
        $ blood += chosen_action["reward"].get("blood", 0)
        $ iron += chosen_action["reward"].get("iron", 0)
        $ threat += chosen_action["reward"].get("threat", 0)
        
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
    
    # --- DYNAMIC JUMP ---
    $ target_label = chosen_action["target"]
    jump expression target_label

    # Loop back to the start of the turn
    jump turn_start
