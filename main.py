import sys

def main():
    if len(sys.argv) > 1:
        print("ola,", sys.argv[1] + '!')
    else:
        print("Ola mundo")

if __name__ == "__main__":
    main()