from importlib.metadata import version
from pathlib import Path
from typing import Any

from sphinx.application import Sphinx

from sphinx_deprecated_deleted.const import directive_name, ext_name, locales_dir
from sphinx_deprecated_deleted.directive import DeprecatedRemoved


def setup(app: Sphinx) -> dict[str, Any]:
    locale_dir = Path(__file__).resolve().parent / locales_dir
    app.add_message_catalog(ext_name, locale_dir)
    app.add_directive(directive_name, DeprecatedRemoved)
    app.add_config_value("deprecated_removed_type", None, "env")
    return {
        "version": version(ext_name),
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
