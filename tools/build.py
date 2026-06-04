import sys
from subprocess import run

from _tools_init import chdir
from compile import main as compile_main


def main():
    with chdir:
        compile_main()
        run([sys.executable, "-m", "build", *sys.argv[1:]])


if __name__ == "__main__":
    main()
