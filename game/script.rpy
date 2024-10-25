# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Customer")

image customer_not_talking = "customer_not_talking.png"
image customer_confused = "customer_confused.png"
image customer_talking = "customer_mouth_open.png" 




# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bincoinside

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "customer1.png" to the images
    # directory.

    show customer_not_talking

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



label Herefor:
    show customer_confused
    c "Looking for a soda. Haven't had a good soda in a long time. Is there a soda machine?"
    menu:

        "Here's one on me.":
            jump Heres_A_Soda

    
label Heres_A_Soda:
    show customer_not_talking
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
    c "this is what the customer would say in response to 'yo'"

    return