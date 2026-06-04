import logging
from pathlib import Path

from babel.messages.mofile import write_mo
from babel.messages.pofile import read_po
from setuptools import Command, setup
from setuptools.command.build import SubCommand, build

log = logging.getLogger()

build.sub_commands.append(("build_mo", None))


class build_mo(Command, SubCommand):
    def initialize_options(self):
        self.build_lib = None

    def finalize_options(self):
        self.get_finalized_command("build_py")
        self.set_undefined_options("build_py", ("editable_mode", "editable_mode"))
        if self.editable_mode:
            self.build_lib = "src"
        self.set_undefined_options("build_py", ("build_lib", "build_lib"))

    @property
    def _build_lib(self) -> Path:
        return Path(self.build_lib)

    def run(self):
        for out, in_ in self._get_output_mapping().items():
            log.info(f"compile {in_} -> {out}")
            out.parent.mkdir(parents=True, exist_ok=True)
            with open(in_, "rb") as f_in, open(out, "wb") as f_out:
                write_mo(f_out, read_po(f_in))

    def get_source_files(self) -> list[str]:
        return list(self.get_output_mapping().values())

    def get_outputs(self) -> list[str]:
        return list(self.get_output_mapping().keys())

    def _get_output_mapping(self) -> dict[Path, Path]:
        name = self.distribution.metadata.name.replace("-", "_")
        d: dict[Path, Path] = {}
        for path in Path("locales").glob("**/*.po"):
            d[self._build_lib / name / path.with_suffix(".mo")] = path
        return d

    def get_output_mapping(self) -> dict[str, str]:
        return {str(key): str(value) for key, value in self._get_output_mapping().items()}


setup(
    cmdclass={"build_mo": build_mo},
)
