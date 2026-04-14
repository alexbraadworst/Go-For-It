image split_divider = Solid("#000000", xysize=(10, 1080))

transform split_left:
    crop (480, 0, 960, 1080)
    xalign 0.0

# This does the same, but shoves it right
transform split_right:
    crop (480, 0, 960, 1080)
    xalign 1.0
    
transform left_side_sprite:
    xalign 0.25
    yalign 1.0

transform right_side_sprite:
    xalign 0.75
    yalign 1.0


transform fly_across_screen:
    xpos -0.2 ypos 0.5 rotate 0      # Starts flat
    linear 1.5 xpos 1.2 rotate 360   