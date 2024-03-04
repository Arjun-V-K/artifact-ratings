from app import db

"""
Example data
    {
      "setKey": "ThunderingFury",
      "slotKey": "goblet",
      "rarity": 5,
      "mainStatKey": "anemo_dmg_",
      "level": 20,
      "substats": [
        {
          "key": "critRate_",
          "value": 6.2
        },
        {
          "key": "atk",
          "value": 37.0
        },
        {
          "key": "critDMG_",
          "value": 21.8
        },
        {
          "key": "def_",
          "value": 5.8
        }
      ],
      "location": "",
      "lock": false,
      "id": 192
    },
    {
      "setKey": "ThunderingFury",
      "slotKey": "goblet",
      "rarity": 5,
      "mainStatKey": "hydro_dmg_",
      "level": 20,
      "substats": [
        {
          "key": "critDMG_",
          "value": 27.2
        },
        {
          "key": "atk",
          "value": 14.0
        },
        {
          "key": "atk_",
          "value": 11.7
        },
        {
          "key": "enerRech_",
          "value": 4.5
        }
      ],
      "location": "",
      "lock": false,
      "id": 193
    },
    {
      "setKey": "ThunderingFury",
      "slotKey": "circlet",
      "rarity": 5,
      "mainStatKey": "critDMG_",
      "level": 20,
      "substats": [
        {
          "key": "def",
          "value": 16.0
        },
        {
          "key": "critRate_",
          "value": 9.3
        },
        {
          "key": "atk_",
          "value": 11.1
        },
        {
          "key": "atk",
          "value": 33.0
        }
      ],
      "location": "Dori",
      "lock": false,
      "id": 194
    },
"""

class Artifact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    setKey = db.Column(db.String(50), nullable=False)
    slotKey = db.Column(db.String(50), nullable=False)
    rarity = db.Column(db.Integer)
    mainStatKey = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer)

    # TODO: Substats
    