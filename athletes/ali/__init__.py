INFO = {
    "address": "ali-wallet-address",
    "name": "Muhammad Ali",
}

TRAITS = {
    "Base": {
        "The Greatest": 64,
        "Butterflies and Bees": 23,
        "Underwater": 13,
    },
    "Head": {
        None: 54,
        "Hat": 14,
        "Sparring Headgear": 13,
        "Crown The GOAT": 12,
        "Halo": 6,
        "Crown": 1,
    },
    "Face": {
        None: 68,
        "Sweat": 20,
        "Scratch": 10,
        "Moustache": 2,
    },
    "Mouth": {
        None: 72,
        "GOAT Mouthguard": 12,
        "Medal": 11,
        "Locked": 4.75,
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
        "Red Gloves": 15,
        "Black Gloves": 14,
        "Towel": 12,
        "Speed Ball": 11,
        "Shook Up The World": 10,
        "Postage Stamp": 8,
        "Mirror": 7,
        "Microphones": 4.5,
        "Lightbulbs & Wings": 2.5,
        "Diamond Gloves": 1,
    },
    "Clothing": {
        None: 20,
        "Navy Suit": 19,
        "Gown": 14,
        "Black Suit": 12,
        "Peach Suit": 11,
        "Purple Suit": 10,
        "Elvis Gown": 6,
        "Gold Suit": 5,
        "The King's Gown": 2,
        "Astronaut": 1,
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
    },
}


def conditions(traits):

    # IF Sweat THEN no No clothing trait
    if traits["Face"] == "Sweat":
        traits["Clothing"] = None

    # IF Butterflies & Bees THEN no Shook Up The World
    # IF Butterflies & Bees THEN no Microphones
    # IF Butterflies & Bees THEN no Lightbulbs & Wings
    # IF Butterflies & Bees THEN no Mirror
    # IF Butterflies & Bees THEN no The King's Gown
    if traits["Base"] == "Butterflies & Bees":
        if traits["Accessory"] in [
            "Shook Up The World",
            "Microphones",
            "Lightbulbs & Wings",
            "Mirror",
        ]:
            traits["Accessory"] = None
        if traits["Clothing"] == "The King's Gown":
            traits["Clothing"] = None

    # IF Sparring Headgear THEN no Shook Up The World
    # IF Sparring Headgear THEN no Wayfarers
    if traits["Head"] == "Sparring Headgear":
        if traits["Accessory"] == "Shook Up The World":
            traits["Accessory"] = None
        if traits["Eyes"] == "Wayfarers":
            traits["Eyes"] = None

    # IF Dosbrak Bandana THEN no Mirror
    # IF Locked THEN no Mirror
    # IF Wayfarers THEN no Mirror
    if (
        traits["Mouth"] in ["Dosbrak Bandana", "Locked"]
        or traits["Eyes"] == "Wayfarers"
    ):
        if traits["Accessory"] == "Mirror":
            traits["Accessory"] = None

    # IF Astronaut THEN no Lightbulbs & Wings
    if (
        traits["Clothing"] == "Astronaut"
        and traits["Accessory"] == "Lightbulbs & Wings"
    ):
        traits["Accessory"] = None

    # IF The King's Gown THEN no Lightbulbs & Wings
    if (
        traits["Clothing"] == "The King's Gown"
        and traits["Accessory"] == "Lightbulbs & Wings"
    ):
        traits["Accessory"] = None

    # IF Underwater THEN no No Cabin, Gold, Orange, Red backgrounds
    if traits["Base"] == "Underwater" and traits["Background"] in [
        "Cabin",
        "Gold",
        "Orange",
        "Red",
    ]:
        traits["Background"] = "Solana"

    return traits
