# making a basic group character dictionary
# keys are: name, race, class, level, ac, speed, passive perception

char_0_seth = {
    'name': "Jhaa'Tara",
    'race': 'dwarf',
    'class': 'fighter',
    'level': 7,
    'AC': 18,
    'speed': 30,
    'passive perception': 10,
}

char_0_kate = {
    'name': "Aegir",
    'race': 'water genasi',
    'class': 'barbarian',
    'level': 6,
    'AC': 17,
    'speed': 40,
    'passive perception': 15,
}

char_0_kate['HP'] = 84
char_0_seth['HP'] = 57

char_0_kirah = {}

char_0_kirah['name'] = 'Eryellah'
char_0_kirah['race'] = 'aasimar'
char_0_kirah['class'] = 'cleric'
char_0_kirah['level'] = 7
char_0_kirah['AC'] = 16
char_0_kirah['speed'] = 30
char_0_kirah['passive perception'] = 15
char_0_kirah['HP'] = 66

# To Hit Check and Damage Calculator

party = [char_0_kirah, char_0_kate, char_0_seth]

to_hit_check = "\nEnter the attack roll to hit below."
to_hit_check += '\n\tTo hit: '

does_it_hit = input(to_hit_check)
does_it_hit = int(does_it_hit)

for to_hit in party:
    if does_it_hit >= to_hit['AC']:
        print(f"\nThat's a hit on {to_hit['name']}! Roll for damage!")
        damage_check = "Enter Damage: "

        damage = input(damage_check)
        damage = int(damage)
        print(f"\n\t {to_hit['name'].upper()} takes {damage}! Their HP is now {to_hit['HP']-damage}!")
    else:
        print(f"\nYou missed {to_hit['name']}. Try again next round.")
