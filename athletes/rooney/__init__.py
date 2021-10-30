
TRAITS = {
    "BASE": {
        "Standard": 80,
        "Old": 15,
        "Young": 5,
    },
    "HEAD": {
        None: 54,
        "BA Snapback": 14,
        "Wooly Hat": 13,
        "Winner Hat": 12,
        "Title Crown": 6,
        "Crown": 1,
    },
    "FACE": {
        None: 68,
        "Sweat": 20,
        "England Paint": 10,
        "Ad Beard": 2,
    },
    "MOUTH": {
        None: 72,
        "Gold Mouthguard": 12,
        "Medal": 11,
        "Diamond Grill": 4.75,
        "Dosbrak Bandana": 0.25,
    },
    "EYE": {
        None: 62,
        "Wayfarers": 18,
        "Bloody Eye": 13,
        "Laser Eyes": 7,
    },
    "ACCESSORIES": {
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
    "CLOTHES": {
        "White Jersey": 20,
        "Red Jersey": 19,
        "Blue Jersey": 14,
        "Suit": 12,
        "Training Hoodie": 11,
        "Black Jersey": 10,
        "Managers Jacket": 6,
        "Flag": 5,
        "Red Jersey Torn": 2,
        "Astronaut": 1,
    },
    "BACKGROUNDS": {
        "Green": 20,
        "Black": 20,
        "Red": 20,
        "Orange": 15,
        "Blue": 15,
        "Blockasset": 5,
        "Team": 4.2,
        "Stadium": 0.8,
    },
}

def conditions(nft_traits):

    if nft_traits['BASE'] == 'Young' and nft_traits['CLOTHING'] == 'Astronaut':
        nft_traits['CLOTHING'] = 'Red Jersey Torn'

    if nft_traits['BASE'] == 'Old' and nft_traits['FACE'] == 'England Paint':
        nft_traits['FACE'] = None

    return nft_traits
