INFO = {
    "address": "ovechkin-wallet-address",
    "name": "Alexander Ovechkin",
}

TRAITS = {
    "Base": {
        "Standard": 64,
        "Old": 23,
        "Young": 13,
    },
    "Head": {
        None: 54,
        "BA Snapback ": 14,
        "Hockey Helmet black": 13,
        "Russian Hat": 12,
        "Hocky Helmet Gold": 6,
        "Crown": 1,
    },
    "Face": {
        None: 64,
        "Sweat": 24,
        "Bloody": 10,
        "Big Beard": 2,
    },
    "Mouth": {
        None: 72,
        "Jaws": 12,
        "Gold Teeth": 11,
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
        "Bloody Glove": 15,
        "Gold Glove": 14,
        "Ice Stick": 12,
        "Raining Pucks": 11,
        "Gold Stick": 10,
        "Fire Stick": 8,
        "Diamond Glove": 7,
        "Diamond Stick": 4.5,
        "Dentist": 2.5,
        "Raining Ice Pucks": 1,
    },
    "Clothing": {
        "Red Jersey": 20,
        "Black Jersey": 19,
        "White Jersey": 14,
        "Blue Jersey": 12,
        "Patriot": 11,
        "Solana Jersey": 10,
        "The Red Machine": 6,
        "Suit": 5,
        "Ice Ice Ovi": 2,
        "Astronaut": 1,
    },
    "Background": {
        "Green": 20,
        "Black": 20,
        "Red": 20,
        "Blue": 15,
        "Orange": 15,
        "Blockasset": 5,
        "Russia": 4.2,
        "Hockey": 0.8,
    },
    "Signature": {
        "Dosbrak": 100,
    },
}


def conditions(t):
    # IF Crown THEN no Russia
    if t["Head"] == "Crown" and t["Background"] == "Russia":
        t["Background"] = "Blockasset"

    # IF Gold Helmet THEN no Wayfarers
    # IF Red Helmet THEN no Wayfarers
    if t["Head"] in ["Gold Helmet", "Red Helmet"] and t["Eyes"] == "Wayfarers":
        t["Wayfarers"] = None

    # IF Ice Ice Ovi THEN no Frozen
    # Frozen trait does not exists

    return t
