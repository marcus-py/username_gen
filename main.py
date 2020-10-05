import random
from adjectives import adjectives
from nouns import nouns
def username_gen():
  describerandom = random.randint(1,len(adjectives))
  thingrandom = random.randint(1, len(nouns))
  adjective_index = adjectives[describerandom]
  noun_index = nouns[thingrandom]
  randint = random.randint(1,1000)
  username = str(adjective_index) + '_' + str(noun_index) + str(randint) 
  print(username)

username_gen()
