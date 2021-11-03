INFO = {
    "address": "lomu-wallet-address",
    "name": "Jonah Lomu",
}

TRAITS = {
    "Base": {
        "Standard": 64,
        "Old": 23,
        "Young": 13,
    },
    "Head": {
        None: 54,
        "BA Snapback": 14,
        "Headband": 13,
        "Hat": 12,
        "Halo": 6,
        "Crown": 1,
    },
    "Face": {
        None: 64,
        "Haka": 24,
        "Sweat": 10,
        "Bane": 2,
    },
    "Mouth": {
        None: 72,
        "Solana Mouthguard": 12,
        "NZ Mouth Guard": 11,
        "Diamond Grill": 4.75,
        "Dosbrak Bandana": 0.25,
    },
    "Eyes": {
        None: 62,
        "Wayfarers": 18,
        "Eye Injury": 13,
        "Laser Eyes": 7,
    },
    "Accessory": {
        None: 15,
        "Ball": 15,
        "Old Ball": 14,
        "NZ Ball": 12,
        "Boots": 11,
        "Crown Ball": 10,
        "Egg Ball": 8,
        "Gold Chain": 7,
        "Fire Ball": 4.5,
        "Boom Box": 2.5,
        "Diamond Ball": 1,
    },
    "Clothing": {
        "NZ Jersey": 20,
        "Solana Jersey": 19,
        "NZ Away Jersey": 14,
        "CM Jersey": 12,
        "Blue Suit": 11,
        "Shirt": 10,
        "Yellow Jersey": 6,
        "NZ Old Jersey": 5,
        "Black Tie": 2,
        "Astronaut": 1,
    },
    "Background": {
        "Black": 20,
        "Orange": 20,
        "Red": 20,
        "Purple": 15,
        "Blue": 15,
        "Blockasset": 5,
        "Gold": 4.2,
        "New Zealand": 0.8,
    },
    "Signature": {
        "Dosbrak": 100,
    },
}


def conditions(traits):

    # IF Eye Injury THEN no Headband
    # IF Eye Injury THEN no BA Snapback
    # IF Eye Injury THEN no Hat
    if traits["Eyes"] == "Eye Injury":
        traits["Head"] = None

    # IF Astronaut THEN no Boots
    # IF Astronaut THEN no Boom Box
    if traits["Clothing"] == "Astronaut" and traits["Accessory"] in [
        "Boots",
        "Boom Box",
    ]:
        traits["Accessory"] = None

    # IF Blue Suit THEN no Boots
    if traits["Clothing"] == "Blue Suit" and traits["Accessory"] == "Boots":
        traits["Accessory"] = None

    # IF Bane THEN no Diamond Grill
    if traits["Face"] == "Bane" and traits["Mouth"] == "Diamond Grill":
        traits["Mouth"] = None

    # IF Haka THEN no Solana Mouthguard
    # IF Haka THEN no NZ Mouth Guard
    # IF Haka THEN no Diamond Grill
    if traits["Face"] == "Haka":
        traits["Mouth"] = None

    # IF Dosbrak Bandana THEN no Haka
    if traits["Mouth"] == "Dosbrak Bandana":
        traits["Face"] = None

    # IF Wayfarers THEN no Bane
    if traits["Eyes"] == "Wayfarers" and traits["Face"] == "Bane":
        traits["Face"] = None

    # IF Blue Suit THEN no Sweat
    # IF Black Tie THEN no Sweat
    # IF Astronaut THEN no Sweat
    if traits["Clothing"] in ["Blue Suit", "Black Tie", "Astronaut"] and traits["Face"] == "Sweat":
        traits["Face"] = None

    # IF Shirt THEN no Sweat
    if traits["Clothing"] == "Shirt" and traits["Face"] == "Sweat":
        traits["Face"] = None

    return traits
