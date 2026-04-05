init python:
    # self improvement
    historical_self = {
        1848: [
            {
                "name": "Construct the Prussian State Telegraph",
                "cost": {"ap": 2},
                "reward": {"blood": 10, "iron": 5, "threat": 5}, 
                "target": "action_state_telegraph"
            }
        ],
        1849: [
            {
                "name": "Construct the Prussian State Telegraph",
                "cost": {"ap": 2},
                "reward": {"blood": 10, "iron": 5, "threat": 5}, 
                "target": "action_state_telegraph"
            }
        ],
        1862: [
            {
                "name": "Deliver 'Blood and Iron' Speech",
                "cost": {"ap": 2},
                "reward": {"blood": 15, "iron": 15, "threat": 10},
                "target": "event_speech_1862"
            }
        ]
    }
    standard_self = [
        {
            "name": "Study Machiavelli",
            "cost": {"ap": 1},
            "reward": {"iron": 2},
            "target": "action_study"
        },
        {
            "name": "Military Drilling",
            "cost": {"ap": 2},
            "reward": {"blood": 5},
            "target": "action_drill"
        }
    ]

    # foreign diplomacy
    historical_diplomacy = {
        1864: [
            {
                "name": "Intervene in Schleswig-Holstein",
                "cost": {"ap": 3},
                "reward": {"blood": 15, "iron": 5, "threat": 20},
                "target": "event_danish_war"
            }
        ]
    }
    standard_diplomacy = [
        {
            "name": "Send Envoys to Vienna",
            "cost": {"ap": 1},
            "reward": {"threat": -5},
            "target": "action_placate_austria"
        },
        {
            "name": "Fund Krupp Armaments",
            "cost": {"ap": 2},
            "reward": {"iron": 10, "threat": 5},
            "target": "action_krupp"
        }
    ]

    # "relations" :3
    historical_relations = {
        1848: [
            {
                "name": "March to the defense of Schleswig and Holstein",
                "cost": {"ap": 2},
                "reward": {
                    "affection_Schleswig": 25,
                    "affection_Holstein": 25,
                    "blood": 10,
                    "iron": 10,
                    "threat": 15
                },
                "target": "rel_1848_danish_war"
            },
            {
                "name": "Send troops to crush the Hecker Uprising in Baden",
                "cost": {"ap": 2},
                "reward": {
                    "affection_Baden-Wurttemberg": 20, 
                    "threat": -10,
                    "blood": 5
                },
                "target": "rel_1848_baden_rebellion"
            },
            {
                "name": "Send 'condolences' to Bavaria over the Lola Montez scandal",
                "cost": {"ap": 1},
                "reward": {
                    "affection_Bavaria": 15 
                },
                "target": "rel_1848_bavaria_scandal"
            },
            {
                "name": "Reassure Hanover",
                "cost": {"ap": 1},
                "reward": {
                    "affection_Hanover": 10,
                    "iron": 5
                },
                "target": "rel_1848_hanover_panic"
            },
            {
                "name": "Praise Mecklenburg for not rioting",
                "cost": {"ap": 1},
                "reward": {
                    "affection_Mecklenburg-Vorpommern": 10
                },
                "target": "rel_1848_mecklenburg_date"
            }
        ],
        1864: [
            {
                "name": "Liberate Schleswig & Holstein from Denmark",
                "cost": {"ap": 4},
                "reward": {
                    "affection_Schleswig": 40, 
                    "affection_Holstein": 40, 
                    "iron": 15, 
                    "threat": 20
                },
                "target": "event_danish_war_dating"
            }
        ],
        1866: [
            {
                "name": "Force Hanover's Submission (Austro-Prussian War)",
                "cost": {"ap": 3},
                "reward": {
                    "affection_Hanover": -50, # They hate you for this...
                    "blood": 20, 
                    "threat": 30
                },
                "target": "event_hanover_conquest"
            }
        ]
    }

    standard_relations = [
        {
            "name": "Send beer kegs to Bavaria",
            "cost": {"ap": 2},
            "reward": {
                "affection_Bavaria": 15, 
                "affection_Baden-Wurttemberg": 5 # BFF bonus!
            },
            "target": "action_bavaria_drink"
        },
        {
            "name": "Remind Baden-Wurttemberg about Marianne (France)",
            "cost": {"ap": 1},
            "reward": {
                "affection_Baden-Wurttemberg": 10, # Fear makes them clingy
                "threat": -5
            },
            "target": "action_scare_baden"
        },
        {
            "name": "Help Mecklenburg-Vorpommern with the harvest",
            "cost": {"ap": 1},
            "reward": {
                "affection_Mecklenburg-Vorpommern": 10,
                "blood": 5
            },
            "target": "action_farm_mecklenburg"
        },
        {
            "name": "Host a lavish gala for Saxony and Austria",
            "cost": {"ap": 3},
            "reward": {
                "affection_Saxony": 20, # Costs a lot to win over the hater
                "threat": -10
            },
            "target": "action_saxony_gala"
        },
        {
            "name": "Invite Holstein to a German culture festival",
            "cost": {"ap": 2},
            "reward": {
                "affection_Holstein": 15,
                "affection_Schleswig": 15 # Schleswig always tags along!
            },
            "target": "action_holstein_festival"
        }
    ]
