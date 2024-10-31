# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Customer")
define f = Character(_("Floorboard Guy"), color="#c8c8ff")
define w = Character(_("Wizard"), color="#c8c8ff")
define r = Character("Restful Cube")
define co = Character("Cop")
image customer_not_talking = "customer_not_talking.png"
image customer_confused = "customer_confused.png"
image customer_talking = "customer_mouth_open.png" 




# The game starts here.

label start:

   

    scene bg bincoinside

    show restful_cube
    r "Hey man, thanks for working here at Binco's. I'm heading out so you're going to be working alone tonight man."



    show customer_not_talking
    with dissolve
    # These display lines of dialogue.

    c "Hey."
    


    menu:

        "Hi! Welcome to Binco's":
            jump Hi

        "Good evening.":
            jump Good

        "Yo.":
            jump Yo

label Hi:
    show customer_talking
    c "Hey there."
    jump Hi2

label Hi2:
    menu:

        "How can I help you?":
            jump Herefor

        "Seen anything interesting lately?":
            jump Floor

label Floor:
    show customer_confused
    c "Yea, actually. Over in the soda area I heard something under the floor."
    jump UnderFloor
    return

label UnderFloor:
    show customer_not_talking
    menu:
        
        "Oh, god. Was it a digging sound? Like somebody digging with a shovel?":
            jump Digging

        "That was probably nothing. Why don't we go take a look, though.":
            jump Digging

label Digging:
    scene floorguy_appears
    with dissolve
    
    show floorboardguy_not_talking
    with dissolve

label Herefor:
    show customer_confused
    c "Looking for a soda. Haven't had a good soda in a long time. Is there a soda machine?"
    menu:

        "Here's one on me.":
            jump Heres_A_Soda

    
label Heres_A_Soda:
    show customer_drinking_soda
    

label Good:
    show customer_talking
    c "Oookay, Dracula. Good evening to you too. Haha."
    jump Good_2

label Good_2:
    show customer_not_talking
    menu:
        "I really am Dracula, by the way.":
            jump Is_Dracula

        "Not even joking, Dracula lives in a mansion like three minutes from here.":
            jump Isnt_Dracula

label Is_Dracula:
    show customer_talking
    c "Fuck off, haha."
    jump Is_Dracula2

label Is_Dracula2:
    show customer_not_talking
    menu:
        "I really am Dracula, by the way.":
            jump Is_Dracula

    

label Yo:
    show customer_talking
    c "That's funny, the greeter at the door just told me the same thing. 'Yo.'"
    "(But there isn't a greeter. This isn't walmart.)"
    menu: 
        "A greeter? We don't have greeters at Binco's.":
            c "Oh. Then I guess those potions he was talking about weren't Binco's brand."
            jump Inspect_Greeter
        "Oh no. Was he old, and did he look like a type of Gandalf?":
            c "Yea, now that you mention it. He sort of did."
            jump Inspect_Greeter
            

label Inspect_Greeter:
    scene wizard_appears
    with dissolve
    
    show wizard
    with dissolve
    
    show wizard_talking
    w "ohohohoooo helloooooo there fellow! What a pleasant evening, it's indeed quite mellow."
    menu: 
        
        "You can't be here, old man. I've been told you know that.":
            w "Oh you must be new here! Sit down, crack open a beer. I fear you must be mistaken, a problem I am NOT! Indeed, I'm a friend of this parking lot."
            menu: 

                "No, I'm pretty sure I can't let you be here. I'm gonna call the cops":
                    jump CallCops
                 
                "Okay, fine. What're you doing out here anyway?":
                    jump Chillin
                 
label CallCops:
        show cop_talking
        with dissolve
        co "Oh, look who's back. Gonna sell more 'pixie dust' to people?"
        w "Helloooo officer! I was wondering when you'd show up. No, this time I'm practically GIVING AWAY this homonculus in a cup."
        show homonculus
        co "I can smell your breath from here. You know the rules about public intoxication."
        w "It's my wizard mead! It's a cultural seed!"
        co "Yea, well you're gonna be spending the night in the drunk tank. Let's go."
        w "Shit, man..."
        co "Can we get you to come down to the station and take your statement?"
            menu: 

                "Yea, sure.":
                    jump Jailhouse

                
