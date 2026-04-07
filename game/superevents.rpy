

label event_1848:
    scene bg 1848
    
    "It is March of 1848. The people are in the streets."

    "News from France about the success of the February Revolution has fanned frustration over widespread crop failures, economic crisis, and the growth of liberal nationalism."

    "Now, liberals are calling for Prussia to reform into a constitutional monarchy that can lead the German Confederation into a national state for all Germans."

    show prussia intense at left
    
    show fwiv at right

    fwiv "What are we to do!? The people are all riled up!"

    show prussia frustrated

    p "And whose fault is that!? You let the army charge those protestors at the Tiergarten! The whole reason we have this whole barricade mess is because of that!"

    fwiv "Enough with the past. I need to put an end to this somehow. What do you suppose I should do?"

    menu:
        "Appeal to his vanity (Push for reform)":
            p "They have a point, you know. The days of monarchy are coming to an end, whether you like it or not. You have to ride the wave so you don't drown!"
            fwiv "Absolutely not! God chose me to rule, not a mob of peasants!"
            p "But Your Majesty, think of the history books! Friedrich Wilhelm, the Great Reformer! You'll gain praise from many generations to come!"
            fwiv "Sigh... I suppose you're right. And it wouldn't be good if we sent the army back in. Many innocent lives would be lost."
            fwiv "I suppose I will draft a statement."
        "Appeal to his divine right (Push for crackdown)":
            p "Damn you, you're the King, act like it! Send the army back in and crush them! You need to crack down on this, hard!"
            fwiv "But think of the people..."
            p "Does it matter? You're their king! You were chosen by God!"
            fwiv "Yes... Yes. You're right. I agree. We can't show weakness at this crucial point!"

            jump fail_1848_crackdown
    
    scene bg 1848 king

    "On March 21, King Friedrich Wilhelm IV initiates a change of course by announcing his support of the formation of an all-German parliament."
    
    "Riding through Berlin wearing a black-red-gold armband, he gives impromptu speeches about his support for German unity."

    "By the 29th, he appoints a liberal government which, on the 2nd of April, announces elections to form a Prussian National Assembly."

    "This Parliament decides to work with the German Confederation's Federal Convention to form a national assembly with the purpose of writing a constitution for the Confederation."

    scene bg frankfurt parliament

    "It is May. The delegates elected to the Nationalversammlung are largely representative of moderate liberalism: free speech, constitutional monarchy, religious tolerance, and the abolition of aristocratic privileges."

    "These delegates ignore calls from more radical elements such as the industrial workers, republicans, and socialists for any action more radical than that."

    "On the 18th, these delegates solemnly make their way to the Paulskirche in Frankfurt for the first session."

    scene bg frankfurt parliament2
    
    "Months pass, and it is now October. The National Assembly has convened once again at the Paulskirche in Frankfurt."
    
    "Hundreds of delegates are now arguing over borders, national unification, and the very definition of a 'German'."
    
    show prussia frustrated at left
    
    p "If I have to listen to one more liberal professor talk about Hegelian dialectics, I am going to march my infantry in here and clear the room."
    
    show austria smug at right
    
    a "Patience, Prussia. Statecraft requires elegance. Not that a barracks-state like you would understand."
    
    show prussia intense
    
    p "Cut the act, Austria. We all know why we're here. Are we building a 'Grossdeutschland' with you, or a 'Kleindeutschland' with me?"
    
    a "A Germany without Austria is no Germany at all. The southern states know this."

    p "The deputies won't accept non-Germans within Germany. Your territories in Italy and Hungary will really upset the matter..."

    a "We won't be giving up the empire. They'll have to settle the matter and accept those lands, or they can count us out."

    p "I'll be damned..."
    
    "The tension in the room is palpable. You have a brief window to sway the delegates before the final debate, next year."

    "Focus on building greater relationships with your fellow German states in the Relationships tab, and be sure to take stock of policies in the Diplomacy tab."
    
    return

label event_1849:

    "April 1849. Prussian troops have crushed popular movements across the Confederation."

    "Friedrich Wilhelm IV has additionally reasserted his authority, dissolving the Prussian Constituent Assembly."

    scene bg frankfurt parliament2

    "Despite all this, the Parliament has reconvened for the final vote on the constitution."
    
    show austria angry at right
    
    a "This is a farce! Austria will not divide her empire just to appease a room full of liberal academics!"
    
    a "If you demand we leave Hungary and Italy behind, then we withdraw from this assembly entirely!"
    
    hide austria
    
    show prussia smug at left
    
    p "Don't let the door hit you on the way out."
    
    "With Austria's dramatic exit, the 'Grossdeutschland' solution is dead. The Parliament defaults to 'Kleindeutschland'."
    
    # wooed the south
    if suitor_relations.get("Bavaria", 0) >= 40 and suitor_relations.get("Baden-Wurttemberg", 0) >= 50:
        show prussia smug at left
        
        p "Look at them. All those liberals and minor princes finally falling in line."

        p "Bavaria is eating out of my hand, and Baden knows exactly who keeps their throne safe from republican mobs."

        show prussia joyful
        
        p "Without the South, Austria has no leverage left."
        
        p "I played this perfectly..."
        
        "The smaller states rally behind you. You have successfully isolated Austria from the rest of the Confederation."
        $ iron += 10
        $ threat -= 5
        
    elif suitor_relations.get("Bavaria", 0) >= 40:
        show prussia frustrated at left
        
        p "Bavaria is with me, thank God. That cuts off Austria's main avenue of influence."
        
        show prussia intense
        
        p "But Baden... I should have marched down there and crushed that uprising myself."

        p "A fragmented South is dangerous. I have the majority, but it's a messy, bleeding majority."

        p "Austria isn't gone for good. They're going to use this division against me later. I can already feel a headache coming on."
        
        "You secure the vote, but the lack of total southern unity leaves your flank exposed."
        $ threat += 5
        
    else:
        show prussia frustrated at left with vpunch
        
        p "Damn it. Damn it all."

        p "Bavaria is actively whispering with the Austrian delegation. I can see them glaring at me from across the aisles."
        
        show prussia sad
        
        p "The entire southern bloc is slipping right through my fingers. What the hell was I doing all year? Wasting time on internal bureaucracy while Vienna stole my suitors?!"
        
        show prussia intense
        
        p "Fine. If they won't be wooed by diplomacy and commerce... they'll have to be broken by war. But that's a war I'm not ready for yet!"
        
        "You failed to secure the southern bloc. Austria looks incredibly smug as the states remain divided."
        $ iron -= 5
        $ threat += 25
        
    "Regardless of the southern grumbling, the Parliament finalizes the constitution. They send an imperial deputation to Berlin."
    
    scene bg sanssouci
    show prussia normal at left
    show fwiv at right
    
    "The delegates arrive, carrying the drafted constitution. They offer King Friedrich Wilhelm IV the title: 'Emperor of the Germans'."
    
    fwiv "They... they want me to be Emperor? Of a united Germany?"
    
    p "Don't get too excited. Look at who is offering it. They expect you to answer to a parliament."
    
    menu:
        "Accept the crown.":
            show prussia joyful
            p "Take it! We win! Germany is ours!"
            fwiv "Yes! I accept the will of the people! I am Emperor!"
            jump fail_state_crown

        "Refuse the 'Crown from the Gutter'":
            p "Don't take a crown from the gutter! Tell them no."

            fwiv "You are exactly right. I rule by the grace of God, not by the permission of bakers and lawyers."
            
            fwiv "I refuse your crown! Get out of my palace!"
            
            "The deputation leaves in absolute disgrace."
            "Without Prussian backing, the Frankfurt Parliament collapses. The revolution is effectively over. The old conservative order is restored."
            
            $ threat -= 15
            $ blood += 5
            
            return


label event_1862:
    # 1. Set the scene
    show bismarck serious at left
    
    "The Landtag refuses to fund the military expansion."
    bismarck "The great questions of the time will not be resolved by speeches and majority decisions..."
    bismarck "...but by iron and blood."
    
    return


label event_1871:
    scene bg versailles
    show prussia triumphant at center
    
    "It is January 18th, 1871. The Hall of Mirrors in Versailles is packed."
    
    p "We have done it. Through blood, iron, and a ridiculous amount of Action Points... Germany is united."
    
    "The German Empire is officially proclaimed. The campaign is victorious."
    
    jump end_credits

label end_credits:
    
    # Stop any background music currently playing so it doesn't clash with the video audio
    stop music fadeout 2.0
    
    # Play the video file. 
    # By default, the player can click to skip it. 
    $ renpy.movie_cutscene("movies/ending.webm", delay=244)
    
    "Thank you for playing!"
    
    return