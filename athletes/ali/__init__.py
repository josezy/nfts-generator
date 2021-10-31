TRAITS = {
    "Base": {
        "The Greatest": 64,
        "Butterflies & Bees": 23,
    },
    "Head": {
        None: 54,
        "Crown": 14,
        "Halo": 13,
        "Crown The GOAT": 12,
        "Sparring Headgear": 6,
        "Hat": 1,
    },
    "Face": {
        None: 68,
        "Sweat": 20,
        "Moustache": 10,
        "Scratch": 2,
    },
    "Mouth": {
        None: 72,
        "Dosbrak Bandana": 12,
        "Locked": 11,
        "Medal": 4.75,
        "GOAT Mouthguard": 0.25,
    },
    "Eyes": {
        None: 62,
        "Wayfarers": 18,
        "Laser Eyes copy": 13,
        "bruise eye ": 7,
    },
    "Accessory": {
        None: 15,
        "Shook Up The World": 15,
        "Mirror": 14,
        "Black Gloves": 12,
        "Red Gloves": 11,
        "Diamond Gloves": 10,
        "Postage Stamp": 8,
        "Speed Ball": 7,
        "Lightbulbs & Wings": 4.5,
        "Microphones": 2.5,
        "Towel": 1,
    },
    "Clothing": {
        None: 20,
        "Astronaut": 19,
        "The King's Gown": 14,
        "Gold Suit": 12,
        "Purple Suit": 11,
        "Peach Suit": 10,
        "Black Suit": 6,
        "Gown": 5,
        "Navy Suit": 2,
        "black shirt": 1,
    },
    "Background": {
        "Black": 20,
        "Orange": 20,
        "Red": 20,
        "Purple": 15,
        "Gold": 15,
        "Solana": 5,
        "USA": 4.2,
        "Cabin": 0.8,
    },
    "signature copy": {
        "signature copy": 100,
    }
}


def conditions(nft_traits):

    if nft_traits["Face"] == "Sweat":
        nft_traits["Clothing"] = None

    return nft_traits
