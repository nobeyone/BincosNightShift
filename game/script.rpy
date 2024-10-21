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
    show customer_talking
    "..."

    menu:

        "How can I help you?":
            jump Herefor

        "Seen anything interesting lately?":
            jump Floor

label Floor:
    show customer_confused
    c "Yea, actually. Over in the soda area I heard something under the floor."
    return

label Herefor:
    show customer_confused
    c "Looking for a soda. Haven't had a good one in a while."
    return

label Good:
    show customer_talking
    c "Okay, Dracula. Good evening to you too. Haha."

    return

label Yo:
    show customer_talking
    c "this is what the customer would say in response to 'yo'"

    return
