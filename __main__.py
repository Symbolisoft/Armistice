from engine import *

if __name__ == '__main__':
    g = Game()
    g.main_menu()
    g.new_game()
    while g.playing:
        g.main()

    pygame.quit()
    sys.exit()

    