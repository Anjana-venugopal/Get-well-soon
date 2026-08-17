import tkinter as tk
from tkinter import messagebox
import random
import math

# ==============================================================================
# 💌 CUSTOMIZE YOUR MESSAGES HERE!
# ==============================================================================
BABES_NAME = "Babe"          # Change to your nickname for them
YOUR_NAME = "Your Favorite Person" # Change to your name
MAIN_TITLE = "Sending You Lots of Love & Healing Vibes! ✨"
# ==============================================================================

class HeartParticle:
    """Represents a floating heart on the canvas."""
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.x = random.randint(20, width - 20)
        self.y = random.randint(height, height + 100)
        self.size = random.randint(12, 28)
        self.speed = random.uniform(1.2, 3.0)
        self.amplitude = random.uniform(10, 30)
        self.frequency = random.uniform(0.02, 0.05)
        self.step = random.uniform(0, 100)
        self.symbol = random.choice(["❤️", "💖", "💕", "🌸", "🧸", "✨", "💗"])
        
        self.id = canvas.create_text(
            self.x, self.y, 
            text=self.symbol, 
            font=("Arial", self.size), 
            anchor="center"
        )

    def move(self):
        self.step += 1
        self.y -= self.speed
        # Oscillate sideways slightly
        x_offset = math.sin(self.step * self.frequency) * self.amplitude
        current_x = self.x + x_offset
        
        self.canvas.coords(self.id, current_x, self.y)
        
        # Reset heart position when it goes above the top frame
        if self.y < -30:
            self.y = self.height + random.randint(10, 50)
            self.x = random.randint(20, self.width - 20)
            self.step = random.uniform(0, 100)

class GetWellSoonApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"A Special Care Package For {BABES_NAME} ❤️")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#fff5f5")

        # Hug counter state
        self.hug_count = 0

        # Background Canvas for Animations
        self.canvas = tk.Canvas(self.root, bg="#fff5f5", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Create Floating Hearts Animation
        self.hearts = []
        for _ in range(25):
            self.hearts.append(HeartParticle(self.canvas, 600, 700))

        # Main Card UI Container (Placed on Canvas)
        self.create_card_ui()

        # Start animation loop
        self.animate()

    def create_card_ui(self):
        # Center Frame
        card_frame = tk.Frame(self.canvas, bg="#ffffff", bd=0, relief="flat", highlightbackground="#ffd1d1", highlightthickness=2)
        card_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=580)

        # Top Header
        title_label = tk.Label(
            card_frame, 
            text=f"Get Well Soon, {BABES_NAME}! 🩹❤️", 
            font=("Helvetica", 20, "bold"), 
            bg="#ffffff", 
            fg="#e63946"
        )
        title_label.pack(pady=(25, 5))

        subtitle_label = tk.Label(
            card_frame, 
            text=MAIN_TITLE, 
            font=("Helvetica", 11, "italic"), 
            bg="#ffffff", 
            fg="#7d7d7d"
        )
        subtitle_label.pack(pady=(0, 15))

        # Big Animated Heart Banner
        self.pulse_symbol = tk.Label(
            card_frame, 
            text="🩹💗🤒", 
            font=("Segoe UI Emoji", 36), 
            bg="#ffffff"
        )
        self.pulse_symbol.pack(pady=5)

        # Sweet Note Box
        note_text = (
            f"Dear {BABES_NAME},\n\n"
            "I'm sending you all my warmest thoughts, softest blankets, and "
            "biggest love! Rest up, stay cozy, and remember that I'm right here "
            "cheering for your speedy recovery.\n\n"
            "Here is your emergency virtual care package 👇"
        )
        note_label = tk.Label(
            card_frame, 
            text=note_text, 
            font=("Helvetica", 11), 
            bg="#fff0f3", 
            fg="#4a4a4a", 
            wraplength=420, 
            justify="center",
            padx=15, 
            pady=15
        )
        note_label.pack(pady=15)

        # Buttons Grid for Interactive Care Package
        btn_frame = tk.Frame(card_frame, bg="#ffffff")
        btn_frame.pack(pady=10)

        soup_btn = tk.Button(
            btn_frame, text="🥣 Warm Noodle Soup", font=("Helvetica", 10, "bold"),
            bg="#ffccd5", fg="#800f2f", activebackground="#ffb3c1", relief="flat",
            padx=12, pady=8, cursor="hand2", command=self.serve_soup
        )
        soup_btn.grid(row=0, column=0, padx=8, pady=6)

        meds_btn = tk.Button(
            btn_frame, text="💊 Love Prescription", font=("Helvetica", 10, "bold"),
            bg="#ffccd5", fg="#800f2f", activebackground="#ffb3c1", relief="flat",
            padx=12, pady=8, cursor="hand2", command=self.give_medicine
        )
        meds_btn.grid(row=0, column=1, padx=8, pady=6)

        flower_btn = tk.Button(
            btn_frame, text="🌸 Pick a Healing Flower", font=("Helvetica", 10, "bold"),
            bg="#ffccd5", fg="#800f2f", activebackground="#ffb3c1", relief="flat",
            padx=12, pady=8, cursor="hand2", command=self.pick_flower
        )
        flower_btn.grid(row=1, column=0, padx=8, pady=6)

        hug_btn = tk.Button(
            btn_frame, text="🧸 Send Giant Hug", font=("Helvetica", 10, "bold"),
            bg="#ffccd5", fg="#800f2f", activebackground="#ffb3c1", relief="flat",
            padx=12, pady=8, cursor="hand2", command=self.send_hug
        )
        hug_btn.grid(row=1, column=1, padx=8, pady=6)

        # Interactive Hug Tracker
        self.hug_label = tk.Label(
            card_frame, 
            text="Hugs received today: 0", 
            font=("Helvetica", 10, "bold"), 
            bg="#ffffff", 
            fg="#c9184a"
        )
        self.hug_label.pack(pady=(10, 0))

        # Footer
        footer_label = tk.Label(
            card_frame, 
            text=f"Made with ❤️ by {YOUR_NAME}", 
            font=("Helvetica", 9), 
            bg="#ffffff", 
            fg="#a0a0a0"
        )
        footer_label.pack(side="bottom", pady=15)

    def animate(self):
        """Update floating particles and pulse icon."""
        for heart in self.hearts:
            heart.move()

        # Repeat frame update approx 30 fps
        self.root.after(33, self.animate)

    # Button Event Handlers
    def serve_soup(self):
        messagebox.showinfo(
            "Warm Soup Served! 🥣",
            f"Here is a fresh bowl of hot chicken/veggie soup made with extra love for {BABES_NAME}!\n\n"
            "• Temperature: Perfectly cozy\n"
            "• Side dish: Infinite kisses\n\n"
            "Blow on it gently before eating! 🥄"
        )

    def give_medicine(self):
        messagebox.showinfo(
            "Doctor's Prescription 📋",
            f"OFFICIAL RECOVERY PLAN FOR {BABES_NAME.upper()}:\n\n"
            "1. Take 1 long nap (Mandatory) 💤\n"
            "2. Drink 1 big glass of water 💧\n"
            "3. Unlimited forehead kisses 💋\n"
            "4. Zero stress allowed today! 🚫\n\n"
            "Refills available 24/7!"
        )

    def pick_flower(self):
        flowers = [
            ("🌻 Sunflower", "To bring a little sunshine and brightness to your day!"),
            ("🌷 Tulip", "A reminder that you're so special and loved."),
            ("🌸 Cherry Blossom", "Gentle, beautiful, and resilient—just like you."),
            ("🌹 Red Rose", "To remind you how deeply I love you every single day!"),
            ("🌼 Daisy", "A fresh bloom to bring cheer and restful vibes.")
        ]
        chosen_flower, note = random.choice(flowers)
        messagebox.showinfo(
            f"You Picked a {chosen_flower}!",
            f"{note}\n\nVirtual bouquet sent straight to your bedside! 💐"
        )

    def send_hug(self):
        self.hug_count += 1
        self.hug_label.config(text=f"Hugs received today: {self.hug_count}")
        
        # Change pulse symbol temporarily
        self.pulse_symbol.config(text="🧸🫂💖")
        self.root.after(1000, lambda: self.pulse_symbol.config(text="🩹💗🤒"))
        
        messages = [
            "SQUEEEEZE! Huge warm hug incoming! 🤗",
            "Hold on tight! Another cozy hug delivered! 💕",
            "Wrapping you up in a big warm blanket hug! 🛋️",
            "Extra soft squeeze to make the aches go away! ✨"
        ]
        messagebox.showinfo("Warm Hug Sent!", random.choice(messages))


if __name__ == "__main__":
    root = tk.Tk()
    app = GetWellSoonApp(root)
    root.mainloop()
