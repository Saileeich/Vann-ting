from app import App

def main():
    WIDTH, HEIGHT = 500, 500
    CAPTION = "Øygarden Simulator 2D"
    FPS = 24
    app = App(WIDTH, HEIGHT, CAPTION, FPS)
    app.run()

if __name__ == "__main__":
    main()