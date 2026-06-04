from typing import cast

from docutils.nodes import Node
from sphinx.addnodes import versionmodified
from sphinx.domains.changeset import VersionChange, versionlabel_classes, versionlabels
from sphinx.locale import get_translation

from sphinx_deprecated_deleted.const import directive_name, ext_name

_ = get_translation(ext_name)

versionlabels[directive_name] = _("Deprecated since version %s, will be removed in version %s")
versionlabel_classes[directive_name] = "deprecated"


class DeprecatedRemoved(VersionChange):
    required_arguments = 2

    def run(self) -> list[Node]:
        self.arguments = [tuple(self.arguments)]
        nodes = super().run()
        if (type_ := self.config.deprecated_removed_type) is not None:
            cast(versionmodified, nodes[0])["type"] = type_
        return nodes
