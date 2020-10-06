import random
from adjectives import adjectives
from nouns import nouns
def username_gen():
  describerandom = random.randint(0,len(adjectives))
  nounrandom = random.randint(0, len(nouns))
  adjective_index = adjectives[describerandom]
  noun_index = nouns[nounrandom]
  randint = random.randint(1,1000)
  username = str(adjective_index) + '_' + str(noun_index) + str(randint) 
  print(username)

username_gen()
