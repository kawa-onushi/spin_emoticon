import sys
import time


def wait_job_finish():
    spin = ["(´･ω･`)", "( ´･ω･)", "(  ´･ω)", "(   ´･)", "(    ´)",
            "(     )", "(´    )", "(･´   )", "(ω･´  )", "(･ω･´ )", "(`･ω･´)"]

    spinner = 0
    print("Please wait for the job to finish.")
    count = 0
    while (count < 100):
        sys.stdout.write("\r " + spin[spinner % len(spin)])
        sys.stdout.flush()
        spinner += 1
        count += 1
        time.sleep(1)
    return


def main():
    wait_job_finish()
    return


if __name__ == "__main__":
    main()
