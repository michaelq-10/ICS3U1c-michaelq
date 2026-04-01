import pygame
import math

# password
user_attempt = input("Enter password for a surprise: ")

if user_attempt == "911":
    spawn_plane = True
else:
    spawn_plane = False

# Initialization
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# global var
frames = 0
plane_x = -50
clouds = [
    [200, 120],
    [400, 80],
    [550, 150]
]

# Buildings for looping city
building_width = 100
building_spacing = 150
num_buildings = WIDTH // building_spacing + 3
buildings = [i * building_spacing for i in range(num_buildings)]

# func
def lerp_color(c1, c2, t):
    return (
        int(c1[0] + (c2[0] - c1[0]) * t),
        int(c1[1] + (c2[1] - c1[1]) * t),
        int(c1[2] + (c2[2] - c1[2]) * t)
    )

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Time logic
    frames += 1
    time_of_day = (frames * 0.002) % 1.0

    # Brightness (sun high at 0.25)
    if time_of_day < 0.5:
        brightness = math.sin(time_of_day * 2 * math.pi)
    else:
        brightness = 0

    # Sky colors
    day_top, day_bottom = (135, 206, 235), (180, 220, 255)
    night_top, night_bottom = (5, 5, 20), (15, 15, 40)

    current_top = lerp_color(night_top, day_top, brightness)
    current_bottom = lerp_color(night_bottom, day_bottom, brightness)

    # Sky gradient
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        color = lerp_color(current_top, current_bottom, ratio)
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

    # Sun/Moon
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
        pygame.draw.circle(screen, current_top, (moon_x + 8, moon_y), 18)

    # ---------------- city ----------------
    b_color = lerp_color((20, 20, 30), (80, 80, 100), brightness)
    for i in range(len(buildings)):
        x = (buildings[i] - frames*1.5) % (WIDTH + building_spacing) - building_spacing
        height = 200 + (i % 3)*50
        pygame.draw.rect(screen, b_color, (x, HEIGHT - height, building_width, height))

    # ---------------- clouds ----------------
    for cloud in clouds:
        cloud[0] += 1.2
        if cloud[0] > WIDTH + 50:
            cloud[0] = -50
        pygame.draw.circle(screen, (230, 230, 230), (int(cloud[0]), int(cloud[1])), 30)
        pygame.draw.circle(screen, (230, 230, 230), (int(cloud[0]) + 25, int(cloud[1]) - 20), 30)
        pygame.draw.circle(screen, (230, 230, 230), (int(cloud[0]) + 50, int(cloud[1])), 30)

    # ---------------- plane ----------------
    if spawn_plane:
        plane_x += 3
        if plane_x > WIDTH + 40:
            plane_x = -40
        plane_y = 100
        # Body
        pygame.draw.rect(screen, (200, 200, 200), (plane_x, plane_y, 40, 10))
        # Wings
        pygame.draw.polygon(screen, (180, 180, 180), [
            (plane_x + 10, plane_y),
            (plane_x + 20, plane_y - 10),
            (plane_x + 30, plane_y)
        ])
        # Tail
        pygame.draw.polygon(screen, (160, 160, 160), [
            (plane_x, plane_y),
            (plane_x - 10, plane_y - 5),
            (plane_x, plane_y + 5)
        ])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
