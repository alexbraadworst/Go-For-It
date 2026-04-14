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

label diplo_1850_denmark_peace:
    scene bg prussia office
    
    "July 1850. The diplomatic fallout from the Danish War is still suffocating your economy. The Great Powers are demanding a final resolution."
    
    show prussia serious at right
    
    "You dip your pen into the inkwell, staring at the Treaty of Berlin."
    "It officially ends hostilities with Denmark... but it explicitly leaves Schleswig and Holstein to fight the Danes entirely on their own."
    
    show schleswig crying at right
    
    sw "Prussia, please! You can't just abandon us! The Danish army is marching back into Jutland!"
    
    show prussia neutral
    
    p "Schleswig, I told you in Malmö that I cannot fight the British Navy and the Russian Army for you."

    p "My supply lines are stretched. My foundries need time to breathe. If I stay in this war, I will drag the entire Fatherland into the abyss."
    
    sw "But you promised us freedom!"
    
    show prussia intense
    
    p "I promised you I would act in the best interests of the state! And right now, the state requires peace."

    show prussia sad

    p "...I'm so sorry."
    
    "You avert your eyes and sign the document."
    
    p "Survive the winter, Schleswig. When I am strong enough to ignore the British, I will return for you. But until then, you are on your own."
    
    "Schleswig runs from the room in tears." 
    "You have appeased the Great Powers, but your reputation among the northern duchies is in ruins."
    
    jump turn_start

label diplo_1851_federal_diet:
    play music "music/radetzky.ogg" fadein 2.0

    scene bg frankfurt exterior with fade
    
    "Following the humiliation at Olmütz, you have been forced to officially abandon your attempts to create a Prussian-led German union."
    "Instead, you must return to the old German Confederation under Austrian leadership."

    show prussia frustrated at center

    p "I'd rather march barefoot across broken Krupp steel."

    show prussia sad

    p "My army wasn't ready. If I had fought her, Russia would have crossed the Vistula and crushed me from behind."
    p "So now... I have to apologize."

    "A tall, imposing man steps up beside you. He casually lights a cigar, entirely unfazed by your foul mood."

    show prussia frustrated at left
    show bismarck at right
    with moveinright

    ovb "Have patience!"
    ovb "Let Austria have her parchment and her titles. We will win the future."

    show prussia normal

    p "You always know exactly what to say to make me feel better, Bismarck."

    show prussia intense

    p "Let's get this over with."

    scene bg frankfurt parliament
    with fade

    "You push open the heavy oak doors. The grand hall of the Federal Diet is packed with delegates from all the German states."
    "At the very front, sitting in the highest, most ornate chair, is Austria."

    show austria smug at center
    with dissolve

    if suitor_relations["Saxony"] >= 20 and suitor_relations["Bavaria"] >= 20:
        
        "She is holding court, sipping from a delicate porcelain teacup. Bavaria and Saxony stand nearby, looking deeply uncomfortable."

        show bavaria sad at left
        show saxony embarrassed at right

        s "Yes... well... it is a complicated geopolitical reality..."

        b "Indeed. Let us just be glad open conflict was avoided."

        "Austria notices you walking down the aisle. The entire room goes dead silent."

        show austria joyful

        a "Oh! Look everyone! The wayward child returns!"

        "Bavaria and Saxony immediately look at the floor, refusing to meet your eyes. Austria might hold the title of President, but they both know exactly whose army saved their thrones last year."

    else:
        
        "She is holding court, sipping from a delicate porcelain teacup while Bavaria and Saxony stand nearby, hanging on her every word."

        show bavaria normal at left
        show saxony joyful at right

        s "And then she just... gave up! It was magnificent, Austria!"

        b "A toast to the true President of the Confederation!"

        "Austria notices you walking down the aisle. The entire room goes dead silent."

        show austria joyful

        a "Oh! Look everyone! The wayward child returns!"

        show saxony smug
        show bavaria smug

    a "Did your little 'Erfurt Union' club not work out, Prussia? I told you, trying to replace me is a fool's errand."

    show prussia frustrated at left
    show austria smug at right_side_sprite
    hide bavaria
    hide saxony
    with move

    p "I am here, as agreed in the treaties, to formally resume my seat in the Federal Diet."

    a "Say it properly, darling."

    show prussia intense
    with vpunch

    "You grind your teeth together so hard you taste blood. You glance toward the back of the room, where Russia is leaning against a pillar, watching you with cold, calculating eyes."

    show russia normal at right

    "He gives you a slow, deliberate nod. A silent threat."

    show prussia frustrated

    p "...I am here to acknowledge the restoration of the German Confederation, under the permanent presidency of the Austrian Empire."

    show austria joyful

    a "Excellent! Now, be a good girl and sign the registry. And try not to start any more silly little rebellions, alright?"

    "You aggressively snatch the quill from the podium and sign your name, pressing so hard the tip snaps."
    "You have officially submitted. The Great Powers are satisfied, and the immediate threat of a two-front war vanishes. But the damage to your pride is immeasurable."

    show prussia smug

    p "Enjoy the presidency, Austria. I brought you a gift to celebrate."

    show austria normal

    a "Oh? A gift? Did you finally learn some manners?"

    p "I am appointing my new permanent envoy to the Diet. He'll be representing my interests here every single day."

    "You step aside, letting Bismarck step forward. He takes a long drag from his cigar and blows the smoke directly over Austria's pristine desk."

    show bismarck at left
    hide prussia

    ovb "A pleasure to meet you, Your Imperial Highness."
    
    show austria frustrated

    a "Excuse me, who is this brute? And put that cigar out immediately! Only the presiding power is allowed to smoke in chambers!"

    ovb "Is that so? How fascinating." 

    "Bismarck takes another leisurely puff, grinning."

    ovb "I look forward to our... debates."

    "Austria looks absolutely appalled. You turn and leave the hall, a dark, satisfied smirk playing on your lips."
    "You may have lost the diplomatic battle, but you are going to make her life an absolute living hell."

    jump turn_start

label diplo_1851_zollverein_expansion:

    scene bg prussia office
    with fade

    "After the political humiliation at the Federal Diet, you realized something important."
    "Austria might control the titles of the Confederation, but you control the industry and rail lines."
    "It's time to weaponize the economy."

    show hanover frustrated at left
    show prussia smug at right

    hr "I cannot believe I am doing this. Me! Forced to share a unified tariff zone with... new money."

    show hanover sad

    hr "When Great Britain was still paying my allowance, I would have never subjected myself to this kind of vulgar commercialism."

    p "The British cut you off over a decade ago, Hanover." 
    p "Your treasury is empty, your roads are dirt, and your toll booths are choking your own merchants."
    
    show prussia joyful

    p "Sign the paper. Let the us bring you into the modern age."

    show hanover frustrated

    hr "Fine. But I am signing it with my least favorite pen, just so you know I disapprove."

    "Hanover aggressively signs the treaty, bringing the critical northern territories into your economic sphere."

    show hanover normal

    "Suddenly, the double doors to the boardroom are violently thrown open."

    play sound "sfx/door_slam.ogg"
    with hpunch

    show austria frustrated at center
    hide hanover
    with moveinleft

    a "Stop right there! What is the meaning of this?!"

    show prussia smug

    p "Oh, Austria. Did you get lost looking for an opera house? This is a boardroom. We only deal in things that actually matter here."

    a "Don't take that tone with me! I am the President of the Confederation!"
    a "And as President, I demand that the Austrian Empire be fully integrated into this... this 'Zollverein' immediately!"

    show saxony embarrassed at left
    show bavaria normal at left_side_sprite

    "Saxony and Bavaria peek their heads into the room behind Austria, looking incredibly uncomfortable."

    s "She, uh... she found out we were making a lot of money without her."

    b "I told her we were just going to a beer-tasting festival, but she saw the shipping manifests..."

    show prussia normal

    p "You want to join the Customs Union, Austria? Truly?"

    show austria intense

    a "Yes! It is completely unacceptable for a German economic zone to exist without its political leader at the helm! I will take my rightful place at the head of this table!"

    p "Very well."

    "You snap your fingers. Bismarck steps out from the shadows of the corner office, holding a ridiculously tall stack of financial ledgers."

    show bismarck at right

    ovb "Good afternoon, Your Imperial Highness. We have anticipated your interest."

    ovb "To join the Zollverein, you simply need to agree to zero internal tariffs. Free trade across all borders."

    show austria smug

    a "Obviously. And I assume I will collect the majority of the transit dues?"

    show prussia joyful

    p "Oh, absolutely. But there's a catch. If you drop your tariffs, my Krupp steel, my Silesian coal, and my mechanized textiles will instantly flood the Bohemian and Viennese markets."

    show prussia intense

    p "Your industries are entirely protected by heavy import taxes. They are outdated, inefficient, and slow."
    p "If you join my free trade zone, my factories will bankrupt your entire domestic industry within six months."

    show austria sad

    "Austria freezes. The color completely drains from her face as Bismarck hands her a spreadsheet projecting the absolute destruction of the Austrian economy."

    a "You... you structured the entire economic union to be completely incompatible with my empire."

    show prussia smug

    p "I have absolutely no idea what you mean. We simply demand peak efficiency."

    p "If you can't keep up with the pace of Prussian industry, that's hardly my fault, is it?"

    show austria frustrated
    with vpunch

    a "This is a targeted attack! You are trying to isolate me! You're trying to make them dependent on you!"

    "Austria points an accusing finger at Bavaria and Saxony."

    a "Don't listen to her! Her money is dirty!"
    
    a"She doesn't even have a decent waltz!" with vpunch

    show bavaria embarrassed

    b "I mean... yes, but... she's offering us standardized railway gauges and extremely lucrative coal subsidies..."

    show saxony sad

    s "I'm sorry, Austria. The arts are wonderful, but I really need the infrastructure funding."

    show austria intense

    a "You are all traitors to the old order! I won't forget this, Prussia! I still hold the political power!"

    "Austria turns on her heel and storms out of the room, slamming the door behind her."

    ovb "Well. That went exactly as calculated."

    show prussia joyful

    p "By the time we're finished, the rest of Germany won't be able to buy a single loaf of bread without routing the payment through Berlin!"

    "The economic noose is tightening."

    jump turn_start