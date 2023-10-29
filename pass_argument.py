import argparse

def main(args):
    if args.clean:
        print("Cleaning is enabled.")
    else:
        print("Cleaning is not enabled.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='My Python Script')
    parser.add_argument('--clean', action='store_true', help='Enable cleaning')

    args = parser.parse_args()
    main(args)