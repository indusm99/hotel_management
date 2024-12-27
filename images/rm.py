import tkinter as tk

class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Define window width and height as a percentage of the screen size
        window_width = int(screen_width * 0.6)  # 80% of the screen width
        window_height = int(screen_height * 0.6)  # 80% of the screen height
        
        # Calculate position x and y to center the window on the screen
        position_x = int((screen_width - window_width) / 2)
        position_y = int((screen_height - window_height) / 2)
        
        # Set the geometry of the window
        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RoomBooking(root)
    root.mainloop()
