# 1.
# B = probability that both children are girls
# G = probability that the older children is a girl
# This can be stated as: P(B|G) = P(B,G) / P(G)
# 2.
# B = probability that both children are girls
# L = probability that at least one children is a girl
# This can be stated as: P(B|L) = P(B,L) / P(L)
import enum, random
class Kid(enum.Enum):
    BOY = 0
    GIRL = 1
def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])
both_girls = 0
older_girl = 0
either_girl = 0
random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == Kid.GIRL:
        older_girl += 1
    if older == Kid.GIRL and younger == Kid.GIRL:
        both_girls += 1
    if older == Kid.GIRL or younger == Kid.GIRL:
        either_girl += 1
print("P(both | older):", both_girls / older_girl) 
print("P(both | either):", both_girls / either_girl)  