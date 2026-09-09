"""Custom nbconvert exporter for the CCSF JupyterHub image.

JupyterLab 4.6+ shows a "Sanitize HTML output" prompt whenever a user
exports a notebook using the built-in "html" format and the server's
jupyter_server version supports it (see notebook-extension's
exportToFormat command: the dialog only fires when the requested
format is literally "html").

This module registers a second exporter, "html_embed", that always
embeds images (markdown images, raw <img> tags, and cell-output
figures) as base64 data URIs and is never routed through that dialog,
since its format id isn't "html". The File menu's "Download HTML" item
(see overrides.json) is pointed at this format so the export stays a
single click, same as before JupyterLab 4.6.
"""

from nbconvert.exporters.html import HTMLExporter


class EmbeddedHTMLExporter(HTMLExporter):
    """HTML export with local images and attachments embedded."""

    # Label shown in "File > Save and Export Notebook As", if ever enabled.
    export_from_notebook = "HTML (images embedded)"

    def _embed_images_default(self):
        return True
