init python:
    # self improvement
    historical_self = {
        1849: [
            {
                "name": "Construct the Prussian State Telegraph",
                "cost": {"ap": 2},
                "reward": {"blood": 10, "iron": 5, "threat": 5}, 
                "target": "self_1849_telegraph"
            },
            {
                "name": "Inaugurate the first session of the Prussian Landtag",
                "cost": {"ap": 2},
                "reward": {"max_ap": 1},
                "target": "self_1849_landtag"
            }
        ],
        1850: [
            {
                "name": "Ratify the revised Constitution of Prussia",
                "cost": {"ap": 2},
                "reward": {"max_ap": 1, "threat": -5}, 
                "target": "self_1850_constitution"
            },
            {
                "name": "Establish the Central Press Bureau",
                "cost": {"ap": 2}, 
                "reward": {"blood": 5, "threat": 10},
                "target": "self_1850_police"
            }
        ],
        1862: [
            {
                "name": "Deliver 'Blood and Iron' Speech",
                "cost": {"ap": 2},
                "reward": {"blood": 15, "iron": 15, "threat": 10},
                "target": "self_speech_1862"
            }
        ]
    }
    standard_self = [
        {
            "name": "Study Machiavelli",
            "cost": {"ap": 1},
            "reward": {"blood": 2, "iron": 1},
            "target": "self_study"
        },
        {
            "name": "Military Drilling",
            "cost": {"ap": 2},
            "reward": {"blood": 5},
            "target": "self_drill"
        },
        {
            "name": "Fund Krupp Armaments",
            "cost": {"ap": 2},
            "reward": {"iron": 10, "threat": 5},
            "target": "self_krupp"
        },
        {
            "name": "See to the Rail Lines",
            "cost": {"ap": 1},
            "reward": {"iron": 2},
            "target": "self_rail"
        }
    ]

    # foreign diplomacy
    historical_diplomacy = {
        1848: [
            {
                "name": "Discuss Duckwitz's Tariff Plan",
                "cost": {"ap": 2},
                "reward": {"iron": 10},
                "target": "diplo_1848_duckwitz"
            }
        ],
        1849: [
            {
                "name": "Propose the Alliance of the Three Kings",
                "cost": {"ap": 3},
                "reward": {"iron": 15, "threat": 15}, # Attempting a conservative union
                "target": "diplo_1849_three_kings"
            }
        ],
        1850: [
            {
                "name": "Propose the Erfurt Union",
                "cost": {"ap": 3},
                "reward": {"iron": -5, "threat": -10},
                "target": "diplo_1850_union"
            }
        ],
        1864: [
            {
                "name": "Intervene in Schleswig-Holstein",
                "cost": {"ap": 3},
                "reward": {"blood": 15, "iron": 5, "threat": 20},
                "target": "diplo_1864_danish_war"
            }
        ]
    }
    standard_diplomacy = [
        {
            "name": "Send Envoys to Vienna",
            "cost": {"ap": 1},
            "reward": {"threat": -5},
            "target": "action_placate_austria"
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
                "name": "Praise Mecklenburg for not rioting",
                "cost": {"ap": 1},
                "reward": {
                    "affection_Mecklenburg-Vorpommern": 10
                },
                "target": "rel_1848_mecklenburg_date"
            }
        ],
        1849: [
            {
                "name": "Crush the May Uprising in Dresden",
                "cost": {"ap": 2},
                "reward": {
                    "affection_Saxony": 20,
                    "blood": 10,
                    "threat": 10
                },
                "target": "rel_1849_uprising"
            },
            {
                "name": "Help Baden (again)",
                "cost": {"ap": 3},
                "reward": {
                    "affection_Bavaria": 15,
                    "affection_Baden-Wurttemberg": 20, 
                    "blood": 15
                },
                "target": "rel_1849_palatinate"
            }
        ],
        1850: [
            {
                "name": "Bribe Saxony to stay in the Three Kings' Alliance",
                "cost": {"ap": 2},
                "req_affection": {"Saxony": 30},
                "reward": {"affection_Saxony": 15, "iron": 5},
                "target": "rel_1850_saxony_bribe"
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
            "req_affection": {"Bavaria": 50},
            "reward": {
                "affection_Bavaria": 5, 
                "affection_Baden-Wurttemberg": 5 # BFF bonus!
            },
            "target": "rel_bavaria_drink"
        },
        {
            "name": "Remind Baden-Wurttemberg about Marianne (France)",
            "cost": {"ap": 1},
            "reward": {
                "affection_Baden-Wurttemberg": 10, # Fear makes them clingy
                "threat": -5
            },
            "target": "rel_scare_baden"
        },
        {
            "name": "Help Mecklenburg-Vorpommern with the harvest",
            "cost": {"ap": 1},
            "reward": {
                "affection_Mecklenburg-Vorpommern": 10,
                "blood": 5
            },
            "target": "rel_farm_mecklenburg"
        },
        {
            "name": "Host a lavish gala for Saxony and Austria",
            "cost": {"ap": 3},
            "req_affection": {"Saxony": 40},
            "reward": {
                "affection_Saxony": 10, # Costs a lot to win over the hater
                "iron": -5,
                "threat": -10
            },
            "target": "rel_saxony_gala"
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
