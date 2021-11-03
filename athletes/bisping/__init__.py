INFO = {
    "address": "6uDvPTDPgRaCBuSK5Jq531TugMEXJXm8APhzca3T2KuR",
    "name": "Michael Bisping",
}

TRAITS = {
    "Base": {
        "Standard": 64,
        "Bald": 23,
        "Old Mike": 13,
    },
    "Head": {
        None: 54,
        "Sparring Headgear": 14,
        "Snapback": 13,
        "Announcer": 12,
        "DJ Mikey B": 6,
        "Crown": 1,
    },
    "Face": {
        None: 64,
        "Bloody": 24,
        "Red Terminator": 10,
        "Gold Terminator": 2,
    },
    "Mouth": {
        None: 72,
        "Cigar": 12,
        "Falling Mouthguard": 11,
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
        "Bare Fists": 15,
        "Gloves": 14,
        "Bloody Wraps": 12,
        "Bloody Gloves": 11,
        "Microphone": 10,
        "SOL Gloves": 8,
        "Gold Gloves": 7,
        "199 Belt": 4.5,
        "Knuckle Duster Spikes": 2.5,
        "Diamond Gloves": 1,
    },
    "Clothing": {
        None: 20,
        "Bloody Body": 19,
        "Jiu Jitsu Robe": 14,
        "Suit": 12,
        "Tattoo": 11,
        "Punk Jacket": 10,
        "Butcher": 6,
        "Patriot Flag": 5,
        "The Count": 2,
        "Astronaut": 1,
    },
    "Background": {
        "Teal": 20,
        "Black": 20,
        "Red": 20,
        "Purple": 15,
        "Mustard": 15,
        "Blockasset": 5,
        "Octagon": 4.2,
        "Count's Lair": 0.8,
    },
    "Signature": {
        "Dosbrak": 100,
    },
}


def conditions(traits):

    # IF Butcher THEN no Accessories, DJ Mikey B, Announcer, Sparring Headgear, Dosbrak Bandana
    # IF Butcher THEN no Gold Terminator
    # IF Butcher THEN no Red Terminator
    # IF Butcher THEN no Wayfarers
    if traits["Clothing"] == "Butcher":
        traits["Accessory"] = None
        traits["Head"] = None
        traits["Face"] = None
        if traits["Mouth"] == "Dosbrak Bandana":
            traits["Mouth"] = "Diamond Grill"
        if traits["Eyes"] == "Wayfarers":
            traits["Eyes"] = None

    # IF Bald base THEN no No Astronaut
    if traits["Base"] == "Bald" and traits["Clothing"] == "Astronaut":
        traits["Clothing"] = "The Count"

    # IF Wayfarers THEN no Sparring Headgear, Announcer, DJ Mikey B
    if traits["Eyes"] == "Wayfarers":
        traits["Head"] = None

    # IF Sparring Headgear THEN no Bruised Eye
    if traits["Head"] == "Sparring Headgear" and traits["Eyes"] == "Bruised Eye":
        traits["Eyes"] = None

    # IF Bruised Eye THEN no Gold Terminator
    # IF Bruised Eye THEN no Red Terminator
    if traits["Eyes"] == "Bruised Eye":
        traits["Face"] = None

    # IF Sparring Headgear THEN no Bloody Body, Jiu Jitsu Robe, Tattoo, Butcher, Patriot Flag, Astronaut
    # IF Sparring Headgear THEN no Wayfarers
    # IF Sparring Headgear THEN no Microphone
    if traits["Head"] == "Sparring Headgear":
        traits["Clothing"] = None
        if traits["Eyes"] == "Wayfarers":
            traits["Eyes"] = None
        if traits["Accessory"] == "Microphone":
            traits["Accessory"] = None

    # IF No clothing trait THEN no Wayfarers
    if not traits["Clothing"] and traits["Eyes"] == "Wayfarers":
        traits["Eyes"] = None

    # IF Butcher THEN no Microphone
    # IF Announcer THEN no Microphone
    # IF Bald Mike THEN no Microphone
    # IF No clothing trait THEN no Microphone
    # IF Astronaut THEN no Microphone
    if (
        not traits["Clothing"]
        or traits["Clothing"] in ["Butcher", "Astronaut"]
        or traits["Head"] == "Announcer"
        or traits["Base"] == "Bald"
    ):
        if traits["Accessory"] == "Microphone":
            traits["Accessory"] = None

    # IF Patriot Flag THEN no Cigar
    if traits["Clothing"] == "Patriot Flag" and traits["Mouth"] == "Cigar":
        traits["Mouth"] = None

    # IF Announcer THEN no Cigar
    if traits["Head"] == "Announcer" and traits["Mouth"] == "Cigar":
        traits["Mouth"] = None

    # IF Astronaut THEN no DJ Mikey B
    if traits["Clothing"] == "Astronaut" and traits["Head"] == "DJ Mikey B":
        traits["Head"] = None

    # IF Bald Mike THEN no DJ Mikey B
    if traits["Base"] == "Bald" and traits["Head"] == "DJ Mikey B":
        traits["Head"] = None

    # IF Microphone THEN no Bloody Body, Jiu Jitsu Robe, Tattoo, Butcher, Patriot Flag, Astronaut
    if traits["Accessory"] == "Microphone" and traits["Clothing"] in ["Bloody Body", "Jiu Jitsu Robe", "Tattoo", "Butcher", "Patriot Flag", "Astronaut"]:
        traits["Clothing"] = "Suit"

    return traits
