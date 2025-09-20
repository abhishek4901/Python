import tkinter as tk
import speedtest
import threading

def run_speed_test():
    result_label.config(text="Finding best server...\n")
    
    def test():
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            
            result_label.config(text="Testing download speed...\n")
            download_speed = st.download() / 1024 / 1024

            result_label.config(text="Testing upload speed...\n")
            upload_speed = st.upload() / 1024 / 1024

            ping = st.results.ping

            output = (
                "------ Internet Speed Test Results ------\n"
                f"Download Speed: {download_speed:.2f} Mbps\n"
                f"Upload Speed:   {upload_speed:.2f} Mbps\n"
                f"Ping:           {ping:.2f} ms"
            )
            result_label.config(text=output)
        except Exception as e:
            result_label.config(text=f"Error: {e}")

    # run in separate thread so UI doesn’t freeze
    threading.Thread(target=test).start()

# Create window
root = tk.Tk()
root.title("Net Speed Tester")

# Set small size and place bottom-left
root.geometry("350x200+0+600")  # width x height + X + Y (adjust Y to your screen height)
root.resizable(False, False)

# Button
button = tk.Button(root, text="Run Speed Test", command=run_speed_test)
button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Click 'Run Speed Test' to begin", justify="left", anchor="w")
result_label.pack(padx=10, pady=10, fill="both")

# Start GUI
root.mainloop()
# Save as python NetSpeedTesterGUI.py and run with python NetSpeedTesterGUI.py
