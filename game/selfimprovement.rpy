define p = Character("Prussia")

# 1849
label self_1849_telegraph:
    scene bg prussia office
    show prussia normal at right
    show siemens at left

    p "Hello, Herr von Siemens."

    siemens "It is a pleasure to meet you."

    p "I take it you'd like to sell me on the new electric telegraph. But we already have our semaphore system! How will this be any better?"

    siemens "Well! There's a number of benefits. Firstly these are way faster than the traditional system; the signals travel in an instant."

    siemens "Secondly, these can work day, night, rain or shine. It's not dependent on weather conditions."

    siemens "Lastly, you need a large staff of highly trained operators to run the semaphore towers. These just need an operator and someone to receive the messages."

    p "What about the cost? It seems it would be pretty costly to lay all those wires."

    siemens "Well, given the benefits it gives, I'd say it pays for itself over time. Civilians can also use it which would be a boon for all sorts of civilian sectors."

    show prussia joyful
     
    p "Seems convincing enough! I'll go ahead and refer this matter to the King so he can sign off on it."

    siemens "It's a deal!"

    jump turn_start 

label self_1849_landtag:
    scene bg landtag outside
    
    "With the dismissal of the Constituent Assembly, the King was able to pass a new constitution into law last year in 1848."

    "That constitution provides for a new bicameral legislature consisting of a House of Lords and a House of Representatives."

    "Today is the first sitting of this new legislature!"

    show prussia joyful at right
    show fwiv at left 
    
    p "It sure makes me feel good to see the people's will in action!"

    fwiv "Haha... yeah... people's will... anyway, there will be some pleasantries that you will have to get through, and then you'll yield the floor to me to open the session in earnest."

    show prussia embarrassed 

    p "Wait, I have to do the pleasantries?! Aren't you the king!?"
    
    p "But what am I going to say? This happened on such short notice... I didn't even expect you to dismiss the first Parliament, and now you want me to open a new one?"
    
    fwiv "Don't let these commoners get you down!"

    fwiv "It's not as if they're going to be dealing with most matters anyway, they'll just be debating the Constitution and make some infinitesimally small changes."

    p "If you say so..."

    scene bg landtag

    show prussia embarassed at center

    p "Ah... hello everyone! Sorry, I'm more used to blood and gore and guts and stuff, public speaking's not exactly my strong suit..."

    show prussia joyful

    p "Anyway! It's great to see you all gathered here. Given what happened last year, we in the government recognize the need for reform over revolution, and..."

    "You see one of the deputies has already gotten a cigar out and is smoking it while chatting to his fellow deputy."

    show prussia frustrated with vpunch

    p "Damn it! Have some tact when I am speaking to you! I am Prussia!"

    "Some of the deputies chuckled upon seeing this foot stamping reprimand from you."
    
    "You decide to just swallow your pride and keep going."

    p "As I was saying, we in the government recognize that reform is preferable to revolution."
    
    p "Therefore, in order to ensure our institutions remain coopera- I mean strong and robust to deal with all issues,"

    show prussia intense

    p "...We present this legislature. Don't make me regret giving you a voice!"
    
    jump turn_start

label self_1850_constitution:
    scene bg prussia office

    "The political hangover from the unrest of 1848 remains, so to keep the liberals from rebelling again, you have been forced to do the unthinkable:"
    "Draft a permanent constitution."

    show prussia frustrated at right
    with vpunch

    p "Shucks... Gee gosh diddly darnit... Gee whiz..."

    "You stab your quill into the inkwell and glare menacingly at the massive legal document on your desk."

    show prussia sad

    p "I suppose it had to come eventually...."

    "Friedrich Wilhelm IV paces nervously by the window, looking equally as distressed."

    show fwiv at center

    show prussia intense

    fwiv "Do you think I want a piece of paper coming between me and my divine right to rule? It makes me physically ill."

    fwiv "But the treasury is strained, and we need the bourgeoisie to keep paying their taxes without throwing cobblestones at the royal guard."

    fwiv "There must be a loophole. I refuse to allow the mob to outvote us."

    "Suddenly a shadowy figure emerges from the corridor."

    "It's Otto von Manteuffel, Minister of the Interior."

    show manteuffel at left

    manteuffel "That, Your Highness, is why we don't let the mob outvote us. We just have to rewrite the math!"

    show prussia normal

    p "...Go on."

    manteuffel "If we must have a democracy to appease the liberals, we shall give them one." 
    
    manteuffel "Universal male suffrage. Everyone gets a vote."

    show prussia frustrated

    p "Are you insane?! They'll dismantle the army!"

    fwiv "The peasants and factory workers outnumber the Junkers a hundred to one!"

    manteuffel "Patience! Everyone gets a vote... but not all votes are created equal."
    
    "von Manteuffel drops a heavy ledger onto the desk, tapping it with his pipe."

    manteuffel "We divide the voters into three classes based entirely on the taxes they pay."

    manteuffel "The wealthiest citizens who pay the first third of all taxes get to elect one-third of the parliament."

    manteuffel "The middle class, paying the next third, elects another third."

    manteuffel "The remainder? They elect the final third."
    
    "You blink, processing the sheer bureaucratic audacity of the plan."

    show prussia normal

    p "Wait... so the industrialists and Junkers..."

    manteuffel "Comprise roughly five percent of the population, yet completely control two-thirds of the legislative power!"

    manteuffel "It is mathematically impossible for the liberals or the poor to ever pass a law we do not like."

    fwiv "By God, it's brilliant! It looks like a concession, but it's actually an iron cage!"

    show prussia joyful
    with hpunch

    p "Oh, I love it!"

    p "They get their voting booths and election campaigns, and I get to keep my military untouched!"

    show prussia smug

    p "Pass the quill, I suddenly feel very... democratic."

    "You sign the Revised Constitution of 1850 with a massive, sweeping flourish."

    "Prussia has officially become a constitutional monarchy, but the absolute power of the crown and the military remains firmly intact."

    jump turn_start

label self_1850_police:

    scene bg prussia office
    with fade

    "The new constitution may have legally granted freedom of the press, but that doesn't mean you actually have to tolerate it."

    show prussia frustrated at right
    with vpunch

    p "If I have to read one more liberal editorial complaining about the military budget, I am going to personally feed a printing press into a Krupp blast furnace!"

    "You aggressively slam a crumpled newspaper onto your desk."

    p "Look at this! They are calling my standing army 'an unnecessary provocation'! Do they want the French to just waltz into the Rhineland?!"

    "A man steps out from the shadows of your office. His footsteps are completely silent. This is Wilhelm Stieber, your newly appointed Director of Police."

    show prussia normal at center
    with move
    show stieber at left
    with moveinleft

    stieber "Violence against the press only creates martyrs. The mob loves a martyr."

    show prussia intense

    p "Then what do you suggest, Herr Stieber? Should I just let them poison the minds of my conscripts with their democratic drivel?"

    stieber "Not at all. I propose we do not break the printing presses. I propose we own them."

    stieber "We establish a 'Central Press Bureau.' On paper, a simple government information office."

    show prussia normal

    p "Go on..."

    stieber "We monitor every single publication in the kingdom. We offer lucrative state subsidies to the editors who praise the army."
    
    stieber "For those who refuse, we don't arrest them." 
    stieber "We simply audit their finances. We intercept their mail. We lean on their landlords."

    show prussia joyful

    p "Ohoho... we suffocate them in red tape and whisper campaigns."

    stieber "Precisely." 

    stieber "Furthermore, my agents will plant our own articles in foreign newspapers, then have our domestic papers report on those foreign articles as 'international consensus'."
    
    stieber "We will create a reality where opposing the state is not just illegal, but socially unthinkable."

    show prussia smug

    p "Fighting war with blackmail and paranoia! I like it."

    p "The all-seeing eye of the eagle."

    show prussia intense
    with vpunch

    p "Do it, Stieber."

    "Stieber bows deeply, a chilling smile on his face, and melts back into the shadows."
    
    "The Central Press Bureau is officially established." 
    
    "Within months, opposition newspapers mysteriously go bankrupt or change their editorial stance overnight." 
    jump turn_start

label self_1851_banking:
    scene bg prussia office
    with fade

    show prussia frustrated at center
    with vpunch

    p "Unacceptable! What do you mean the Royal Bank is denying the loan for the new Silesian rail corridor?!"

    "You slam a heavily stamped ledger onto your desk, glaring at the treasury officials who are currently cowering near the door."

    p "I need those tracks laid before winter! How am I supposed to project overwhelming military dominance if my logistics network is being throttled by a bunch of conservative bean-counters?!"

    "The officials scatter as a sharply dressed, incredibly composed man walks into the room. It's David Hansemann, a prominent merchant and former liberal politician from the 1848 revolutions."

    show prussia intense at right
    with moveinleft
    show hansemann at left_side_sprite
    with moveinleft

    p "...Weren't you one of those liberals yelling at me about democracy a few years ago?"

    hansemann "I was, Your Highness. I quickly realized though that yelling in parliaments doesn't actually build anything, capital does that."

    hansemann "The state banks are too timid and are terrified of risk." 

    hansemann "Furthermore, your aristocratic financiers only lend what they can personally afford to lose. Their capital is static and tied up in landed estates."
    
    hansemann "To industrialize at the speed at which you want, you need a new type of financial institution."

    show prussia normal

    p "A new type of financial institution, you say?"

    hansemann "I propose a new kind of financial institution, a joint-stock bank.."
    
    hansemann "We pool the wealth of private investors bypassing the bureaucratic bottlenecks of the state treasury, and funnel massive lines of credit directly into heavy industry."

    hansemann "By distributing the risk across a massive base, we unlock an unprecedented amount of capital!"

    hansemann "It will be called the {i}Disconto-Gesellschaft{/i}."

    show prussia frustrated

    p "Stockbrokers? Speculators? The British do that, and their markets crash all the time."

    hansemann "It is private money, yes. But it will be directed exactly where you want it to go."

    hansemann "We are not the British, English banks strictly separate short-term commercial deposits from long-term industrial investment." 
    
    hansemann "It is inefficient!"

    hansemann "The {i}Disconto-Gesellschaft{/i} will pioneer the 'Universal Banking' model. We take in the deposits of the bourgeoisie, and we directly underwrite the massive and long-term bonds that are required for heavy industry."

    hansemann "It's not like we're to just hand Krupp or Borsig the money and hope for the best. We take equity in their companies, we sit on their boards of directors."



    show prussia joyful
    with hpunch

    "Your eyes widen. The realization hits you like a perfectly aimed artillery shell."

    p "Ah! So you're just bypassing the state treasury entirely!"

    hansemann "Precisely. The Austrians can have their feudalism. We will buy the future."

    show prussia smug

    p "Hansemann, you might just be my favorite capitalist."

    p "Draft the charter. I will have the King sign it by sundown!"

    "You eagerly sign the royal charter, establishing the Disconto-Gesellschaft."

    jump turn_start

label self_1853_jade_bight:

    scene bg prussia office
    with fade

    "You are aggressively stabbing a compass into a massive map of northern Europe, glaring at the coastlines."

    show prussia frustrated at right
    with vpunch

    p "It's a puddle! The Baltic Sea is nothing but a glorified puddle!"

    show prussia sad

    p "How am I supposed to project power when my entire fleet is trapped behind the Danish straits?!" 

    p "Every time I try to sail out, Copenhagen gets to stare at me, and Britain threatens a blockade!"

    p "I need deep water! I need the North Sea!"

    "The heavy oak door opens, and Prince Adalbert, the Admiral of the Prussian Navy, casually strolls in. He is holding a sealed leather dossier."

    show adalbert normal at left
    with moveinleft

    adalbert "Complaining about the geography again? Really, you should try solving your problems with diplomacy instead of a compass."

    show prussia normal

    p "Adalbert. Tell me you brought me a solution..."

    show adalbert smug

    adalbert "Better! I brought you a deed."

    "Adalbert tosses the dossier onto the map, landing right over the western German coastline."

    adalbert "I just returned from a very quiet, very expensive meeting with the Grand Duke of Oldenburg." 

    adalbert "For the price of 500,000 Thalers, he has officially signed the Jade Treaty. He has ceded us a stretch of coastline on the Jade Bight."

    show prussia joyful
    with hpunch

    p "The Jade Bight?! On the North Sea?! Direct access to the ocean, bypassing the Danes entirely?!"

    show prussia smug

    p "Adalbert, you magnificent visionary! I'm going to build a naval base so massive it's gonna make the British admiralty choke on their tea!"

    show prussia joyful
    
    p "I want drydocks! I want coastal batteries! I want an armada of steam-powered frigates!"

    show adalbert normal

    adalbert "...Before you order the ironclads, you should know exactly what we just purchased."

    adalbert "It is not a port, Your Highness." 

    adalbert "It is a desolate and malaria-infested tidal mudflat. There are no roads, no towns, and it floods regularly."

    adalbert "Taming that swamp and building a deep-water harbor from scratch will cost us millions and will cost the lives of thousands of workers to disease and exposure."

    show prussia intense

    "You pause for a moment, looking down at the map. The sheer logistical nightmare of the task would deter any normal state."

    "But you are not a normal state."

    show prussia smug

    p "Draft the engineering regiments. Send them to the Jade. Tell them they are not building a harbor..."

    show prussia intense
    with vpunch

    p "...they are building the future of the Prussian Navy! And I do not care how much blood and gold it costs to lay the foundations!"

    adalbert "I will inform the treasury to open the war chest. Happy building, Your Highness."

    "The Jade Treaty is ratified. The grueling and massively expensive construction of what will eventually become the great naval city of Wilhelmshaven begins." 
    
    "Prussia may finally have a foothold on the high seas."

    jump turn_start

label self_1855_ruhr_mining:

    scene bg mine
    with fade
    play sound "sfx/factory.ogg" loop
    play music "sfx/factory2.ogg"

    show prussia joyful at center

    p "Look at it. The absolute destruction of nature for the sake of state power. It's beautiful."

    "David Hansemann steps up beside you, having to raise his voice over the roar of the machinery."

    show prussia normal at left
    show hansemann at right
    with moveinright

    hansemann "Welcome to the future of the German economy, Your Highness. We call it 'Tiefbau'—deep-shaft mining."

    show prussia intense

    p "I know what a coal mine is, Hansemann. But the Ruhr has been mining coal for decades. Why do you need three action points worth of state subsidies for this one?"

    hansemann "Because, until now, we were only scratching the surface. We could only mine the shallow seams before hitting the groundwater table and flooding the tunnels."

    hansemann "But thanks to the capital from the Disconto-Gesellschaft, we've installed massive, industrial steam pumps." 
    hansemann "We aren't just scratching the surface anymore, rather we are draining the subterranean lakes."

    "Hansemann points down into the abyss past the headstock tower."

    hansemann "We are digging hundreds of meters straight down, beneath the marl layer. Down there is a virtually infinite ocean of high-grade coking coal."

    show prussia normal

    p "The exact type of fuel Krupp needs to run his new blast furnaces."

    hansemann "Exactly! The coal feeds the blast furnaces. The furnaces forge the steel. The steel builds the railways and the artillery. The railways transport the coal."

    hansemann "It is a perfect, self-sustaining loop of heavy industrial dominance. We just need the state to underwrite the initial drilling costs."

    show prussia smug
    with hpunch

    p "While Austria is busy harvesting wheat and arguing about beet tariffs, we are going to hollow out the underworld and burn it!"

    show prussia intense

    p "Hansemann, take the subsidies. Take whatever you need! I want the Ruhr Valley transformed into the largest industrial complex on the continent!"

    p "I want so much coal coming out of the ground that the sky turns black from Dortmund to Düsseldorf!"

    stop sound fadeout 2.0
    stop music fadeout 2.0
    
    "You sign the massive subsidy package. The deep-shaft mines of the Ruhr explode into productivity, fundamentally altering the economic balance of power in Europe."

    "Prussia will no longer just be an army with a state, but also a leading industrial titan."

    jump turn_start

# Add this to your character definitions at the top of the file
define wilhelm = Character("Prince Regent Wilhelm")

label self_1858_new_era:
    scene black with fade
    centered "{b}{size=40}The New Era{/size}{/b}\nOctober 1858 - Sanssouci Palace, Potsdam" with dissolve
    pause 1.0

    scene bg sanssouci chamber
    with fade

    "The grand bedroom is quiet, save for the ticking of a grandfather clock and the shallow breathing from the royal bed."
    "King Friedrich Wilhelm IV, the romantic, and the man who rejected the crown from the gutter, has suffered a series of severe strokes." 
    "His mind is gone."

    show prussia sad at center

    p "It's too quiet..."

    p "He spent his entire reign writing poetry, sketching cathedrals, and dreading the modern age. Now... he can't even speak."

    "You look down at your hands. You do not have the luxury of grieving for long. A state without a mind is a state waiting to be conquered."

    "Heavy and disciplined footsteps echo in the hallway. The doors open."

    show prussia normal at right
    with moveinleft
    show regentwilly at left_side_sprite
    with moveinleft

    "It is the King's younger brother, Wilhelm."

    regentwilly "The doctors have confirmed it, he will not recover. The Regency is officially mine."

    show prussia normal

    p "So. The 'romantic on the throne' steps down, and the 'Cartridge Prince' steps up."

    show prussia smug

    p "I remember how you handled the barricades in 1848, Wilhelm. I likewise remember how you commanded my artillery in Baden. You're a soldier."

    regentwilly "I am. And as a soldier, I look at our kingdom and I see a state of absolute strategic paralysis."

    regentwilly "My brother surrounded himself with reactionary sycophants." 
    
    regentwilly "The Diet hates the crown, the liberals are constantly agitated, and our diplomatic standing is stagnant."

    regentwilly "I have dismissed the conservative cabinet. I am bringing in moderates. The newspapers are already calling it the 'New Era'."

    show prussia frustrated
    with vpunch

    p "Moderates?! You're making concessions to the liberals?! Are you out of your mind?!"

    p "We just spent an entire decade building a massive police state and a rigged electoral system to keep them out of power!"

    "Wilhelm smiles. It is not a warm smile."

    regentwilly "Let them have their 'New Era'. Let them sing in the streets and praise my name in their newspapers. Let the threat of revolution fade."

    regentwilly "While they are busy cheering for my 'moderate' politics, I am going to ask them to approve the largest military expansion in European history."

    show prussia normal

    p "...Whuh?"

    show wilhelm normal

    wilhelm "Our population has doubled since 1815, yet the annual conscription quota hasn't changed. We are leaving tens of thousands of able-bodied men in the civilian sector."

    wilhelm "I intend to double the size of the standing army. I intend to create entirely new regiments, fully equipped with Krupp steel. I intend to turn the entire male population into a highly trained reserve force."

    show prussia joyful
    with hpunch

    "Your heart practically skips a beat. You stare at him, completely awestruck."

    p "You... you're using a liberal honeymoon period to build the ultimate military machine?"

    show prussia smug

    p "Mwehehehe..."

    "With Wilhelm at the helm, the romantic indecision of the past decade vanishes. The Prussian government will now operate with efficiency."

    "The liberals put down their pitchforks, completely unaware that they are about to fund their own worst nightmare."

    jump turn_start

label self_1860_army_reform:
    scene black with fade
    centered "{b}{size=40}The Death of the Citizen Soldier{/size}{/b}\nFebruary 1860 - The Ministry of War, Berlin" with dissolve
    pause 1.0

    scene bg prussia office
    with fade

    "The honeymoon period of the 'New Era' is officially over. The time for smiling at liberals has passed."
    "You are standing over a massive war table in your office, surrounded by demographic charts and military ledgers. You are not happy."

    show prussia frustrated at center
    with vpunch

    p "It's unacceptable! It is a complete numerical disgrace!"

    p "Our population has grown from 10 million in 1820 to nearly 18 million today! Yet our annual conscription intake is still capped at 40,000 men!"

    show prussia intense

    p "We are leaving an entire generation of able-bodied men sitting in factories and wheat fields when they should be learning how to march! If Marianne decides to cross the Rhine tomorrow, she will outnumber us two-to-one!"

    "The heavy oak doors of your office swing open. Prince Regent Wilhelm strides in, wearing his immaculate general's uniform."
    "Beside him is a man with a face like carved granite and eyes devoid of any warmth or compromise. This is Albrecht von Roon, your new Minister of War."

    show prussia normal at left
    show wilhelm normal at center
    show roon normal at right
    with moveinright

    wilhelm "You are preaching to the choir, Prussia. The army is stagnant. But Herr von Roon has brought the solution."

    "Roon steps forward, dropping a terrifyingly thick, leather-bound legislative bill onto your war table."

    roon "Good morning, Your Highness. I have completed the draft for the reorganization of the army."

    show prussia smug

    p "Let me see that. I hope you're asking for at least ten new regiments."

    show roon smug

    roon "I am asking for thirty-nine new infantry regiments and ten new cavalry regiments. We are raising the annual intake from 40,000 to 63,000 men."

    show prussia joyful
    with hpunch

    p "Thirty-nine?! Oh, Roon, you are speaking directly to my soul! The artillery? The logistics?"

    show roon normal

    roon "Fully modernized. But the sheer numbers are only the first pillar of the reform. The second pillar is discipline."
    
    roon "Currently, conscripts serve two years of active duty. This bill extends mandatory active service to three full years."

    show prussia normal

    "You pause, flipping through the pages. You know exactly what a three-year service term means politically."

    p "Three years? Roon, the liberals in the Landtag will have an absolute aneurysm. They already think the army is too expensive."

    show roon intense

    roon "Let them choke on it. Two years is enough time to teach a boy how to load a rifle and march in a straight line. But it is not enough time to break him."

    roon "In three years, we don't just train a soldier. We strip away his civilian identity entirely. We insulate him in the barracks. We teach him unconditional, blind obedience to the Crown, so that if he is ever ordered to fire upon a revolutionary mob, he will not hesitate."

    show wilhelm intense

    wilhelm "The army must be a pillar of the monarchy, immune to the democratic poison of the parliaments. Three years is non-negotiable."

    show prussia smug

    p "I love the ruthless efficiency, truly. But there's a third pillar in this bill, isn't there?"

    "You tap a specific section of the document, your eyes narrowing."

    p "You're gutting the Landwehr."

    show roon normal

    roon "The civilian militia is a romantic relic of 1813. They are weekend warriors commanded by middle-class merchants and university professors who think they have a right to debate strategy."
    
    roon "They are militarily useless and politically dangerous. This bill sidelines the Landwehr entirely and places the defense of the nation exclusively in the hands of the professional, aristocratic officer corps."

    show prussia intense

    p "You do realize what this is, right? This isn't just a military reform bill."

    p "You are asking the liberal-dominated parliament to pass a bill that permanently destroys their favorite democratic institution, raises taxes to astronomical levels, and hands absolute, unchecked power to the conservative Junkers."

    show wilhelm normal

    wilhelm "I am the sovereign. I command the armed forces. It is their constitutional duty to approve the budget."

    show prussia frustrated

    p "They hold the purse strings, Wilhelm! They will never approve the funding for this! They will veto the budget and paralyze the entire state!"

    show roon intense

    roon "Then we will force it through. The military survival of Prussia supersedes the opinions of tax-collecting bureaucrats. Are you with us, or are you afraid of a few angry delegates?"

    "You look at the bill. It is the blueprint for the most devastating military machine in European history. If passed, it will make you an unstoppable juggernaut. But it will also trigger a constitutional crisis that could tear the state apart."

    "You look back up at Roon and Wilhelm. A slow, terrifying grin spreads across your face."

    show prussia joyful
    with vpunch

    p "Afraid? I am the Iron Kingdom. I don't do 'afraid.'"

    show prussia smug

    p "Submit the bill to the Landtag. Let the delegates scream. We are going to forge this blade, even if we have to break the constitution to do it."

    scene bg landtag

    "The Roon Army Reform Bill is officially presented to the parliament. As predicted, the liberal delegates erupt in absolute, unmitigated outrage. The battle lines are drawn."










# Standard

label self_study:
    scene bg prussia study
    
    "You spend the evening by the fireplace, reading a leather-bound copy of Machiavelli's 'The Prince'."
    
    show prussia smug at center
    
    p "Ah, Machiavelli... The only one who truly understood power."

    p "'It is better to be feared than loved.'"

    p "Obviously. Love is fickle, amirite."
    
    p "Honestly, why even choose?"

    p "If you terrify them enough, they'll eventually convince themselves it's love anyway."

    show prussia serious
    
    p "Though frankly, his advice is a bit outdated."

    p "Nowadays a powerful state relies on a conscripted standing army, not mercenaries."

    show prussia joyful

    p "Still... his chapter on the absolute destruction of rival republics will serve me well."
    
    "You close the book and feel sharper than ever."
    
    jump turn_start

label self_drill:
    scene bg parade ground
    
    "You spend the afternoon on the muddy parade grounds, personally overseeing the infantry maneuvers."
    
    show prussia intense with vpunch
    
    p "Shoulders back! Rifles steady! I want to hear those boots hit the dirt like drumbeats!"
    
    show prussia joyful
    
    p "Ah... Is there anything more cleansing for the soul?"

    p "'Prussia is not a country with an army but an army with a country.' Well, I am enjoying the arrangement..."
    
    "The troops look exhausted, but their discipline is flawless."
    
    jump turn_start

label self_krupp:
    scene bg factory
    
    "You travel to Essen to meet with Alfred Krupp and inspect his latest metallurgical prototypes."
    
    show prussia normal
    
    p "Herr Krupp. Please tell me you have something that can shatter an Austrian fortress from two miles away."
    
    "Krupp silently rolls out the blueprints for a new massive, breech-loading cast steel cannon."
    
    show prussia joyful with vpunch
    
    p "Oh... it's beautiful!" 
    
    p "Look at the caliber of that barrel!"
    
    show prussia joyful with vpunch
    
    p "Take my money!! Take all of it!!!!"
    
    "You authorize another massive state subsidy for the Krupp armaments factories."
    
    jump turn_start

label self_rail:
    scene bg train station
    
    "You spend the day aggressively auditing the timetables of the new Prussian state railways."
    
    show prussia intense
    
    p "These schedules are completely unacceptable. Why are we prioritizing civilian passenger comfort over heavy freight?"
    
    show prussia frustrated with vpunch
    
    p "Every mile of track is an artery. They're not for weekend vacations!"
    
    show prussia intense
    
    p "I want these lines optimized to haul Krupp steel and Ruhr coal by day, and entire infantry corps by night."
    
    show prussia smug
    
    p "Our economy and our army are going to ride the exact same rails. Make sure the trains run on time."
    
    "You optimize the logistics network, accelerating both industrial growth and military mobilization."
    
    jump turn_start
