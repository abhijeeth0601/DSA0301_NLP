import nltk
from nltk.stem import WordNetLemmatizer


def generate_plural_noun(noun):
    lemmatizer = WordNetLemmatizer()
    singular = lemmatizer.lemmatize(noun, 'n')
    if singular == noun:
        if noun == "aircraft" or noun == "eyeglasses" or noun == "mews" or noun == "sheep" or noun == "alms" or noun == "gallows" or noun == "monkfish" or noun == "shellfish" or noun == "barracks" or noun == "goldfish" or noun == "moose" or noun == "shorts" or noun == "binoculars" or noun == "grapefruit" or noun == "mullet" or noun == "shrimp" or noun == "bison" or noun == "greenfly" or noun == "offspring" or noun == "smithereens" or noun == "bourgeois" or noun == "grouse" or noun == "pants" or noun == "spacecraft" or noun == "breadfruit" or noun == "haddock" or noun == "passion" or noun == "fruit" or noun == "species" or noun == "cattle" or noun == "halibut" or noun == "patois" or noun == "squid" or noun == "chalk" or noun == "headquarters" or noun == "pliers" or noun == "staff" or noun == "chassis" or noun == "hovercraft" or noun == "police" or noun == "starfruit" or noun == "chinos" or noun == "ides" or noun == "précis" or noun == "swine" or noun == "cod" or noun == "insignia" or noun == "premises" or noun == "tongs" or noun == "corps" or noun == "jackfruit" or noun == "pyjamas" or noun == "trousers" or noun == "crossroads" or noun == "jeans" or noun == "reindeer" or noun == "trout" or noun == "deer" or noun == "kennels" or noun == "rendezvous" or noun == "tuna" or noun == "dice" or noun == "knickers" or noun == "salmon" or noun == "tweezer" or noun == "dungarees" or noun == "leggings" or noun == "scissors" or noun == "wheat" or noun == "elk" or noun == "means" or noun == "series" or noun == "you":
            plural = noun
        elif noun.endswith('y'):
            plural = noun[:-1] + 'ies'
        elif noun[-1] in ['s', 'x'] or noun[-2:] in ['sh', 'ch']:
            plural = noun + 'es'
        elif noun.endswith('f'):
            plural = noun[:-1] + 'ves'
        elif noun.endswith('fe'):
            plural = noun[:-2] + 'ves'
        else:
            plural = noun + 's'
    else:
        plural = noun
    return plural


nouns = ["cat", "sheep", "city", "baby", "leaf", "knife", "scissors", "pants"]
for noun in nouns:
    plural = generate_plural_noun(noun)
    print(f"{noun} (singular) -> {plural} (plural)")
