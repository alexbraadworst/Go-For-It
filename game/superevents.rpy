

label event_1848:
    scene bg 1848
    
    "It is March of 1848. The people are in the streets."

    "News from France abot the success of the February Revolution has compounded fanned frustration over widespread poverty, and the growth of liberal nationalism."

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
    
    "On March 21, King Friedrich Wilhelm IV initiates a change of course by announcing his support of the formation of an all-German parliament, riding through Berlin wearing a black-red-gold armband and giving impromptu speeches about his support for German unity."

    "By the 29th, he appoints a liberal government which, on the 2nd of April, announces elections to form a Prussian National Assembly."

    "This Parliament decides to work with the German Confederation's Federal Convention to form a national assembly with the purpose of writing a constitution for the Confederation."

    scene bg frankfurt parliament

    "It is May. The delegates elected to the Assembly are largely representative of moderate liberalism: free speech, constitutional monarchy, religious tolerance, and the abolition of aristocratic privileges."






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