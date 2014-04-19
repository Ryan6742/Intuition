from adventure import *
import adventure
import objects
import os

os.system('clear')

player = Player(objects.rm_start)

def main():
    init()
    while True:
        out = parse(player.input(), player)
        print
        print out
        print
        

def init():
    print """You wake up to find yourself lying on the floor of a dark cave. You're not entirely sure how you got here."""

    lying_down = True
    count = 0
    app = "."
    while lying_down:
        print
        first_cmd = player.input()
        print
        if first_cmd == "get up":
            if count > 0: app = ", finally."
            print "You stand up" + app
            lying_down = False
        elif "look" in first_cmd or "l" in first_cmd:
            print "With your back on the floor, you stare at the empty ceiling wondering what it all means."
        elif "wait" in first_cmd or "w" in first_cmd:
            print "You lie on the floor for a few minutes"
        else:
            print "It's hard to do anything while lying on the ground."
        count += 1
    print 
    print "You look around"
    print look_at(objects.rm_start)
    print

if __name__ == '__main__':
    main()