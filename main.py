import urllib.request
import threading
import time

URL = "YOUR_INTENDED_WEB_URL"
NUM_THREADS = 10

stop_event = threading.Event()


def testing():
    while not stop_event.is_set():
        try:
            with urllib.request.urlopen(URL, timeout=5) as response:
                print(
                    f"[{threading.current_thread().name}] "
                    f"Status: {response.getcode()}"
                )

        except Exception as e:
            print(
                f"[{threading.current_thread().name}] "
                f"Error: {e}"
            )

        time.sleep(0.5)


def main():
    threads = []

    for i in range(NUM_THREADS):
        thread = threading.Thread(
            target=testing,
            name=f"Worker-{i + 1}",
            daemon=True
        )
        thread.start()
        threads.append(thread)

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Stopping threads...")

        stop_event.set()

        for thread in threads:
            thread.join(timeout=2)

        print("All threads stopped.")


if __name__ == "__main__":
    main()
