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

label self_study:
    p "Woa i need to study"
    jump turn_start

