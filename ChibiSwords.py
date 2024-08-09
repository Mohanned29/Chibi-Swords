import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def load_and_scale_image(image_path, new_width, new_height):
    image = pygame.image.load(image_path)
    scaled_image = pygame.transform.scale(image, (new_width, new_height))
    return scaled_image

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
sand_img = load_and_scale_image("terrain/sand.png", 100, 100)
sand1_img = load_and_scale_image("terrain/sand1.png", 100, 100)
borders_img = pygame.image.load("terrain/borders.png")
borders1_img = pygame.image.load("terrain/borders1.png")
water = load_and_scale_image("terrain/Water.png", SCREEN_WIDTH, SCREEN_HEIGHT)
sandBig = load_and_scale_image("terrain/sandBig.png", 600 , 300)
bridge = load_and_scale_image("terrain/bridge.png",180,80)
bridge1 = load_and_scale_image("terrain/bridge1.png",180,80)
bridge2 = load_and_scale_image("terrain/bridge2.png",180,80)
bridgeShadow = load_and_scale_image("terrain/BridgeShadow.png",130,80)
foam_images = [load_and_scale_image(f"terrain/Foam{i}.png", 140, 150) for i in range(1, 9)]

# Animation variables
foam_animation_index = 0
foam_animation_speed = 0.1  # Adjust the speed of the foam animation
foam_animation_time = 0

def draw_scene():
    global foam_animation_index, foam_animation_time

    # Draw the background
    screen.blit(water, (0, 0))  # Correctly blit the water image

    # Draw the rest of the images
    #screen.blit(sandBig, (600, 300))

    # Draw the foam animation at the base of each object
    if pygame.time.get_ticks() > foam_animation_time:
        foam_animation_index = (foam_animation_index + 1) % len(foam_images)
        foam_animation_time = pygame.time.get_ticks() + int(1000 * foam_animation_speed)
    
    # Position the foam at the base
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
    #screen.blit(sand_img, (80, 400))
    #screen.blit(sand1_img, (180, 400))
    #screen.blit(borders_img, (80, 390))
    #screen.blit(borders1_img, (120, 390))
    screen.blit(bridge, (180,275))
    screen.blit(bridge1, (435,275))
    screen.blit(bridge1, (690,275))

    

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the scene
        draw_scene()

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Cap the frame rate at 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
