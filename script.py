from datetime import datetime

def main():
    print("Hello, World!")
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", current_time)

if __name__ == "__main__":
    main()
