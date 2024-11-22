import time

def main():
    while True:
        # Replace this with your task logic
        print("Task running...")
        with open("../logs/job_output.log", "a") as log_file:
            log_file.write(f"Task executed at {time.ctime()}\n")
        time.sleep(10)

if __name__ == "__main__":
    main()
