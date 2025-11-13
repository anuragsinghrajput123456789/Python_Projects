📸 Image Slideshow Viewer (Tkinter + PIL)

A clean, optimized, and interview-ready Image Slideshow Viewer built using Python, Tkinter, and Pillow (PIL).
The app displays images in a smooth, non-blocking slideshow using root.after() and supports auto-cycling through the images.

🚀 Features

✅ Smooth, non-freezing slideshow (no time.sleep())

✅ Object-oriented clean architecture

✅ Auto-play slideshow using itertools.cycle

✅ High-quality image resizing using LANCZOS

✅ Error handling for missing or unreadable images

✅ Simple, neat Tkinter UI

✅ Beginner-friendly & interview-ready code

🖼️ Demo

(Add your screenshot or GIF here if you want)

📦 Technologies Used

Python

Tkinter (GUI)

Pillow (PIL) for image handling

itertools.cycle for looping slideshow

📁 Project Structure
📂 image-slideshow-viewer
│── main.py
│── README.md
│── images/
│     ├── image1.jpg
│     ├── image2.jpg
│     └── ...

🧠 How It Works

Images are loaded & resized once at startup

Converted to PhotoImage for Tkinter

Slideshow cycles using cycle()

root.after() updates image every few seconds (non-blocking)

Button click starts slideshow

🛠️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/image-slideshow-viewer.git
cd image-slideshow-viewer

2. Install Required Library
pip install pillow

3. Run the Application
python main.py

🧩 Code Snippet (Main Logic)
self.label.config(image=next_img)
self.root.after(self.delay, self.show_next_image)


This ensures the slideshow never freezes and runs asynchronously.

📜 Full Code (main.py)
import tkinter as tk
from tkinter import messagebox
from itertools import cycle
from PIL import Image, ImageTk


class ImageSlideshowApp:
    def __init__(self, root, image_paths, delay=3000, image_size=(800, 800)):
        self.root = root
        self.root.title("Image Slideshow Viewer")
        self.delay = delay  # slideshow delay in ms

        # Load Images
        self.images = self.load_images(image_paths, image_size)
        self.slideshow_cycle = cycle(self.images)

        # GUI Elements
        self.label = tk.Label(root, bg="black")
        self.label.pack(fill="both", expand=True)

        self.play_button = tk.Button(root, text="Play Slideshow", command=self.start_slideshow)
        self.play_button.pack(pady=10)

        self.is_running = False

    def load_images(self, paths, size):
        loaded_images = []
        for path in paths:
            try:
                img = Image.open(path).resize(size, Image.Resampling.LANCZOS)
                loaded_images.append(ImageTk.PhotoImage(img))
            except Exception as e:
                messagebox.showerror("Error", f"Unable to load image:\n{path}\n\n{e}")
        if not loaded_images:
            messagebox.showerror("Error", "No images loaded!")
            self.root.destroy()
        return loaded_images

    def start_slideshow(self):
        if not self.is_running:
            self.is_running = True
            self.play_button.config(state="disabled")
            self.show_next_image()

    def show_next_image(self):
        if not self.is_running:
            return
        next_img = next(self.slideshow_cycle)
        self.label.config(image=next_img)
        self.root.after(self.delay, self.show_next_image)


if __name__ == "__main__":
    root = tk.Tk()

    image_paths = [
        r"C:\Users\91836\Pictures\Camera Roll\Bff\B612_20230802_113518_795.jpg",
        r"C:\Users\91836\Pictures\Camera Roll\Bff\B612_20230802_113810_421.jpg",
        r"C:\Users\91836\Pictures\Camera Roll\Bff\B612_20230802_114443_321.jpg",
        r"C:\Users\91836\Pictures\Camera Roll\Bff\B612_20230802_114743_140.jpg",
    ]

    app = ImageSlideshowApp(root, image_paths, delay=3000, image_size=(800, 800))
    root.mainloop()

📌 Future Enhancements (Optional)

You can easily extend this project with features like:

▶️ Pause / Resume button

⏭️ Next / Previous image

🗂️ Auto-load all images from a folder

🔍 Fullscreen mode

✨ Fade-in animation

⌨ Keyboard shortcuts

🖼 Thumbnails preview panel

Want these features? Just ask!

🤝 Contributing

Pull requests are welcome!
Feel free to open issues to suggest new features.

⭐ Show Your Support

If you like this project, please ⭐ star the repo — it motivates the creator!

If you want, I can also create:

✅ GitHub repo description
✅ Project banner
✅ Contributor badges
✅ Folder structure
✅ License file