INFO = {
    "address": "rooney-wallet-address",
    "name": "Wayne Rooney",
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
        "Wooly Hat": 13,
        "Winner Hat": 12,
        "Title Crown": 6,
        "Crown": 1,
    },
    "Face": {
        None: 64,
        "Sweat": 24,
        "England Paint": 10,
        "Ad Beard": 2,
    },
    "Mouth": {
        None: 72,
        "Gold Mouthguard": 12,
        "Medal": 11,
        "Diamond Grill": 4.75,
        "Dosbrak Bandana": 0.25,
    },
    "Eyes": {
        None: 62,
        "Wayfarers": 18,
        "Bloody Eye": 13,
        "Laser Eyes": 7,
    },
    "Accessory": {
        None: 15,
        "Captain Armband": 15,
        "Pigskin Ball": 14,
        "Yellow Card": 12,
        "Red Card": 11,
        "Confetti": 10,
        "Fire Ball": 8,
        "League Trophy": 7,
        "European Trophy": 4.5,
        "Boot Award": 2.5,
        "Diamond Ball": 1,
    },
    "Clothing": {
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
        "Dosbrak": 100,
    },
}


def conditions(traits):

    # IF Young THEN no Astronaut
    if traits["Base"] == "Young" and traits["Clothing"] == "Astronaut":
        traits["Clothing"] = "Red Jersey Torn"

    # IF Old Base THEN no No England Paint
    if traits["Base"] == "Old" and traits["Face"] == "England Paint":
        traits["Face"] = None

    # IF England Paint THEN no No accessory
    if traits["Face"] == "England Paint":
        traits["Accessory"] = None

    # IF Astronaut THEN no Captain Armband
    # IF Patriot Flag THEN no Captain Armband
    if traits["Clothing"] in ["Patriot Flag", "Astronaut"] and traits["Accessory"] == "Captain Armband":
        traits["Accessory"] = None

    # IF League Trophy THEN no White Jersey, Blue Jersey, Suit, Training Hoodie, Black Jersey, Patriot Flag, Managers Jacket, Astronaut
    if traits["Accessory"] == "League Trophy":
        traits["Clothing"] = "Red Jersey Torn"

    # IF England Paint THEN no Clothing
    if traits["Face"] == "England Paint":
        traits["Clothing"] = None

    # IF Wooly Hat THEN no Blue Jersey, Black Jersey, White Jersey
    if traits["Head"] == "Wooly Hat":
        traits["Clothing"] = "Red Jersey"

    # IF Captain Armband THEN no Suit
    # IF Captain Armband THEN no Training Hoodie
    # IF Captain Armband THEN no Managers Jacket
    # IF Captain Armband THEN no Astronaut
    if traits["Accessory"] == "Captain Armband":
        traits["Clothing"] = "Black Jersey"

    # IF Managers Jacket THEN no League Trophy
    # IF White Jersey THEN no League Trophy
    # IF Blue Jersey THEN no League Trophy
    # IF Patriot Flag THEN no League Trophy
    # IF Black Jersey THEN no League Trophy
    # IF Managers Jacket THEN no European Trophy
    # IF White Jersey THEN no European Trophy
    # IF Blue Jersey THEN no European Trophy
    # IF Patriot Flag THEN no European Trophy
    # IF Black Jersey THEN no European Trophy
    if traits["Clothing"] in ["Managers", "White Jersey", "Blue Jersey", "Patriot Flag", "Black Jersey"]:
        if traits["Accessory"] in ["League Trophy", "European Trophy"]:
            traits["Accessory"] = "Fire Ball"

    # IF England paint THEN no Clothing trait
    # IF Winner Hat THEN no Blue Jersey
    # IF Winner Hat THEN no White Jersey
    if traits["Head"] == "Winner Hat" and traits["Clothing"] in ["Blue Jersey", "White Jersey"]:
        traits["Clothing"] = "Red Jersey"

    # IF Bloody Eye THEN no League Trophy
    if traits["Eyes"] == "Bloody Eye" and traits["Accessory"] == "League Trophy":
        traits["Accessory"] = None

    return traits
