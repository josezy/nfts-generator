
INFO = {
    "address": "",
    "name": "Wayne Rooney",
}

TRAITS = {
    "base": {
        "Standard": 80,
        "Old": 15,
        "Young": 5,
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
    "Backgrounds": {
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

def conditions(nft_traits):

    if nft_traits['base'] == 'Young' and nft_traits['clothes'] == 'Astronaut':
        nft_traits['clothes'] = 'Red Jersey Torn'

    if nft_traits['base'] == 'Old' and nft_traits['face'] == 'England Paint':
        nft_traits['face'] = None

    if nft_traits['face'] == 'England Paint':
        nft_traits['accessories'] = None

    if nft_traits['clothes'] == 'Astronaut' and nft_traits['accessories'] == 'Captain Armband':
        nft_traits['accessories'] = None

    if nft_traits['accessories'] == 'League Trophy':
        nft_traits['clothes'] = 'Red Jersey'

    if nft_traits['face'] == 'England Paint':
        nft_traits['clothes'] = None

    return nft_traits
