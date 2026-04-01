import pygame
import math

user_attempt = input("Enter password for a surprise: ")

if user_attempt == "911":
    spawn_plane = True
else:
    spawn_plane = False
    
# ---------------------------------------------------------
# 2. INITIALIZATION
# ---------------------------------------------------------
pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Global Variables
frames = 0
plane_x = -50
cloud_x = 200
cloud_y = 120

def lerp_color(c1, c2, t):
    return (
        int(c1[0] + (c2[0] - c1[0]) * t),
        int(c1[1] + (c2[1] - c1[1]) * t),
        int(c1[2] + (c2[2] - c1[2]) * t)
    )

# ---------------------------------------------------------
# 3. MAIN GAME LOOP
# ---------------------------------------------------------
running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # A. TIME LOGIC (0.0 to 1.0 cycle)
    frames += 1
    # 0.002 is the speed. Higher = faster cycle.
    time_of_day = (frames * 0.002) % 1.0 

    # B. CALCULATE SKY COLORS
    # brightness is 1.0 at high noon (0.25) and 0.0 at night (0.5 to 1.0)
    if time_of_day < 0.5:
        brightness = math.sin(time_of_day * 2 * math.pi)
    else:
        brightness = 0

    day_top, day_bottom = (135, 206, 235), (180, 220, 255)
    night_top, night_bottom = (5, 5, 20), (15, 15, 40) # Deep dark

    current_top = lerp_color(night_top, day_top, brightness)
    current_bottom = lerp_color(night_bottom, day_bottom, brightness)

    # C.sky gradient background
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        color = lerp_color(current_top, current_bottom, ratio)
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

    # D. sun/moon 
    arc_height = 300
    ground_y = 420

    if time_of_day < 0.5: 
        sun_t = time_of_day * 2 
        sun_x = int(sun_t * WIDTH)
        sun_y = int(ground_y - math.sin(sun_t * math.pi) * arc_height)
        pygame.draw.circle(screen, (255, 255, 0), (sun_x, sun_y), 30)
    else: 
        moon_t = (time_of_day - 0.5) * 2 
        moon_x = int(moon_t * WIDTH)
        moon_y = int(ground_y - math.sin(moon_t * math.pi) * arc_height)
        pygame.draw.circle(screen, (220, 220, 255), (moon_x, moon_y), 20)
        # Moon crescent shadow
        pygame.draw.circle(screen, current_top, (moon_x + 8, moon_y), 18)

    # Buildings (Dimmed based on brightness)
    b_color = lerp_color((20, 20, 30), (80, 80, 100), brightness)
    pygame.draw.rect(screen, b_color, (120, 260, 100, 600))
    pygame.draw.rect(screen, b_color, (380, 280, 120, 600))

    # Clouds
    pygame.draw.circle(screen, (230, 230, 230), (cloud_x, cloud_y), 30)
    pygame.draw.circle(screen, (230, 230, 230), (cloud_x + 25, cloud_y - 20), 30)
    pygame.draw.circle(screen, (230, 230, 230), (cloud_x + 50, cloud_y), 30)

    # F. CONDITIONAL PLANE DRAWING
    if spawn_plane is True:
        plane_x += 3
        if plane_x > WIDTH + 40:
            plane_x = -40

        plane_y = 100

        # body
        pygame.draw.rect(screen, (200, 200, 200), (plane_x, plane_y, 40, 10))
        # wings
        pygame.draw.polygon(screen, (180, 180, 180), [
            (plane_x + 10, plane_y),
            (plane_x + 20, plane_y - 10),
            (plane_x + 30, plane_y)
        ])
        # tail
        pygame.draw.polygon(screen, (160, 160, 160), [
            (plane_x, plane_y),
            (plane_x - 10, plane_y - 5),
            (plane_x, plane_y + 5)
        ])

    # UPDATE DISPLAY
    pygame.display.flip()
    clock.tick(60)

pygame.quit()