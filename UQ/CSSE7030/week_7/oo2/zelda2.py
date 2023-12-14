from game2 import GameApp
import tkinter as tk


class ZeldaGameApp(GameApp):
    def load_images(self):
        """Load images files into memory.

        load_images() -> None
        """

        ## Sourced from
        ## http://sjg2008.deviantart.com/art/Legend-of-Zelda-Dock-Icons-89988906
        ## http://lady-of-link.deviantart.com/art/25-days-of-Zelda-Finished-265423188
        ## http://blueamnesiac.deviantart.com/art/Evolution-of-Link-s-Sword-Wallpaper-306017315
        ## http://blueamnesiac.deviantart.com/art/LOZ-Cartoon-Crissword-Cursor-305341060
        ## http://blueamnesiac.deviantart.com/art/AOL-Box-Art-Sword-Cursor-416444257

        self.images = {
            "player": tk.PhotoImage(file='zelda/link.gif'),
            "balloon": tk.PhotoImage(file='zelda/dark-link.gif'),
            "purple": tk.PhotoImage(file='zelda/majoras.gif'),
            "triangle": tk.PhotoImage(file='zelda/insect.gif'),
            "sword": tk.PhotoImage(file='zelda/sword.gif'),
            "dagger": tk.PhotoImage(file='zelda/dagger.gif'),
            "potion": tk.PhotoImage(file='zelda/heart.gif'),
        }


def main():
    root = tk.Tk()
    app = ZeldaGameApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()