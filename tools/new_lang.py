import sys
from subprocess import run

from _tools_init import chdir

from sphinx_deprecated_deleted.const import ext_name, locales_dir


def main():
    with chdir:
        locales = map(lambda lang: f"--locale={lang}", sys.argv[1:])

        run(
            [
                "pybabel",
                "init",
                f"--input-file={locales_dir}/{ext_name}.pot",
                f"--domain={ext_name}",
                f"--output-dir={locales_dir}",
                *locales,
            ]
        )


if __name__ == "__main__":
    main()
