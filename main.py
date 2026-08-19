import sys

def main():
    if len(sys.argv) > 1:
        for item in sys.argv[1:]:
            print("ola", item + '!')
    else:
        print("ola")

if __name__ == "__main__":
    main()