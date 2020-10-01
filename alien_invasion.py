import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard 
from button import Button
from ship import Ship 
import game_functions as gf

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

music=pygame.mixer.music.load('music/music.mp3')

def run_game():
	# Initialize pygame, settings and screen object.
	pygame.mixer.music.set_volume(0.02)
	pygame.mixer.music.play(-1)
	pygame.init()
	ai_settings=Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Make the play button
	play_button = Button(ai_settings,screen,"Play")

	# Create an instance to store game statistics and create a scoreboard
	stats = GameStats(ai_settings)
	sb=Scoreboard(ai_settings,screen,stats)

	# Make a ship,  a group of bullets and a group of aliens
	ship=Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	# Create the fleet of aliens
	gf.create_fleet(ai_settings,screen,ship,aliens)

	# Start main loop for the game
	while True:
		gf.check_events(ai_settings, screen, stats, sb,play_button, ship, aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,ship,stats,sb,aliens,bullets,play_button)

run_game()