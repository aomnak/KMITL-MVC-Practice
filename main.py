from controller.KaraokeController import KaraokeController  
 
def main():
    controller = KaraokeController()  
    while True:
        controller.add_new_song()
        cont = input("Add another song? (y/n): ").lower()
        if cont != 'y':
            break

if __name__ == '__main__':
    main()
