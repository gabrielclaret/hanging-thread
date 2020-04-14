from game import g_game
import xml.etree.ElementTree as ET 

def parse_monsters():
    print("Monster parsing started...")

    tree = ET.parse("monsters.xml")
    root = tree.getroot()

    for monster in root.iter("monster"):
        look = monster.find("look")
        walk = monster.find("walk")
        shoot = monster.find("shoot")

        g_game.parsed_monsters[monster.attrib["name"]] = {
            "attack":          int(monster.attrib["attack"]),
            "health":          int(monster.attrib["health"]),
            "speed":           int(monster.attrib["speed"]),
            "weight":          int(monster.attrib["weight"]),
            "immortal":        int(monster.attrib["immortal"]),
            "collision":       int(monster.attrib["collision"]),
            "look_color":      [int(color) for color in look.attrib["color"].split(",")],
            "look_width":      int(look.attrib["width"]),
            "look_height":     int(look.attrib["height"]),
            "walk_pattern":    walk.attrib["pattern"],
            "walk_horizontal": int(walk.attrib["horizontal"]),
            "walk_direction":  int(walk.attrib["direction"]),
            "walk_steps":      int(walk.attrib["steps"]),
            "shoot_pattern":   shoot.attrib["pattern"],
            "shoot_cooldown":  int(shoot.attrib["cooldown"]),
            "shoot_range":     int(shoot.attrib["range"]),
            "shoot_speed":     int(shoot.attrib["speed"]),
            "shoot_color":     [int(color) for color in shoot.attrib["color"].split(",")],   
            "shoot_width":     int(shoot.attrib["width"]),
            "shoot_height":    int(shoot.attrib["height"])
        }

    print("Monster parsing finished...")

def parse_levels():
    print("Level parsing started...")

    tree = ET.parse("levels.xml")
    root = tree.getroot()

    for level in root.iter("level"):
        levelers_pointer = level.find("levelers")
        monsters_pointer = level.find("monsters")

        levelers = []
        monsters = []

        for leveler in levelers_pointer.iter("leveler"):
            look = leveler.find("look")
            walk = leveler.find("walk")

            levelers.append({
                "startx":          int(leveler.attrib["startx"]),
                "starty":          int(leveler.attrib["starty"]),
                "health":          int(leveler.attrib["health"]),
                "speed":           int(leveler.attrib["speed"]),
                "immortal":        int(leveler.attrib["immortal"]),
                "collision":       int(leveler.attrib["collision"]),         
                "look_color":      [int(color) for color in look.attrib["color"].split(",")],
                "look_width":      int(look.attrib["width"]),
                "look_height":     int(look.attrib["height"]),
                "walk_pattern":    walk.attrib["pattern"],
                "walk_horizontal": int(walk.attrib["horizontal"]),
                "walk_direction":  int(walk.attrib["direction"]),
                "walk_steps":      int(walk.attrib["steps"]),
                "sprite":          look.attrib["sprite"]
            })

        for monster in monsters_pointer.iter("monster"):
            monsters.append({
                "name":   monster.attrib["name"],
                "startx": int(monster.attrib["startx"]),
                "starty": int(monster.attrib["starty"])
            })

        start_x = int(level.attrib["startx"]) 
        start_y = int(level.attrib["starty"]) 

        g_game.parsed_levels.append({
            "startx":   start_x,
            "starty":   start_y,
            "levelers": levelers,
            "monsters": monsters
        })

    print("Level parsing finished...")