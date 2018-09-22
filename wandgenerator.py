import random

opening = ('Now here we have',
           'I\'m not sure, but consider this,',
           'Perhaps this,',
           'Maybe you\'d like this,',
           'This is',
           'I can recommend this,',
           'Why don\'t you take a look at this,')


wood = ('Elder',
        'Cedar',
        'Hazel',
        'Holly',
        'Oak',
        'Willow',
        'Ash',
        'Hawthorn',
        'Mahogany',
        'Birch')

core = ('Unicorn tail hair',
        'Dragon heartstring (Hungarian Horntail)',
        'Phoenix tail feather',
        'Phoenix stomach feather',
        'Unicorn mane hair',
        'Dragon heartstring (Swedish Snort-snout)',
        'Phoenix wing feather',
        'Unicorn hair (from body, not tail or mane)',
        'Dragon heartstring (Norwegain Ridgeback)',
        'Phoenix feather (from chest)')

strength = ('Bendy',
            'Whippy',
            'Stiff',
            'Flexible',
            'Sturdy',
            'Light',
            'Firm',
            'Fairly Heavy',
            'Very flexible',
            'Heavy')

bestfor = ('Transfiguration',
           'Dark Arts',
           'Charms',
           'Inventing new spells',
           'Potions',
           'Healing spells',
           'Defense Against The Dark Arts',
           'Offensive spells',
           'Defensive/Protective spells',
           'Apperation')

length = ('12 3/4 inches',
          '10 1/2 inches',
          '12 inches',
          '14 inches',
          '10 inches',
          '13 inches',
          '9 inches',
          '9 1/2 inches',
          '11 1/4 inches',
          '8 inches')

appearance = ('Black with \'cracked\' markings',
              'Reddish with lighter and intricate handle',
              'Brown with knobby handle',
              'Dark brown with ivy carved into it',
              'Tan with unicorn horn-like handle',
              'Very light brown with intricate flame-like markings',
              'Different shades of brown from handle to tip',
              'Jet black with bark-like markings',
              'Dark brown with very small and light spider web pattern',
              'Mahogany with fairly smooth and bark-like markings')


def aoran(word):
    if word[:1].lower() in ('a', 'e', 'i', 'o', 'u'):
        return 'an ' + word
    else:
        return 'a ' + word


print("{} {} wand, {} with a core of {}, {}, {}. Best for {}".format(random.choice(opening),
                                                                     aoran(random.choice(
                                                                         wood)),
                                                                     random.choice(
    length),
    random.choice(
    core),
    random.choice(
    strength).lower(),
    random.choice(
    appearance).lower(),
    random.choice(bestfor)))
