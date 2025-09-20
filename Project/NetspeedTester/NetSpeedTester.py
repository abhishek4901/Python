import speedtest

def test_speed():
    print("Finding best server...\n")
    st = speedtest.Speedtest()

    st.get_best_server()

    print("Testing download speed...")
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps

    print("Testing upload speed...")
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps

    ping = st.results.ping

    print("\n------ Internet Speed Test Results ------")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed:   {upload_speed:.2f} Mbps")
    print(f"Ping:           {ping:.2f} ms")

if __name__ == "__main__":
    test_speed()
