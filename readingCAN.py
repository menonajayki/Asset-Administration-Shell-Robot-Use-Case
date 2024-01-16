import can
import time
import threading
import tkinter as tk
from tkinter import ttk

class CANReader:
    def __init__(self, root):
        self.root = root
        self.root.title("CAN Data Reader")

        self.start_button = ttk.Button(root, text="Start Reading", command=self.start_reading)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(root, text="Stop Reading", command=self.stop_reading)
        self.stop_button.pack(pady=10)
        self.stop_button['state'] = 'disabled'  # Initially, stop button is disabled

        self.text_output = tk.Text(root, height=10, width=50)
        self.text_output.pack(pady=10)

        self.running = False
        self.bus = None

    def start_reading(self):
        self.running = True
        self.start_button['state'] = 'disabled'
        self.stop_button['state'] = 'normal'

        # Start a thread to read CAN data in the background
        self.can_thread = threading.Thread(target=self.read_can_data)
        self.can_thread.start()

    def stop_reading(self):
        self.running = False
        self.start_button['state'] = 'normal'
        self.stop_button['state'] = 'disabled'

    def read_can_data(self):
        try:
            # Set the interface and channel for the entire script
            can.rc['interface'] = 'pcan'
            can.rc['channel'] = 'PCAN_USBBUS1'  # Adjust this based on your specific hardware

            # Specify the bitrate (1 Mbps) and create a Bus instance with the specified configuration
            self.bus = can.interface.Bus(channel='PCAN_USBBUS1', bustype='pcan', bitrate=1000000)

            while self.running:
                message = self.bus.recv()
                display_text = f"Received message: {message}\n"
                self.text_output.insert(tk.END, display_text)
                self.text_output.see(tk.END)  # Scroll to the end
                time.sleep(1)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Make sure to properly shut down the bus
            if self.bus:
                self.bus.shutdown()

# Create the main application window
root = tk.Tk()
app = CANReader(root)

# Start the Tkinter event loop
root.mainloop()