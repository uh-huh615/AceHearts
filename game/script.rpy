# Declare characters used by this game.
define a = Character('Alex', color="#28cd71")

#Define other variables here

# The game starts here.
label start:

    # Start by playing some music.
    play music "illurock.opus"

    scene bg lecturehall
    with fade

    "I wake up slowly, before jolting forward in my bed."

    a "My alarm didn't go off! Oh no, i'm going to be late to sch---"

    a "Wait, no, it's summer vacation. Phew, thought I was going to be in a lot of trouble"

    "It's a question that I've been meaning to ask a certain someone."

    menu:

        "As I realize this, I decide to..."

        "Go back to sleep, might as well sleep in, it's summer!":

            jump sleep

        "Stay up, i'm up any way, may be able to do something useful.":

            jump wake


label sleep:

label wake:
