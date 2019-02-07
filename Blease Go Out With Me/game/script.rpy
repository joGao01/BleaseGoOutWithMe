#characters
define m = Character("MC", color="#052860")
define f = Character("Fish", color="#2c0889")
define n = Character("Narrator")
define a = Character("Alyssa")

#vars
define points = 0

#images
image street1 = "street.jpg"
image buffer = "buffer.jpg"
image running1 = im.FactorScale("running1.png", 0.5)
image running2 = im.FactorScale("running2.png", 0.5)
image crash = im.FactorScale("crash.jpg", 0.7)
image ground1 = "ground.jpg"
image fallen = im.FactorScale("fallen.png", 0.5)
image fallen2 = im.FactorScale("fallen2.png", 0.5)
image groundBg = "groundBg.jpg"
image groundwBread = im.FactorScale("groundwBread.png", 0.4)
image groundwoBread = im.FactorScale("groundwoBread.png", 0.4)
image groundBg2 = "groundBg.jpg"
image groundBgEnd = "groundBgEnd.jpg"
image cafe = im.FactorScale("cafe.jpg", 0.9)
image karaoke = im.FactorScale("karaoke.jpg", 1.2)
image cafeCounter = im.FactorScale("coffee-shop.jpg", 0.4)

image mcSprite = im.FactorScale("mc/sprite.png", 0.5)
image mcBlush = im.FactorScale("mc/blush.png", 0.5)
image mcShock = im.FactorScale("mc/shock.png", 0.5)
image mcWhy = im.FactorScale("mc/why.png", 0.5)
image fishDab = im.FactorScale("fish/dab.png", 0.7)
image fishSprite = im.FactorScale("fish/standing2.png", 0.7)
image fishBlush = im.FactorScale("fish/blush.png", 0.7)
image fishShock = im.FactorScale("fish/surprised.png", 0.7)

image alyssa = im.FactorScale("alyssa.png", 0.5)
image alyssaShock = im.FactorScale("alyssaShock.png", 0.5)

label start:
    scene black
    scene street1
    with moveinleft
    show running1
    with moveinright
    #insert character running
    m "*Record Scratch*"
    m "*Freeze frame*"
    m "Yup. That's me."
    m "And I'm currently running late for work."
    hide running1
    show running2
    with moveinright
    m "My boss is going to kill me."
    m "Or fire me. Depending on how he's feeling."

    scene crash at truecenter with vpunch
    pause 2

    #large crash scene
    scene ground1
    show fallen
    m "Huh?"
    m "Ah I ran into someone."
    m "Typical."
    m "..."
    hide fallen
    scene groundBg
    show groundwBread at top
    m "Oh."
    f "Are you okay?"
    scene ground1
    show fallen2
    m "{i}Oh my bejeezus, they're beautiful.{/i}"
    m "{i}Fabulous.{/i}"
    scene groundBg
#    show groundwoBread need some shoujo effect
    show mcWhy at right
    show fishShock at left
    m "Y-yea, I'm fine."
    f "I'm really sorry about that."
    m "No, it was my fault."

    m "..."
    scene groundBg
    show groundwoBread at top
    n "You really can't resist."

    m "Blease go out with me."
    pause 1
    #title screen?
    scene black
    n "Sometimes we say things that we don't mean to."
    n "It happens."
    n "But now it's up to you to decide what to do."
    n "The truth is, you wouldn't mind taking this irresponsibly attractive fish on a date."
    n "Actually, that would be kind of nice."

    scene groundBg2
    show fishShock at left
    show mcSprite at right

    f "Huh? A blind date? I'm down."

    menu:

        "Play it off as a joke.":
            hide mcSprite
            show mcWhy at right
            m "Ah I'm joking."
            m "Anyway, I'm off to work now."
            m "Bye."
            hide mcWhy with moveoutright
            #fade to black
            jump cowardice

        "Go through with it.":
            hide mcSprite
            show mcWhy at right
            m "{i}Damn, I really said that, didn't I?{/i}"
            m "{i}Well, too late to back out now.{/i}"
            hide mcWhy
            show mcSprite at right
            m "So how about it?"

        #ten minutes later.
    scene buffer
    pause 2
    scene street1
    hide fishShock
    show fishSprite at left
    show mcSprite at right

    f "Ok. See you on Saturday then."
    hide fishSprite with moveoutleft
    hide mcSprite with moveoutright
    scene black
    n "And so, you have scored a date with a stranger you ran into on the street."
    n "Congrats."

    #Black screen with the word Saturday
    show text "SATURDAY" at truecenter
    with dissolve
    pause 2
    hide text
    with dissolve

    scene street
    show running2
    m "ACK I'm running late again!"

    n "Deja vu, eh?"

    scene groundBg2

    n "When you arrive at the scene, Fish is already standing there."
    n "And they look just as great as the fateful day you met."
    show fishSprite at left with moveinleft
    show mcWhy at right with moveinright
    m "Did I keep you waiting long?"
    f "No, I just got here."
    hide mcWhy
    show mcSprite at right
    f "Have you decided where you want to go?"

    menu:

        # "Amusement Park":
        #     "I want to take you to the amusement park"
        #     $ points += 2
        #     jump amusement_park

        "Aquarium":
            m "Let's go to the aquarium"
            #no points lmao u dun fucked up
            jump aquarium

        "Cafe":
            m "I'm taking you to a cafe"
            $ points += 1
            jump cafe

    # label amusement_park:
    #     f "I love the amusement park."
    #     m "{i}Oh thank goodness. I used a random date location generator{/i}"
    #     m "I'm glad."
    #     f "What would you like to do first?"
    #
    #     menu:
    #         "Carousel":
    #             m "Mmm Let's ride the carousel"
    #         "Ferris Wheel":
    #             m ""
    #         "Arcade":
    #             m "Let's go to the arcade."

    label aquarium:
        hide fishSprite
        show fishShock at left
        f "An Aquarium? I hate aquariums."
        hide mcSprite
        show mcWhy at right
        n "Uh oh. Top ten anime betrayals"
        m "Well..I thought since you're a fish.."
        f "Why would I pay to go to a place where my brethren are kept in captivity?"
        m ".."
        m "Alright. Sorry. then where do you suggest we go?"
        hide mcWhy
        show mcSprite at right
        hide fishShock
        show fishSprite at left
        f "Well..."
        f "I've always wanted to do karaoke."

        menu:
            "You can sing?":
                hide mcSprite
                show mcShock at right
                $ points += 1
                m "You can sing?"
                f "Better than you would expect from a fish."
                f "My lungs are pretty strong."
                m "You have lungs?"
                f "Yea. They're in my legs."
                m "Oh. I see"
                f "Anyway, let's go."

            "Hm I'm not really good at singing":
                hide mcSprite
                show mcWhy at right
                #no points for being pessimistic
                f "That's what karaoke is about, is it not?"
                f "Listen, I can't sing that well either, but my lungs are more powerful than you would expect."
                m "Lungs?"
                f "Yea, I have lungs."
                m "I thought fish had gills."
                hide mcWhy
                show mcShock at right
                f "My lungs are in my legs."
                m "Oh.. I see."
                f "Let's go."

        scene black
        pause 0.5
        #change of scene: Karaoke place
        scene karaoke at top
        pause 1
        show fishSprite at left with moveinleft
        show mcSprite at right with moveinright
        f "What song do you want to sing first?"

        menu:
            "Despacito":
                n "You sing Despacito."
                n "The music has been omitted to avoid copyright and to protect your ears."
                f "I didn't want to say anything while you were singing, but I absolutely hate that song."
                m "Oh."
                $ points -= 1

            "Baby Shark":
                n "Against, your better judgement, you pick Baby Shark."
                n "Fish's eyes immediately light up."
                n "You sing Baby Shark."
                n "For the protection of your sanity, the audio has been omitted."
                n "By the time you're done, Fish's eyes are tearing up."
                f "That was beautiful."
                $ points += 2


            "Never gonna give you up":
                n "You smile as you pick this song."
                n "You sing it."
                n "Fish is mildly amused to have been rick-rolled by you."
                $ points += 1

        n "As the day winds down, you hope that Fish has forgiven you for the aquarium incident."
        jump last_decision


    label cafe:
        scene cafe
        show fishSprite at left with moveinleft
        show mcSprite at right with moveinright
        f "I'm not saying I hate coffee but.."
        f "It would not be my drink of choice."
        hide mcSprite
        show mcShock at right
        m "It's not just the coffee. The ambiance is very good."
        hide mcShock
        show mcSprite at right
        m "I often come here to do art or read."
        m "I know almost everyone who works here."
        f "It is really nice."
        f "..."
        #some generic death metal comes on
        n "Generic death metal plays over the speakers."
        f "But I'm not really sure about the choice of music."

        menu:
            "Nah, death metal really adds to the serenity of the cafe.":
                f "Ehh."

            "Hm I see what you mean. I like it, but I could ask them to change it.":
                #change music here
                $ points += 1
                f "Oh thanks."
        m "I'm going to go order drinks now."
        m "You can take a seat in one of the booths."
        m "I'll be back soon."

        #change scene
        scene cafeCounter
        show alyssa at left
        show mcSprite at right
        m "Hi, Alyssa!"
        a "How ya doing? On a date?"
        hide mcSprite
        show mcBlush at right
        #blushing mc
        m "Yea"
        n "Alyssa cranes her neck to take a look at your date."
        hide alyssa
        show alyssaShock at left
        a "Wow what a catch. How'd you manage to reel them in?"
        m "I ran into them on the street. It's a long story."
        hide alyssaShock
        show alyssa at left
        a "What would you like to drink?"

        menu:
            "2 Mocha fraps, please":
                $ points -= 1
                scene cafe
                n "You bring the drinks back to the table where Fish is sitting."
                show mcSprite at right with moveinright
                show fishSprite at left with moveinleft
                f "Mocha Fraps?"
                m "Yea."
                hide fishSprite
                show fishShock at left
                f "I'm allergic to chocolate..being a fish with legs and all."
                m "Oh..."
                hide fishShock with moveoutleft
                n "You drink your mocha frap in silence as Fish gets up to ask for another drink."
                jump last_decision

            "2 Matcha fraps, please":
                $ points += 2
                scene cafe
                n "You bring the drinks back to the table where Fish is sitting."
                show mcSprite at right with moveinright
                show fishBlush at left with moveinleft
                f "Oh! Matcha Fraps! The only drink worth drinking here."
                m "Yea, these fraps are almost as good as chimichangas."
                hide fishBlush
                show fishSprite at left
                f "Chimichangas?"
                n "The two of you lose yourselves in a conversation about coffee and chimichangas."
                jump last_decision

            "2 Vanilla Lattes, please":
                scene cafe
                n "You bring the drinks back to the table where Fish is sitting."
                show mcSprite at right with moveinright
                show fishSprite at left with moveinleft
                f "Vanilla Latte?"
                m "Yea, I hope you don't mind it too much."
                f "Yea. At least it doesn't have chocolate in it."
                m "Oh? What do you have against chocolate?"
                f "I'm sensitive. Chocolate clogs up my lungs."
                hide mcSprite
                show mcShock at right
                m "Lungs? You have lungs?"
                f "Yea, they're stored in my legs."
                n "The two of you drink and chat."
                jump last_decision


    label last_decision:
        scene groundBgEnd
        show mcSprite at right with moveinright
        show fishSprite at left with moveinleft
        m "Did you have fun today?"

        if points >= 3:
            hide fishSprite
            show fishBlush at left
            f "Yea. This was a nice change of pace from things."
            m "I'm glad. I had fun as well."
            f "We should do this again."
            m "{i}Oh my god{/i} Yes. Definitely."
        else:
            f "Hey.. I don't think it's going to work out with us."
            hide mcSprite
            show mcWhy at right
            m "...I'm sorry."

        scene groundBgEnd
        show mcSprite at right
        show fishSprite at left

        menu:
            "It's time to part ways."

            "Say goodbye.":
                m "well, thank you for today."
                m "Bye."
                if points >= 3:
                    f "Yea. See you again soon."
                    hide mcSprite
                    show mcBlush at right
                    n "Fish winks at you, and you die a little inside."
                else:
                    f "Bye. And good luck. There are plenty of other fish in the sea."
                $ points += 1

            "Ask for a kiss." if points >=3:
                hide mcSprite
                show mcBlush at right
                m "Hey. Before you go could I..."
                m "Have one kiss?"
                hide fishSprite
                show fishBlush at left
                n "Oh wow, you got Fish to blush."
                n "Impressive."
                f "Sure."
                n "You kiss."
                n "I bet you were expecting saucy kissing art here."
                n "Too bad the game dev had no time."
                m "Well, see you again."
                f "Soon hopefully?"
                m "Yea."
                $ points += 1

            "Hit 'em with a dab.":
                m "See you again soon!"
                m "{i}DABS{/i}"
                if points >= 3:
                    f "See you!"
                    scene black
                    show fishDab at top with hpunch
                    pause 1
                    f "{i}DABS BACK{/i}"
                    $ points += 2
                else:
                    f "What the hell are you doing?"
                    $ points -= 2


        scene black
        if points >= 4:
            n "You did well."
            n "You really got that Fish."
            n "Hook, line, and sinker."

        else:
            n "It seems like it didn't work out"
            n "Water you doing?"
            n "You don't deserve Fish's love."

        show text "The End" at truecenter
        with dissolve
        pause 2
        hide text
        with dissolve
        return

    label cowardice:
        #black screen
        scene black
        n "I say, from the very bottom of my heart,"
        n "that you're a coward"
        n "And nothing good ever comes to cowards."
        n "Grow a spleen, and when you're ready, come back and try again."
        show text "The End" at truecenter
        with dissolve
        pause 2
        hide text
        with dissolve
        return
