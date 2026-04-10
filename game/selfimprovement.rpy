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
    

    jump turn_start


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
    
    jump turn_hub

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
    
    jump turn_hub

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
    
    jump turn_hub
