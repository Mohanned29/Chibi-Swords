import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def load_and_scale_image(image_path, new_width, new_height):
    image = pygame.image.load(image_path)
    scaled_image = pygame.transform.scale(image, (new_width, new_height))
    return scaled_image

# Load images
base_img = load_and_scale_image("terrain/base.png", 120, 150)
base1_img = load_and_scale_image("terrain/base1.png", 120, 150)
base2_img = load_and_scale_image("terrain/base2.png", 120, 150)
base3_img = load_and_scale_image("terrain/base3.png", 120, 150)
base4_img = load_and_scale_image("terrain/base4.png", 120, 150)
base5_img = load_and_scale_image("terrain/base5.png", 120, 150)
base6_img = load_and_scale_image("terrain/base4.png", 120, 150)
base7_img = load_and_scale_image("terrain/base4.png", 120, 150)
flat_img = load_and_scale_image("terrain/flat.png", 120, 110)
flat1_img = load_and_scale_image("terrain/flat1.png", 120, 110)
flat2_img = load_and_scale_image("terrain/flat2.png", 120, 110)
flat3_img = load_and_scale_image("terrain/flat2.png", 120, 110)
tower1_img = load_and_scale_image("terrain/Tower_Blue.png", 100, 155)
tower2_img = load_and_scale_image("terrain/Tower_purple.png", 100, 155)
water = load_and_scale_image("terrain/Water.png", SCREEN_WIDTH, SCREEN_HEIGHT)
bridge = load_and_scale_image("terrain/bridge.png", 180, 80)
bridge1 = load_and_scale_image("terrain/bridge1.png", 180, 80)
foam_images = [load_and_scale_image(f"terrain/Foam{i}.png", 140, 150) for i in range(1, 9)]
archer_images = [load_and_scale_image(f"idleArcher/idle{i}.png", 50, 60) for i in range(1, 7)]
knight_images = [load_and_scale_image(f"knightBlueRun/Warrior_Blue{i}.png", 50, 60) for i in range(1, 7)]
torch_images = [load_and_scale_image(f"TorchRun/torch{i}.png", 60, 60) for i in range(1, 7)]

foam_animation_index = 0
foam_animation_speed = 0.1
foam_animation_time = 0

archer_animation_index = 0
archer_animation_speed = 0.1
archer_animation_time = 0

knight_animation_speed = 0.15
knight_animation_time = 0

torch_animation_speed = 0.15
torch_animation_time = 0

knights = [{"image_index": 0, "x": 180, "y": 265, "speed": 1}]
torchs = [{"image_index": 0, "x": 865, "y": 265, "speed": -1}]

def kill(obj, obj_list):
    obj_list.remove(obj)

def draw_scene():
    global foam_animation_index, foam_animation_time, archer_animation_index, archer_animation_time, knight_animation_time, torch_animation_time

    screen.blit(water, (0, 0))

    if pygame.time.get_ticks() > foam_animation_time:
        foam_animation_index = (foam_animation_index + 1) % len(foam_images)
        foam_animation_time = pygame.time.get_ticks() + int(1000 * foam_animation_speed)

    screen.blit(foam_images[foam_animation_index], (70, 320))
    screen.blit(foam_images[foam_animation_index], (325, 320))
    screen.blit(foam_images[foam_animation_index], (580, 320))
    screen.blit(foam_images[foam_animation_index], (835, 320))

    screen.blit(base_img, (80, 300))
    screen.blit(base1_img, (80, 270))
    screen.blit(base2_img, (335, 300))
    screen.blit(base3_img, (335, 270))
    screen.blit(base4_img, (590, 300))
    screen.blit(base5_img, (590, 270))
    screen.blit(base6_img, (845, 300))
    screen.blit(base7_img, (845, 270))
    screen.blit(flat_img, (80, 265))
    screen.blit(flat1_img, (335, 265))
    screen.blit(flat2_img, (590, 265))
    screen.blit(flat3_img, (845, 265))
    screen.blit(tower1_img, (85, 190))
    screen.blit(tower2_img, (865, 190))
    screen.blit(bridge, (180, 275))
    screen.blit(bridge1, (435, 275))
    screen.blit(bridge1, (690, 275))

    if pygame.time.get_ticks() > archer_animation_time:
        archer_animation_index = (archer_animation_index + 1) % len(archer_images)
        archer_animation_time = pygame.time.get_ticks() + int(1000 * archer_animation_speed)

    screen.blit(archer_images[archer_animation_index], (110, 180))

    for knight in knights[:]:
        knight["x"] += knight["speed"]

        if pygame.time.get_ticks() > knight_animation_time:
            knight["image_index"] = (knight["image_index"] + 1) % len(knight_images)
            knight_animation_time = pygame.time.get_ticks() + int(1000 * knight_animation_speed)

        screen.blit(knight_images[knight["image_index"]], (knight["x"], knight["y"]))

        if knight["x"] >= 865:
            kill(knight, knights)

    for torch in torchs[:]:
        torch["x"] += torch["speed"]

        if pygame.time.get_ticks() > torch_animation_time:
            torch["image_index"] = (torch["image_index"] + 1) % len(torch_images)
            torch_animation_time = pygame.time.get_ticks() + int(1000 * torch_animation_speed)

        screen.blit(torch_images[torch["image_index"]], (torch["x"], torch["y"]))

        if torch["x"] <= 85:
            kill(torch, torchs)

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_scene()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
