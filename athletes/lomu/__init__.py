INFO = {
    "address": "",
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
        None: 68,
        "Sweat": 20,
        "Bane": 10,
        "Terminator": 2,
    },
    "Mouth": {
        None: 72,
        "Solana Mouthguard": 12,
        "All Blacks Mouth Guard": 11,
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
    "signature": {
        "signature": 100,
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
