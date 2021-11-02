
INFO = {
    "address": "",
    "name": "Wayne Rooney",
}

TRAITS = {
    "base": {
        "Standard": 64,
        "Old": 23,
        "Young": 13,
    },
    "head": {
        None: 54,
        "BA Snapback": 14,
        "Wooly Hat": 13,
        "Winner Hat": 12,
        "Title Crown": 6,
        "Crown": 1,
    },
    "face": {
        None: 68,
        "Sweat": 20,
        "England Paint": 10,
        "Ad Beard": 2,
    },
    "mouth": {
        None: 72,
        "Gold Mouthguard": 12,
        "Medal": 11,
        "Diamond Grill": 4.75,
        "Dosbrak Bandana": 0.25,
    },
    "eye": {
        None: 62,
        "Wayfarers": 18,
        "Bloody Eye": 13,
        "Laser Eyes": 7,
    },
    "accessories": {
        None: 15,
        "Captain Armband": 15,
        "Yellow Ball": 14,
        "Pigskin Ball": 12,
        "Yellow Card": 11,
        "Medals": 10,
        "Confetti": 8,
        "League Trophy": 7,
        "European Trophy": 4.5,
        "Boot Award": 2.5,
        "Diamond Ball": 1,
    },
    "clothes": {
        "White Jersey": 20,
        "Red Jersey": 19,
        "Blue Jersey": 14,
        "Suit": 12,
        "Training Hoodie": 11,
        "Black Jersey": 10,
        "Managers Jacket": 6,
        "Patriot Flag": 5,
        "Red Jersey Torn": 2,
        "Astronaut": 1,
    },
    "Background": {
        "Green": 20,
        "Black": 20,
        "Red": 20,
        "Orange": 15,
        "Blue": 15,
        "Blockasset": 5,
        "Team": 4.2,
        "Stadium": 0.8,
    },
    "Signature": {
        "Signature": 100,
    },
}

def conditions(traits):

    if traits['base'] == 'Young' and traits['clothes'] == 'Astronaut':
        traits['clothes'] = 'Red Jersey Torn'

    if traits['base'] == 'Old' and traits['face'] == 'England Paint':
        traits['face'] = None

    if traits['face'] == 'England Paint':
        traits['accessories'] = None

    if traits['clothes'] == 'Astronaut' and traits['accessories'] == 'Captain Armband':
        traits['accessories'] = None

    if traits['accessories'] == 'League Trophy':
        traits['clothes'] = 'Red Jersey'

    if traits['face'] == 'England Paint':
        traits['clothes'] = None

    return traits
