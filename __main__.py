from engine import *


g = Game()
g.intro_screen()
g.new_game()
while g.playing:
    g.main()

pygame.quit()
sys.exit()