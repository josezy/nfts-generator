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
        "Crown GOAT": 12,
        "Halo": 6,
        "Crown": 1,
    },
    "Face": {
        None: 64,
        "Sweat": 24,
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
        "Side Eyes": 7,
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
    "Signature": {
        "Dosbrak": 100,
    },
}


def conditions(t):

    # IF Sweat THEN no No clothing trait
    if t["Face"] == "Sweat":
        t["Clothing"] = None

    # IF Butterflies & Bees THEN no Shook Up The World
    # IF Butterflies & Bees THEN no Microphones
    # IF Butterflies & Bees THEN no Lightbulbs & Wings
    # IF Butterflies & Bees THEN no Mirror
    # IF Butterflies & Bees THEN no The King's Gown
    if t["Base"] == "Butterflies & Bees":
        if t["Accessory"] in [
            "Shook Up The World",
            "Microphones",
            "Lightbulbs & Wings",
            "Mirror",
        ]:
            t["Accessory"] = None
        if t["Clothing"] == "The King's Gown":
            t["Clothing"] = None

    # IF Sparring Headgear THEN no Shook Up The World
    # IF Sparring Headgear THEN no Wayfarers
    if t["Head"] == "Sparring Headgear":
        if t["Accessory"] == "Shook Up The World":
            t["Accessory"] = None
        if t["Eyes"] == "Wayfarers":
            t["Eyes"] = None

    # IF Dosbrak Bandana THEN no Mirror
    # IF Locked THEN no Mirror
    # IF Wayfarers THEN no Mirror
    if (
        t["Mouth"] in ["Dosbrak Bandana", "Locked"]
        or t["Eyes"] == "Wayfarers"
    ):
        if t["Accessory"] == "Mirror":
            t["Accessory"] = None

    # IF Astronaut THEN no Lightbulbs & Wings
    if (
        t["Clothing"] == "Astronaut"
        and t["Accessory"] == "Lightbulbs & Wings"
    ):
        t["Accessory"] = None

    # IF The King's Gown THEN no Lightbulbs & Wings
    if (
        t["Clothing"] == "The King's Gown"
        and t["Accessory"] == "Lightbulbs & Wings"
    ):
        t["Accessory"] = None

    # IF Underwater THEN no No Cabin, Gold, Orange, Red backgrounds
    if t["Base"] == "Underwater" and t["Background"] in [
        "Cabin",
        "Gold",
        "Orange",
        "Red",
    ]:
        t["Background"] = "Solana"

    # IF Gown THEN no Towel
    if t["Clothing"] == "Gown" and t["Accessory"] == "Towel":
        t["Accessory"] = None

    # IF Sparring Headgear THEN no Mirror
    if t["Head"] == "Sparring Headgear" and t["Accessory"] == "Mirror":
        t["Accessory"] = None

    # IF Halo THEN no Postage Stamp
    if t["Head"] == "Halo" and t["Accessory"] == "Postage Stamp":
        t["Accessory"] = None

    # IF The King's Gown THEN no Towel
    if t["Clothing"] == "The King's Gown" and t["Accessory"] == "Towel":
        t["Accessory"] = None

    # IF Locked THEN no Sparring Headgear
    # IF Locked THEN no Postage Stamp
    # IF Locked THEN no Shook Up The World
    if t["Mouth"] == "Locked":
        if t["Head"] == "Sparring Headgear":
            t["Head"] = None
        if t["Accessory"] in ["Postage Stamp", "Shook Up The World"]:
            t["Accessory"] = None

    # IF Dosbrak Bandana THEN no Mirror
    if t["Mouth"] == "Dosbrak Bandana" and t["Accessory"] == "Mirror":
        t["Accessory"] = None

    # IF Towel THEN no Clothing
    if t["Accessory"] == "Towel":
        t["Clothing"] = None

    # IF Side Eyes THEN no Locked
    if t["Eyes"] == "Side Eyes" and t["Mouth"] == "Locked":
        t["Mouth"] = None

    return t
