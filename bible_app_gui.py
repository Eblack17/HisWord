import customtkinter as ctk
from ai_agents import get_biblical_guidance
import threading
import tkinter as tk
from tkinter import scrolledtext
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BibleAppGUI:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Bible Verse Finder")
        self.window.geometry("800x600")
        
        # Set the theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Input frame
        self.input_frame = ctk.CTkFrame(self.window)
        self.input_frame.pack(padx=20, pady=20, fill="x")
        
        # Input label
        self.input_label = ctk.CTkLabel(
            self.input_frame,
            text="Enter your situation or question:",
            font=("Helvetica", 14)
        )
        self.input_label.pack(pady=5)
        
        # Input text box
        self.input_text = ctk.CTkTextbox(
            self.input_frame,
            height=100,
            font=("Helvetica", 12)
        )
        self.input_text.pack(padx=20, pady=5, fill="x")
        
        # Submit button
        self.submit_button = ctk.CTkButton(
            self.input_frame,
            text="Get Guidance",
            command=self.get_guidance
        )
        self.submit_button.pack(pady=10)
        
        # Output frame
        self.output_frame = ctk.CTkFrame(self.window)
        self.output_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Output text
        self.output_text = scrolledtext.ScrolledText(
            self.output_frame,
            height=20,
            font=("Helvetica", 12),
            wrap=tk.WORD
        )
        self.output_text.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Status label
        self.status_label = ctk.CTkLabel(
            self.window,
            text="",
            font=("Helvetica", 12)
        )
        self.status_label.pack(pady=5)
    
    def get_guidance(self):
        # Get input text
        input_text = self.input_text.get("1.0", "end-1c").strip()
        if not input_text:
            self.status_label.configure(text="Please enter a question or situation")
            return
        
        # Clear previous output
        self.output_text.delete("1.0", "end")
        
        # Update status and disable button
        self.status_label.configure(text="Getting guidance... Please wait...")
        self.submit_button.configure(state="disabled")
        
        def process():
            try:
                # Get guidance
                logger.info(f"Getting guidance for: {input_text}")
                result = get_biblical_guidance(input_text)
                logger.info("Received guidance result")
                
                # Update GUI
                self.window.after(0, lambda: self.show_result(result))
            except Exception as e:
                logger.error(f"Error getting guidance: {str(e)}")
                self.window.after(0, lambda: self.show_error(str(e)))
        
        # Run in background
        threading.Thread(target=process, daemon=True).start()
    
    def show_result(self, result):
        try:
            # Format and display the result, showing only the guidance
            output = f"""{result['guidance']}"""
            
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", output)
            
            # Reset status
            self.status_label.configure(text="")
            self.submit_button.configure(state="normal")
            
            logger.info("Successfully displayed result")
        except Exception as e:
            logger.error(f"Error showing result: {str(e)}")
            self.show_error(str(e))
    
    def show_error(self, error):
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", f"Error: {error}\n\nPlease try again.")
        self.status_label.configure(text="")
        self.submit_button.configure(state="normal")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = BibleAppGUI()
    app.run()
