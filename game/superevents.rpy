

label event_1848:
    scene black with fade
    centered "{b}{size=40}Act 1: Chapter 1{/size}{/b}\n1848 - Springtime of Nations" with dissolve
    pause 1.0
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
    
    "October 1848. The National Assembly has convened once again at the Paulskirche in Frankfurt."
    "Hundreds of delegates are arguing over borders, national unification, and the very definition of a 'German'."
    
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
    
    "The tension in the room is palpable. You have a brief window to sway the delegates before the final debate next year."

    "Focus on building greater relationships with your fellow German states in the Relationships tab!"
    
    jump turn_start

label event_1849:
    scene black with fade
    centered "{b}{size=40}Act 1: Chapter 2{/size}{/b}\n1849 - A Crown from the Gutter" with dissolve
    pause 1.0

    scene bg street battle

    "April 1849. Prussian troops have crushed popular movements across the Confederation."

    "Friedrich Wilhelm IV has additionally reasserted his authority, dissolving the Prussian Constituent Assembly."

    scene bg frankfurt parliament2

    "Despite all this, the Frankfurt Parliament has reconvened for the final vote on the constitution."
    
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

    scene bg prussia office
    
    "It's May 1849."

    "Now that he's rejected the Crown from the Gutter, Friedrich Wilhelm IV has decided to establish a German empire on a more conservative base."
    
    show prussia neutral at left
    show fwiv at right
    
    fwiv "Gentlemen, thank you for making the journey to Berlin. These are dark, chaotic times for the Fatherland."
    
    hide fwiv
    show ea at right
    
    ea "Let us skip the pleasantries, Frederick. I am an old man, and my carriage ride was entirely too bumpy."
    ea "You called us here to propose a union, one where Prussia conveniently holds all the military authority."
    
    hide ea
    show faii at right
    
    faii "It is a massive overreach! You are asking us to surrender our foreign policy and our armies to Berlin." 
    faii "What will Austria say when they hear about this?"
    
    show prussia smug
    
    p "Austria is currently busy begging Russia for help because they can't win against Hungary."

    p "Vienna is not going to save you. Frankly, your own armies aren't going to save you either."
    
    show prussia intense
    
    p "Need I remind you, King Frederick Augustus, that just last week my infantry had to clear the barricades out of your capital?" 
    
    p "You were practically packing your bags to flee Dresden."
    
    faii "I..."

    faii "Well, the situation was uniquely volatile..."
    
    show prussia smug
    
    p "The situation is that the liberal mobs want your heads."
    p "Their attempt at unity failed, but the idea's still popular."
    p "So. if you're going to survive, you'll have to help build a new and conservative union."
    
    hide faii
    show ea at right
    
    ea "You are arrogant, Prussia. You always have been."
    ea "However, the enemy of my enemy..." 
    ea "Fine. Pass me the quill. Hanover will join your Three Kings Alliance. I don't know if Hanover herself will have much nicer to say."
    
    hide ea
    show faii at right
    
    faii "If Hanover signs... then I suppose Saxony has no choice. Austria will not forget this, though."
    
    show prussia joyful
    
    p "Let them remember. By the time Vienna sorts out its own mess, I'll have all of Northern Germany!"
    
    "The two kings reluctantly sign the treaty, formally creating the Alliance of the Three Kings."
    "You have successfully seized the diplomatic initiative, but you can feel the geopolitical tension rising." 
    "You have just drawn a massive target on your back."
    
    $ iron += 15
    $ threat += 50
    return

label event_1850:
    scene black with fade
    centered "{b}{size=40}Act 1: Chapter 3{/size}{/b}\n1850 - The Humiliation of Olmutz" with dissolve
    pause 1.0
    scene bg prussia office
    
    "It is March 1850."
    "After rejecting the liberal crown last year, you and King Frederick William IV have attempted to make your own, highly conservative German union."
    
    show prussia smug at left
    show fwiv at right
    
    p "There won't be any crown from the gutter for us. Our own union, on our own terms."
    
    fwiv "Yes, well... I'm glad Hanover and Saxony agreed to the Three Kings' Alliance. It gives us legitimacy."
    
    "You look across the room. Hanover and Saxony are standing by the door, sweating profusely and whispering to each other."
    
    show hanover embarrassed at center
    
    hr "Prussia, listen. This was a lovely idea, really it was. But..."
    
    show austria intense
    
    a "You really thought you could just lock me out of Germany while I was distracted?!"
    
    show prussia neutral
    
    p "Austria... We were just organizing the northern states. It's nothing for you to worry about."
    
    show austria frustrated with vpunch

    a "I am the President of the German Confederation!"

    a "I demand you dissolve this illegal 'Erfurt Union' immediately!"

    a "Saxony! Hanover! If you know what's good for you, you will walk out that door right now."
    
    "Saxony and Hanover don't even hesitate. They instantly bolt from the room."
    
    show prussia frustrated
    
    p "Cowards! Both of you!"

    p "You don't scare me, Austria."

    p "You may have the title, but I have the best infantry in Europe, I'm not backing down."
    
    scene bg field
    
    "November 1850. The crisis escalates."
    "A constitutional crisis erupts in the central state of Hesse. Austria uses this as a pretext to mobilize the Federal Diet's army against Prussian interests."
    
    show hesse sad at left
    
    h "Prussia, help! My people are rioting, and Bavaria just crossed my southern border with a massive army!"
    
    show bavaria intense at right
    
    b "I am acting on the legal orders of Austria and the restored Federal Diet! Stand aside, Prussia!"
    
    show prussia intense at center
    
    p "You are marching on my military transit roads! If one Bavarian boot touches my supply lines, I will consider it an act of war!"
    
    show bavaria sad with vpunch

    b "Don't do this! I don't want to fight you, but Austria ordered me to restore order!"
    
    "The armies collide at the town of Bronzell. Shots ring out. A white horse is killed in the crossfire."
    "You are moments away from ordering a full-scale artillery barrage when..."
    
    scene bg field

    show prussia normal at left
    show russia intense at right
    
    p "Russia..."
    
    ru "Step down! The Russian Empire stands firmly behind Austria."
    ru "You will not destroy the conservative order of Europe just to satisfy your own ego. If you fire on the Bavarians again, my armies will cross your eastern border."
    
    show austria smug at center
    
    a "Did you really think you could win a two-front war against the Russian Empire and the Austrian Empire?"
    a "You are a regional power, Prussia. Act like one. Meet me at Olmütz to sign your surrender."
    
    "Your hands shake. The military math in your head is brutal and undeniable. Your army is simply not large enough to fight both empires."
    
    scene bg negotiation room
    
    "November 29, 1850. The Punctation of Olmütz."
    "In a small room in Moravia, you are forced to sign a treaty formally abandoning the Erfurt Union."
    "You officially submit to Austrian supremacy and agree to the total restoration of the old German Confederation."
    
    show prussia angry at center with vpunch
    
    "It is the greatest diplomatic humiliation in Prussian history."
    
    p "Enjoy this, Austria. Enjoy this while my foundries are still small and my railways are still short."
    p "This isn't over. I will never forget this room."
    
    scene bg landtag
    
    "At the Landtag, the liberal deputies are screaming in absolute outrage. They accuse the government of cowardice, demanding a war of honor against Austria."
    
    show prussia frustrated at left
    
    p "Idiots. All of them. They want me to commit state suicide just to save face."
    
    "Suddenly, a tall, imposing, heavily-built conservative deputy stands up. The room falls quiet."
    
    show ovb at center
    
    "A Deputy" "Why do major states wage war today?"
    
    show prussia normal
    
    p "...Who is that?"
    
    "A Deputy" "The only healthy foundation of a large state, and this is what essentially distinguishes it from a small state, is state egoism and not romanticism."
    "A Deputy" "It is not worthy of a great state to fight for a cause not inherently its own."

    "A Deputy" "So, gentlemen, show me a goal worthy of war, and I will agree with you."

    "A Deputy" "It is easy for a statesman to blow the trumpet of war with the popular wind, while warming himself by his fire, or uttering thunderous speeches from that platform."
    "A Deputy" "He leaves it to the musketeer bleeding to death on the snow whether his system shall win victory and glory or not."

    "A Deputy" "...Nothing is easier than that, but woe to the statesman who does not look for a reason for war at this time that will still be valid after the war!"

    "A Deputy" "Will you then have the courage to stand up to the farmer at the site of his burned-down farm, to the crippled man who has been shot, to the childless father and say:"
    
    "A Deputy" "You have suffered a lot, but rejoice with us, the Union Constitution has been saved."
    
    show prussia intense
    
    "You stare at the man, completely captivated."
    
    p "Egoism over romanticism... he understands. He actually understands."
    p "Who is that deputy?"
    
    "A clerk leans over to you."
    
    "Clerk" "Him? Oh, he's just a loud, ultra-conservative Junker from Pomerania. Otto von Bismarck. Nobody important."
    
    show prussia smug
    
    p "Bismarck. I'll remember that name."
    
    "The humiliation of Olmütz is complete, but the seeds of your ultimate revenge have been planted."

    # Resolving the massive crisis
    $ iron -= 20
    $ threat -= 30 
    $ max_ap += 1 # You learn a harsh lesson in Realpolitik and gain administrative focus
    
    jump turn_start

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