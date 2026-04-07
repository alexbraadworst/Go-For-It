# 1848
label diplo_1848_duckwitz:
    scene bg prussia office
    
    show duckwitz at left
    show prussia normal at right
    duckwitz "The solution to our commercial disunity is simple. We offer a third way: neither total protectionism, nor total free trade!"
    
    p "I'm listening. But if you say the word 'tariff', the coastal states are going to have a panic attack."
    
    duckwitz "It is a perfectly balanced system! We abolish the sugar monopolies and lower the iron tariffs to appease the British."
    
    duckwitz "But, we implement a flat 25 percent tariff on imported manufactured goods to protect our own inland industries."
    
    duckwitz "By offering them this compromise, we will force Britain to officially recognize this Assembly as the supreme commercial power in Germany!"
    
    show prussia frustrated
    
    p "You want to use coercive tariffs to manipulate the British Empire into recognizing you politically?"
    
    p "Have you ever actually met an Englishman?"
    
    duckwitz "Lord Cowley seemed highly receptive to the liberal aspects of the plan!"
    
    p "They're free-trade zealots! The Board of Trade is going to laugh in your face."
    
    "Duckwitz ignores your warning and submits the plan to London. Britain immediately rejects it as a violation of free-trade dogma, just as you predicted."

    scene bg frankfurt parliament

    "Back at the Paulskirche, the Economic Committee is in a state of total panic."

    show prussia smug at left

    p "Let me get this straight. Duckwitz actually thought he could trick the British Board of Trade?"
    
    show hanover sad at right
    
    hr "It was a perfectly reasonable compromise! A twenty-five percent tariff to protect our infant industries, while offering London a few liberalized trade routes in return. It’s brilliant!"
    
    show prussia intense
    
    p "Hanover, you naive, coastal idiot. The British don’t do 'compromise.' They do 'Free Trade'."
    p "Duckwitz handed them a protectionist tariff. Did you honestly think they wouldn't notice?"
    
    hide hanover
    show bavaria frustrated at right
    
    b "Easy for Hanover to say! Her ports are flooded with cheap British textiles anyway! If we open our markets to London, my local factories will be bled dry in a month!"
    
    show austria smug at center
    
    a "It is rather amusing watching your little 'National Assembly' tear itself apart over cotton imports. Statecraft is clearly too complex for you."
    
    show prussia frustrated
    
    p "Shut up, Austria."
    p "Bavaria, stop crying. Hanover, stop reading pamphlets written by Richard Cobden. The Duckwitz plan is dead."
    
    hide austria
    hide bavaria
    show hanover frustrated at right
    
    hr "Dead?! But Lord Cowley said..."
    
    p "Lord Cowley is an ambassador, not an economist! The Board of Trade just sent back a ten-page lecture on the 'inevitabilities of the free market'. They flat-out refused our terms."
    
    "Prussia slams a heavy, leather-bound ledger onto the table."
    
    show prussia smug
    
    p "The Frankfurt Assembly has no power, no recognition, and no money. You are begging foreign empires for permission to manage your own economies."
    p "There is only one economic power in Germany that actually functions, the Zollverein."
    
    menu:
        "Threaten to extend the Zollverein's borders. (Rally the south to your side)":
            p "If you want actual protection from British industrial syndicates without begging London for scraps, my customs union is extending its borders next year."
            p "You either integrate your economies with mine, or you drown in cheap English iron. Choose."
            
            "Hanover looks furious, but Bavaria and the inland states look visibly relieved to have a protector."
            
            $ iron += 10
            $ threat += 15
            $ suitor_relations["Hanover"] -= 20
            $ suitor_relations["Bavaria"] += 10
            $ suitor_relations["Baden-Wurttemberg"] += 10
            $ suitor_relations["Saxony"] += 10
            $ suitor_relations["Hesse"] += 10
            
            jump turn_start

        "Spread rumors about British spies. (Avoid causing a scene)":
            p "Have you noticed how many 'English gentlemen' have been wandering around the coastal ports lately?"
            p "Hanover, Hamburg... they aren't trying to unite Germany. They're trying to turn us into a British economic colony."
            
            "Bavaria gasps, immediately side-eyeing Hanover. The southern states cluster slightly closer to you."
            
            $ threat -= 5
            $ suitor_relations["Bavaria"] += 5
            $ suitor_relations["Baden-Wurttemberg"] += 5
            $ suitor_relations["Saxony"] += 5
            $ suitor_relations["Hesse"] += 5
            
            jump turn_start

# 1849