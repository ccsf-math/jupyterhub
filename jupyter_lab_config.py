# Store in ~/.jupyter/ for user nbconvert configuration
# Store in /srv/conda/envs/notebook/etc/jupyter for system-wide nbconvert configuration

c = get_config()

# Enable embedding images in exported HTML files
c.HTMLExporter.embed_images = True

# Increase data rate limits for large outputs (plots, dataframes)
c.ServerApp.iopub_data_rate_limit = 10000000
c.ServerApp.iopub_msg_rate_limit = 10000

# Better terminal defaults
c.ServerApp.terminado_settings = {'shell_command': ['/bin/bash']}
