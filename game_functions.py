import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Respond to key presses """
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship): 
    """ Respond to key releases """
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False 
def fire_bullet(ai_settings, screen, ship, bullets):
    """ Fire a bullet if limit not reached yet """
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    
    #Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    # Make the most recently drawn screen viable
    pygame.display.flip()


def update_bullets(bullets):
    """ Update position of bulelts and get rid of the old bullets """
    # Update bullet position
    bullets.update()

    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)