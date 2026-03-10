# CCSF JupyterHub

The configuration for the [2i2c](https://2i2c.org/) and [Cloudbank](https://www.cloudbank.org/) supported [JupyterHub at CCSF](https://ccsf.cloudbank.2i2c.cloud/).

- Access the hub using your [CCSFmail](https://www.ccsf.edu/about-ccsf/administration/finance-and-administration/information-technology-services/ccsfmail-faq-students) @mail.ccsf.edu Google account sign in credentials.
- You can use the Docker image `quay.io/ccsf/jupyterhub` to recreate the hub environment.
  - The current tag is `sp26.3`
  - You can fetch that tag with docker using the command `docker pull quay.io/ccsf/jupyterhub:sp26.3`
- Contact the Shawn Wiggins swiggins@ccsf.edu for support.

## Relevant Documentation

- [repo2docker Documentation](https://repo2docker.readthedocs.io/en/latest/)
- [2i2c Infrastructure Documentation](https://infrastructure.2i2c.org/en/latest/)
- [UC Berkeley's DataHub Repo - DATA 8 Focus](https://github.com/berkeley-dsep-infra/datahub)

## Replicate Fall 2025 JupyterHub Environment

Currently, these instructions do not seem to be working with computers running the newer Apple Silicon chips.

### Step 1 — Install Docker Desktop

1. Download [Docker Desktop](https://www.docker.com/products/docker-desktop/) for your operating system.
2. Run the installer and follow the prompts. On Mac, drag Docker to your Applications folder. On Windows, accept the default options.
3. Launch Docker Desktop. Wait until the whale icon in your menu bar/taskbar is **steady** (not animated) — this means Docker is running.

> ⚠️ Docker must be running in the background for all steps below.

---

### Step 2 — Pull the JupyterHub Image

1. Open a terminal:
   - **Mac:** Spotlight Search → `Terminal`
   - **Windows:** Search → `PowerShell` or `Command Prompt`
   - **Linux:** Any terminal emulator

2. Run the following command to download the course image (~2–4 GB, may take several minutes):

```bash
docker pull quay.io/ccsf/jupyterhub:fa25
```

3. Wait until you see `Status: Downloaded newer image for quay.io/ccsf/jupyterhub:fa25` before proceeding.

---

### Step 3 — Run the Container

#### Option A — Using the Terminal (recommended)

```bash
docker run -p 8888:8888 quay.io/ccsf/jupyterhub:fa25
```

#### Option B — Using Docker Desktop's UI

1. Open Docker Desktop and click the **Images** tab in the left sidebar.
2. Find `quay.io/ccsf/jupyterhub` with the `fa25` tag and click **Run**.
3. Expand **Optional Settings** and set:
   - **Host port:** `8888`
   - **Container port:** `8888`
4. Click **Run**.

---

### Step 4 — Open JupyterHub in Your Browser

1. In your terminal (or in Docker Desktop → **Containers** → select your container → **Logs** tab), look for a line like:

```
http://127.0.0.1:8888/lab?token=abc123...
```

2. Copy the **full URL including the token** and paste it into your browser. Alternatively, **Ctrl+Click** (or **Cmd+Click** on Mac) the link directly in the terminal.

3. JupyterHub should open in your browser and be ready to use.

---

### Stopping and Restarting

- **Stop:** Press `Ctrl+C` in the terminal, or click **Stop** in Docker Desktop.
- **Restart later:** In Docker Desktop, go to **Containers**, find your container, and click **Start**. Then revisit the Logs tab for the new token URL.

---

### Troubleshooting

| Problem | Solution |
|---|---|
| Port 8888 already in use | Change host port to `8889`: use `-p 8889:8888` in the run command, then visit `http://127.0.0.1:8889/...` |
| "Cannot connect" in browser | Make sure the container is still running and you're using the full URL with token |
| Token URL not visible in logs | Scroll up in the Logs tab — it appears near startup |
| Docker command not found | Restart your terminal after installing Docker Desktop |
