from time import sleep
from progress_ticker import progress_ticker

@progress_ticker()
def main():
    sleep(5)

if __name__ == '__main__':
    main()
