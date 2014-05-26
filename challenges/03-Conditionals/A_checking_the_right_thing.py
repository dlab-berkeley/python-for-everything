# As (hopefully) discussed in class, people are very bad at conditional
# reasoning! But computers are great at it, as long as you write the rules
# properly.

## Let's set up some ages...

sally_age = 12
john_age = 32

# Can these folks drink? Write a conditional for each one and assign a variable
# XXX_can_drink for sally and john

## We'll start out safe and assume no one can drink until we check!

sally_can_drink = False
john_can_drink = False

## Now replace False with the "correct" condition
## Note - we're again playing it safe - False is never "True", so we'll never
## say sally_can_drink!

if False: # conditionals take True or False
    sally_can_drink = True

## And again, please take care of john!

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
