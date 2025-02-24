from engine import *

if __name__ == '__main__':
    g = Game()
    g.intro_screen()
    g.new_game()
    while g.playing:
        g.main()

    pygame.quit()
    sys.exit()

    