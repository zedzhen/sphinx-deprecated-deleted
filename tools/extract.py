from subprocess import run

from _tools_init import base_dir, chdir

from sphinx_deprecated_deleted.const import ext_name, locales_dir


def main():
    with chdir:
        (base_dir / locales_dir).mkdir(parents=True, exist_ok=True)

        run(["pybabel", "extract", f"--output={locales_dir}/{ext_name}.pot", "src/"])
        run(
            [
                "pybabel",
                "update",
                f"--input-file={locales_dir}/{ext_name}.pot",
                f"--domain={ext_name}",
                f"--output-dir={locales_dir}",
            ]
        )


if __name__ == "__main__":
    main()
