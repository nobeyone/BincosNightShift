# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Customer")

define doug = Character("Doug")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bincoinside

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "customer1.png" to the images
    # directory.

    show customer not_talking

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
    show customer talking
    c "Hey there."
    jump Hi2

label Hi2:
    show customer not_talking
    "..."
    menu:

        "How can I help you?":
            jump Herefor

        "Seen anything interesting lately?":
            jump Floor

label Floor:
    show customer confused
    c "Yea, actually. Over in the soda area I heard something under the floor."
    return
