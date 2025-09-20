import speedtest
import threading
from plyer import notification
import pystray
from PIL import Image, ImageDraw

def run_speed_test(icon, item):
    def test():
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            download_speed = st.download() / 1024 / 1024
            upload_speed = st.upload() / 1024 / 1024
            ping = st.results.ping

            result = (
                f"Download: {download_speed:.2f} Mbps\n"
                f"Upload: {upload_speed:.2f} Mbps\n"
                f"Ping: {ping:.2f} ms"
            )

            # Show result in Windows notification
            notification.notify(
                title="Internet Speed Test",
                message=result,
                timeout=10  # seconds
            )
        except Exception as e:
            notification.notify(
                title="Speed Test Error",
                message=str(e),
                timeout=10
            )

    threading.Thread(target=test).start()

def create_image():
    # make simple tray icon
    img = Image.new("RGB", (64, 64), (0, 128, 255))
    d = ImageDraw.Draw(img)
    d.rectangle([16, 16, 48, 48], fill=(255, 255, 255))
    return img

# Create tray icon with menu
icon = pystray.Icon(
    "NetSpeedTester",
    create_image(),
    menu=pystray.Menu(
        pystray.MenuItem("Run Speed Test", run_speed_test),
        pystray.MenuItem("Quit", lambda icon, item: icon.stop())
    )
)

icon.run()
