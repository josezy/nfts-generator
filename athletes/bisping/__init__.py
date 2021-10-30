
TRAITS = {
    "BASE": {
        "Standard": 80,
        "Bald": 15,
        "Old Mike": 5,
    },
    "HEAD": {
        None: 54,
        "Sparring Headgear": 14,
        "Snapback": 13,
        "Announcer": 12,
        "DJ Mikey B": 6,
        "Crown": 1,
    },
    "FACE": {
        None: 68,
        "Bloody": 20,
        "Red Terminator": 10,
        "Gold Terminator": 2,
    },
    "MOUTH": {
        None: 72,
        "Cigar": 12,
        "Falling Mouthguard": 11,
        "Diamond Grill": 4.75,
        "Dosbrak Bandana": 0.25,
    },
    "EYES": {
        None: 62,
        "Wayfarers": 18,
        "Bruised Eye": 13,
        "Laser Eyes": 7,
    },
    "ACCESSORIES": {
        None: 15,
        "Bare Fists": 15,
        "Gloves": 14,
        "Bloody Wraps": 12,
        "Bloody Gloves": 11,
        "Microphone": 10,
        "SOL Gloves": 8,
        "Gold Gloves": 7,
        "199 Belt": 4.5,
        "Knuckle Duster Spikes": 2.5,
        "Diamond Gloves": 1,
    },
    "CLOTHING": {
        None: 20,
        "Bloody Body": 19,
        "Jiu Jitsu Robe": 14,
        "Suit": 12,
        "Tattoo": 11,
        "Punk Jacket": 10,
        "Butcher": 6,
        "Patriot Flag": 5,
        "The Count": 2,
        "Astronaut": 1,
    },
    "BACKGROUND": {
        "Teal": 20,
        "Black": 20,
        "Red": 20,
        "Purple": 15,
        "Mustard": 15,
        "Blockasset": 5,
        "Octagon": 4.2,
        "Count's Lair": 0.8,
    },
}

def conditions(nft_traits):

    if nft_traits['CLOTHING'] == 'Butcher':
        nft_traits['ACCESSORIES'] = None
        nft_traits['HEAD'] = None
        if nft_traits['MOUTH'] == 'Dosbrak Bandana':
            nft_traits['MOUTH'] = 'Diamond Grill'

    if nft_traits['BASE'] == 'Bald' and nft_traits['CLOTHING'] == 'Astronaut':
        nft_traits['CLOTHING'] = 'The Count'

    return nft_traits
