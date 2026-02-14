# Store in ~/.jupyter/ for user nbconvert configuration
# Store in /srv/conda/envs/notebook/etc/jupyter for system-wide nbconvert configuration

c = get_config()

# Enable embedding images in exported HTML files
c.HTMLExporter.embed_images = True

# Better terminal defaults
c.ServerApp.terminado_settings = {'shell_command': ['/bin/bash']}

# Disable Python syntax highlighting in markdown cells
c.MarkdownCell.cm_config = {'mode': 'gfm'}  # GitHub Flavored Markdown
