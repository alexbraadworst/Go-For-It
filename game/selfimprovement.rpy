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

    "Some of the deputies chuckled upon seeing this foot stamping reprimand from you. You decide to just keep going."

    p "As I was saying, we in the government recognize that reform is preferable to revolution."
    
    p "Therefore, in order to ensure our institutions remain coopera- I mean strong and robust to deal with all issues,"

    p ""



label self_study:
    p "Woa i need to study"
    jump turn_start

