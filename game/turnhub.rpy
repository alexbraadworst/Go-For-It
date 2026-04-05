screen main_turn_screen():
    default current_tab = "self"

    # A master vbox keeps the top bar and the main window perfectly separated
    vbox:
        align (0.5, 0.5)
        spacing 20

        # stats
        frame:
            xsize 1600
            padding (20, 15) # height to automatically fits the 50x50 images
            
            hbox:
                align (0.5, 0.5)
                spacing 25
                
                text "Year: [year]" yalign 0.5 size 28 bold True
                text "Action Points: [action_points]" yalign 0.5 size 28 bold True
                
                image "blood" size (50, 50) yalign 0.5
                text "Blood: [blood]" yalign 0.5 size 28
                
                image "iron" size (50, 50) yalign 0.5
                text "Iron: [iron]" yalign 0.5 size 28
                
                image "threat" size (50, 50) yalign 0.5
                text "Threat: [threat]" yalign 0.5 size 28

                null width 50 

                textbutton "Advance Year":
                    yalign 0.5
                    text_size 28
                    text_bold True
                    
                    action Return("advance_year") 
                    # Only clickable when AP is 0 
                    sensitive (action_points <= 0)
        
        # main window
        frame:
            xysize (1600, 800)
            padding (20, 20)
            
            vbox:
                spacing 15

                # tabs
                hbox:
                    spacing 5
                    textbutton "Self-Improvement":
                        action SetScreenVariable("current_tab", "self")
                        selected (current_tab == "self")
                    textbutton "Diplomacy":
                        action SetScreenVariable("current_tab", "diplomacy")
                        selected (current_tab == "diplomacy")
                    textbutton "Relationships":
                        action SetScreenVariable("current_tab", "relationships")
                        selected (current_tab == "relationships")

                frame:
                    xysize (1560, 690) 
                    padding (20, 20)

                    # self tab
                    if current_tab == "self":
                        vbox:
                            spacing 10
                            text "Self Improvement - [year]" size 30 bold True
                            
                            $ current_historical_actions = historical_self.get(year, [])
                            if current_historical_actions:
                                text "Historical Events:" bold True color "#b22222"
                                for action in current_historical_actions:
                                    $ cost_ap = action["cost"].get("ap", 0)
                                    $ can_afford = (action_points >= cost_ap)
                                    textbutton "[action['name']] (Cost: [cost_ap] AP)":
                                        action Return(action) 
                                        sensitive can_afford
                                        
                            null height 10 
                            
                            text "Standard Actions:" bold True
                            for action in standard_self:
                                $ cost_ap = action["cost"].get("ap", 0)
                                $ can_afford = (action_points >= cost_ap)
                                textbutton "[action['name']] (Cost: [cost_ap] AP)":
                                    action Return(action) 
                                    sensitive can_afford

                    # diplomacy tab
                    elif current_tab == "diplomacy":
                        vbox:
                            spacing 10
                            text "Foreign Diplomacy - [year]" size 30 bold True
                            
                            $ current_historical_actions = historical_diplomacy.get(year, [])
                            if current_historical_actions:
                                text "Historical Events:" bold True color "#b22222"
                                for action in current_historical_actions:
                                    $ cost_ap = action["cost"].get("ap", 0)
                                    $ can_afford = (action_points >= cost_ap)
                                    textbutton "[action['name']] (Cost: [cost_ap] AP)":
                                        action Return(action) 
                                        sensitive can_afford
                                        
                            null height 10
                            
                            text "Standard Actions:" bold True
                            for action in standard_diplomacy:
                                $ cost_ap = action["cost"].get("ap", 0)
                                $ can_afford = (action_points >= cost_ap)
                                textbutton "[action['name']] (Cost: [cost_ap] AP)":
                                    action Return(action) 
                                    sensitive can_afford

                    # relationships tab
                    elif current_tab == "relationships":
                        hbox:
                            spacing 30
                            
                            # suitor meters
                            vbox:
                                xsize 960 # Takes up about 60% of the screen width
                                spacing 15
                                text "Intra-German 'Relations' - [year]" size 30 bold True

                                viewport:
                                    xysize (960, 580)
                                    scrollbars "vertical"
                                    mousewheel True
                                    
                                    vpgrid:
                                        cols 2
                                        spacing 15
                                        
                                        for state, affection in suitor_relations.items():
                                            frame:
                                                xysize (460, 100) # sized so two fit in the 960w grid
                                                padding (10, 10)
                                                
                                                hbox:
                                                    spacing 15
                                                    yalign 0.5
                                                    
                                                    add "face_" + state.lower() size (80, 80)
                                                    
                                                    vbox:
                                                        spacing 5
                                                        text "[state]" bold True size 22
                                                        
                                                        hbox:
                                                            spacing 10
                                                            bar:
                                                                value affection 
                                                                range 100 
                                                                xysize (250, 20) 
                                                                left_bar "#ff69b4" 
                                                                right_bar "#444444"
                                                                yalign 0.5
                                                            text "[affection]/100" size 16 yalign 0.5

                            # actions
                            vbox:
                                xsize 530 # takes up the remaining 40%
                                spacing 15
                                text "Available Actions:" bold True size 30
                                
                                # actions in their own viewport for infinite buttons
                                viewport:
                                    xysize (530, 580)
                                    scrollbars "vertical"
                                    mousewheel True
                                    
                                    vbox:
                                        spacing 10
                                        
                                        $ current_historical_actions = historical_relations.get(year, [])
                                        if current_historical_actions:
                                            text "Historical Opportunities:" bold True color "#b22222"
                                            for action in current_historical_actions:
                                                $ cost_ap = action["cost"].get("ap", 0)
                                                $ can_afford = (action_points >= cost_ap)
                                                textbutton "[action['name']] (Cost: [cost_ap] AP)":
                                                    action Return(action) 
                                                    sensitive can_afford
                                        
                                        null height 10
                                        
                                        text "Standard Actions:" bold True
                                        for action in standard_relations:
                                            $ cost_ap = action["cost"].get("ap", 0)
                                            $ can_afford = (action_points >= cost_ap)
                                            textbutton "[action['name']] (Cost: [cost_ap] AP)":
                                                action Return(action) 
                                                sensitive can_afford