# As discussed in class, people are very bad at conditional reasoning! But
# computers are great at it, as long as you write the rules properly.

## Now, we have a different scenario, we see some folks drinking. Here's the
## information about the scene before us:

alice_age = 20
alice_is_drinking = True
bob_age = 12
bob_is_drinking = False
charles_age = 22
charles_is_drinking = True

## Now, we only check the people who are drinking (and print a message that we
## are doing so). Then, we say "OK!" if they are 21+, or "This isn't right!" if
## they are under 21.

## Note that the tests for the below are very picky about the *exact* output,
## so don't change those strings!

if True: # Again - I'm play it safe and checking everyone, fix this!
    print "Checking Alice"
    if False: # Check her age
        print "OK!"
    else:
        print "This isn't right!"

## After you fix the above, do the same for Bob and Charles. Be sure to change
## the "Checking..." line, but keep everything else the same
