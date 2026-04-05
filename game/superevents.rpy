

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

    jump event_1848_frankfurt

label event_1848_frankfurt:
    scene bg frankfurt parliament alt
    
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

    "Focus on building greater relationships with your fellow German states in the Relationships tab."
    
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