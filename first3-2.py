#!/usr/bin/python3

guests = ["tom", "lily", "bob"]
print("I want to invite " + guests[0].title() + ", " + guests[1].title() + " and " + guests[2].title()
      + " to have dinner together")

print(guests[0].title() + " can't take apart in the party ")

guests[0] = "alice"
print("I want to invite " + guests[0].title() + ", " + guests[1].title() + " and " + guests[2].title()
      + " to have dinner together")
