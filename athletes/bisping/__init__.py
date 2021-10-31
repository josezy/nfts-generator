
INFO = {
    "address": "6uDvPTDPgRaCBuSK5Jq531TugMEXJXm8APhzca3T2KuR",
    "name": "Michael Bisping",
}

TRAITS = {
    "Base": {
        "Standard": 64,
        "Bald": 23,
        "Old Mike": 13,
    },
    "Head": {
        None: 54,
        "Sparring Headgear": 14,
        "Snapback": 13,
        "Announcer": 12,
        "DJ Mikey B": 6,
        "Crown": 1,
    },
    "Face": {
        None: 68,
        "Bloody": 20,
        "Red Terminator": 10,
        "Gold Terminator": 2,
    },
    "Mouth": {
        None: 72,
        "Cigar": 12,
        "Falling Mouthguard": 11,
        "Diamond Grill": 4.75,
        "Dosbrak Bandana": 0.25,
    },
    "Eyes": {
        None: 62,
        "Wayfarers": 18,
        "Bruised Eye": 13,
        "Laser Eyes": 7,
    },
    "Accessory": {
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
    "Clothing": {
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
    "Background": {
        "Teal": 20,
        "Black": 20,
        "Red": 20,
        "Purple": 15,
        "Mustard": 15,
        "Blockasset": 5,
        "Octagon": 4.2,
        "Count's Lair": 0.8,
    },
    "Signature": {
        "Signature": 100,
    }
}

def conditions(nft_traits):

    if nft_traits['Clothing'] == 'Butcher':
        nft_traits['Accessory'] = None
        nft_traits['Head'] = None
        if nft_traits['Mouth'] == 'Dosbrak Bandana':
            nft_traits['Mouth'] = 'Diamond Grill'

    if nft_traits['Base'] == 'Bald' and nft_traits['Clothing'] == 'Astronaut':
        nft_traits['Clothing'] = 'The Count'

    if nft_traits['Eyes'] == 'Wayfarers':
        nft_traits['Head'] = None

    return nft_traits
