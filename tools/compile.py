from pathlib import Path
from subprocess import run

from _tools_init import chdir

from sphinx_deprecated_deleted.const import ext_name, locales_dir


def main():
    with chdir:
        run(["pybabel", "compile", f"--directory={locales_dir}", f"--domain={ext_name}"])

        locales_in = Path(locales_dir)
        locales_out = Path("src") / ext_name / locales_dir

        for file_in in locales_in.glob("**/*.mo"):
            file_out = locales_out / file_in.relative_to(locales_in)
            file_out.parent.mkdir(parents=True, exist_ok=True)
            file_in.move(file_out)


if __name__ == "__main__":
    main()
