from engine import *

if __name__ == '__main__':
    g = Game()
    g.main_menu()
    
    while g.playing:
        g.main()

    pygame.quit()
    sys.exit()

