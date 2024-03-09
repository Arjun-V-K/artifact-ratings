import re
# Util functions

# type StatKey
#   = "hp" //HP
#   | "hp_" //HP%
#   | "atk" //ATK
#   | "atk_" //ATK%
#   | "def" //DEF
#   | "def_" //DEF%
#   | "eleMas" //Elemental Mastery
#   | "enerRech_" //Energy Recharge
#   | "heal_" //Healing Bonus
#   | "critRate_" //CRIT Rate
#   | "critDMG_" //CRIT DMG
#   | "physical_dmg_" //Physical DMG Bonus
#   | "anemo_dmg_" //Anemo DMG Bonus
#   | "geo_dmg_" //Geo DMG Bonus
#   | "electro_dmg_" //Electro DMG Bonus
#   | "hydro_dmg_" //Hydro DMG Bonus
#   | "pyro_dmg_" //Pyro DMG Bonus
#   | "cryo_dmg_" //Cryo DMG Bonus
#   | "dendro_dmg_" //Dendro DMG Bonus

def format_artifact_substat_text(substat):
    key = substat.key
    value = substat.value

    if key == "hp":
        return f"HP+{value}"
    if key == "hp_":
        return f"HP+{value}%"
    if key == "atk":
        return f"ATK+{value}"
    if key == "atk_":
        return f"ATK+{value}%"
    if key == "def":
        return f"DEF+{value}"
    if key == "def_":
        return f"DEF+{value}%"
    if key == "eleMas":
        return f"Elemental Mastery+{value}"
    if key == "enerRech_":
        return f"Energy Recharge+{value}%"
    if key == "critRate_":
        return f"CRIT Rate+{value}%"
    if key == "critDMG_":
        return f"CRIT DMG+{value}%"

def reverse_pascal_case(pascal_case_str):
    words = re.findall(r'[A-Z][a-z0-9]*', pascal_case_str)
    original_name = ' '.join(words)
    return original_name

def format_artifact_set_key(camel_case_key):
    artifact_set_key_mapping = {
        "Adventurer": "Adventurer",
        "ArchaicPetra": "Archaic Petra",
        "Berserker": "Berserker",
        "BlizzardStrayer": "Blizzard Strayer",
        "BloodstainedChivalry": "Bloodstained Chivalry",
        "BraveHeart": "Brave Heart",
        "CrimsonWitchOfFlames": "Crimson Witch of Flames",
        "DeepwoodMemories": "Deepwood Memories",
        "DefendersWill": "Defender's Will",
        "DesertPavilionChronicle": "Desert Pavilion Chronicle",
        "EchoesOfAnOffering": "Echoes of an Offering",
        "EmblemOfSeveredFate": "Emblem of Severed Fate",
        "FlowerOfParadiseLost": "Flower of Paradise Lost",
        "Gambler": "Gambler",
        "GildedDreams": "Gilded Dreams",
        "GladiatorsFinale": "Gladiator's Finale",
        "GoldenTroupe": "Golden Troupe",
        "HeartOfDepth": "Heart of Depth",
        "HuskOfOpulentDreams": "Husk of Opulent Dreams",
        "Instructor": "Instructor",
        "Lavawalker": "Lavawalker",
        "LuckyDog": "Lucky Dog",
        "MaidenBeloved": "Maiden Beloved",
        "MarechausseeHunter": "Marechaussee Hunter",
        "MartialArtist": "Martial Artist",
        "NighttimeWhispersInTheEchoingWoods": "Nighttime Whispers in the Echoing Woods",
        "NoblesseOblige": "Noblesse Oblige",
        "NymphsDream": "Nymph's Dream",
        "OceanHuedClam": "Ocean-Hued Clam",
        "PaleFlame": "Pale Flame",
        "PrayersForDestiny": "Prayers for Destiny",
        "PrayersForIllumination": "Prayers for Illumination",
        "PrayersForWisdom": "Prayers for Wisdom",
        "PrayersToSpringtime": "Prayers to Springtime",
        "ResolutionOfSojourner": "Resolution of Sojourner",
        "RetracingBolide": "Retracing Bolide",
        "Scholar": "Scholar",
        "ShimenawasReminiscence": "Shimenawa's Reminiscence",
        "SongOfDaysPast": "Song of Days Past",
        "TenacityOfTheMillelith": "Tenacity of the Millelith",
        "TheExile": "The Exile",
        "ThunderingFury": "Thundering Fury",
        "Thundersoother": "Thundersoother",
        "TinyMiracle": "Tiny Miracle",
        "TravelingDoctor": "Traveling Doctor",
        "VermillionHereafter": "Vermillion Hereafter",
        "ViridescentVenerer": "Viridescent Venerer",
        "VourukashasGlow": "Vourukasha's Glow",
        "WanderersTroupe": "Wanderer's Troupe"
    }

    original_key = artifact_set_key_mapping.get(camel_case_key)
    return original_key if original_key else reverse_pascal_case(camel_case_key)
