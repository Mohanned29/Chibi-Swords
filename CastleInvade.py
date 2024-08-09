import curses
import time

def draw_castle(stdscr):
    # Initialize color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    stdscr.clear()

    # Define the player's castle ASCII art
    player_castle = [
        "          |>>>|",
        "          _  _|_  _       ",
        "         |;|_|;|_|;|      ",
        "         \\.    .  /     ",
        "          \\:  .  /      ",
        "           ||:   |       ",
        "           ||:.  |       ",
        "           ||:  .|       ",
        "           ||:   |       ",
        "           ||: , |       ",
        "           ||:   |       ",
        "       __--||: . |--__   ",
        "       \\   ||:   |   /  ",
        "        \\  ||: , |  /   ",
        "         \\||:   .||/    "
    ]
    
    # Define the enemy's castle ASCII art
    enemy_castle = [
        "          |>>>|",
        "          _  _|_  _       ",
        "         |;|_|;|_|;|      ",
        "         \\.    .  /     ",
        "          \\:  .  /      ",
        "           ||:   |       ",
        "           ||:.  |       ",
        "           ||:  .|       ",
        "           ||:   |       ",
        "           ||: , |       ",
        "           ||:   |       ",
        "       __--||: . |--__   ",
        "       \\   ||:   |   /  ",
        "        \\  ||: , |  /   ",
        "         \\||:   .||/    "
    ]

    # Define enemies with their ASCII art, health, and attack power
    enemies = {
        "Goblin": {
            "art": """
  /\\
 (o o)
  \\_/
  / \\
""",
            "health": 30,
            "attack": 10
        },
        "Knight": {
            "art": """
  /\\
 |__|
 |  |
 |__|
 /  \\
""",
            "health": 50,
            "attack": 20
        },
        "Orc": {
            "art": """
  ___
 [o o]
  \\_/
 / | \\
 | | |
 |___|
""",
            "health": 40,
            "attack": 15
        },
        "Troll": {
            "art": """
  _____
  ( o o )
  \\___/
  / | \\
  (  |  )
  |___|
""",
            "health": 60,
            "attack": 25
        }
    }

    # Define phases
    phases = {
        1: [("Goblin", 5)],  # 5 Goblins in phase 1
        2: [("Goblin", 5), ("Orc", 3)],  # 5 Goblins and 3 Orcs in phase 2
        3: [("Goblin", 5), ("Orc", 3), ("Knight", 2)],  # Add Knights in phase 3
        4: [("Goblin", 5), ("Orc", 3), ("Knight", 2), ("Troll", 1)]  # Add Trolls in phase 4
    }

    height, width = stdscr.getmaxyx()
    y1, x1 = 0, 0
    y2 = 0
    x2 = width - len(enemy_castle[0]) - 10

    # Draw player's castle
    color_pair1 = curses.color_pair(1)
    for line in player_castle:
        stdscr.addstr(y1, x1, line, color_pair1)
        y1 += 1

    # Draw enemy's castle
    color_pair2 = curses.color_pair(2)
    for line in enemy_castle:
        stdscr.addstr(y2, x2, line, color_pair2)
        y2 += 1

    # Function to spawn and move enemies
    def spawn_and_move_enemies(stdscr, phase, x2, y2):
        current_phase = phases[phase]
        player_castle_health = 1000
        enemies_on_screen = []
        spawn_delay = 0.5

        for enemy_type, count in current_phase:
            for _ in range(count):
                enemy = {
                    "type": enemy_type,
                    "health": enemies[enemy_type]["health"],
                    "attack": enemies[enemy_type]["attack"],
                    "x": x2 - 5,  # Start next to the enemy castle
                    "y": len(enemy_castle) - 5  # Align with the castle
                }
                enemies_on_screen.append(enemy)
                time.sleep(spawn_delay)

                # Move enemies towards player's castle
                while enemies_on_screen and player_castle_health > 0:
                    stdscr.clear()

                    # Redraw player's castle
                    y1, x1 = 0, 0
                    for line in player_castle:
                        stdscr.addstr(y1, x1, line, color_pair1)
                        y1 += 1

                    # Redraw enemy's castle
                    y2, x2 = 0, width - len(enemy_castle[0]) - 10
                    for line in enemy_castle:
                        stdscr.addstr(y2, x2, line, color_pair2)
                        y2 += 1

                    # Draw and move all enemies
                    for enemy in enemies_on_screen:
                        enemy_art = enemies[enemy["type"]]["art"].strip().split("\n")
                        for i, line in enumerate(enemy_art):
                            if 0 <= enemy["y"] + i < height and 0 <= enemy["x"] < width - len(line):
                                stdscr.addstr(enemy["y"] + i, enemy["x"], line, curses.color_pair(2))

                        enemy["x"] -= 1  # Move enemy leftwards

                        # Check if enemy has reached the player's castle
                        if enemy["x"] < x1 + len(player_castle[0]):
                            player_castle_health -= enemies[enemy["type"]]["attack"]
                            enemies_on_screen.remove(enemy)

                    stdscr.refresh()
                    time.sleep(0.1)  # Adjust the game speed

                    if player_castle_health <= 0:
                        break

        return player_castle_health

    # Example game loop for phases
    for phase in range(1, 5):  # Phases 1 to 4
        player_castle_health = spawn_and_move_enemies(stdscr, phase, x2, y2)
        if player_castle_health <= 0:
            break
        stdscr.addstr(height // 2, width // 2, f"Phase {phase} complete!", curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()
        time.sleep(2)  # Pause before the next phase

    if player_castle_health <= 0:
        stdscr.addstr(height // 2, width // 2, "Game Over!", curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()

# Initialize curses
curses.wrapper(draw_castle)
