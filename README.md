# CCSF JupyterHub

The configuration for the [2i2c](https://2i2c.org/) and [Cloudbank](https://www.cloudbank.org/) supported [JupyterHub at CCSF](https://ccsf.cloudbank.2i2c.cloud/).

- Access the hub using your [CCSFmail](https://www.ccsf.edu/about-ccsf/administration/finance-and-administration/information-technology-services/ccsfmail-faq-students) @mail.ccsf.edu Google account sign in credentials.
- You can use the Docker image `quay.io/ccsf/jupyterhub` to recreate the hub environment.
  - The current tag is `fa26.1`
  - You can fetch that tag with docker using the command `docker pull quay.io/ccsf/jupyterhub:fa26.1`
- Contact the Shawn Wiggins swiggins@ccsf.edu for support.

## Relevant Documentation

- [repo2docker Documentation](https://repo2docker.readthedocs.io/en/latest/)
- [2i2c Infrastructure Documentation](https://infrastructure.2i2c.org/en/latest/)
- [UC Berkeley's DataHub Repo - DATA 8 Focus](https://github.com/berkeley-dsep-infra/datahub)

## Replicate the Fall 2026 Hub Environment Locally

> **Note on what you are running.** This image starts a **single-user JupyterLab** server, not a JupyterHub. It is the same software environment the hub gives you, running locally for one person, with no login page. You reach it with a token URL instead of your CCSFmail account.

### Step 1 — Install Docker Desktop

1. Download [Docker Desktop](https://www.docker.com/products/docker-desktop/) for your operating system.
2. Run the installer and follow the prompts. On Mac, drag Docker to your Applications folder. On Windows, accept the default options.
3. Launch Docker Desktop. Wait until the whale icon in your menu bar/taskbar is **steady** (not animated) — this means Docker is running.

> ⚠️ Docker must be running in the background for all steps below.

**Using a Mac with an Apple Silicon chip (M1, M2, M3, M4)?** Do [Step 1a](#step-1a--extra-setup-for-apple-silicon-macs) before going any further, or the container will not start correctly.

---

### Step 1a — Extra Setup for Apple Silicon Macs

This image is built for `linux/amd64` (Intel/AMD) only. repo2docker builds for a single architecture and our GitHub Actions runner is x86_64, so there is no ARM build of this image. Apple Silicon Macs run it under emulation. That works, but two Docker Desktop settings have to be correct first.

#### 1. Turn off Rosetta emulation

**Docker Desktop → Settings → General →** uncheck **"Use Rosetta for x86_64/amd64 emulation on Apple Silicon" → Apply & Restart.**

Rosetta is the faster emulator, but it mis-handles some of the CPU instructions used by the numerical libraries in this image (OpenBLAS behind NumPy/SciPy, and PyTorch). With Rosetta on, the container typically dies within seconds of starting. With it off, Docker falls back to QEMU, which is slower but runs the whole stack correctly.

#### 2. Raise the memory and disk limits

**Docker Desktop → Settings → Resources:**

- **Memory:** 8 GB or more
- **Disk image size:** 40 GB or more

The compressed download is a few GB, but the unpacked image is much larger: the full TeX Live install, PyTorch, R, and VS Code layers add up quickly.

#### 3. Always pass `--platform linux/amd64`

Use the terminal rather than the Docker Desktop UI on Apple Silicon, since the UI gives you no way to pin the platform:

```bash
docker run --platform linux/amd64 -p 8888:8888 quay.io/ccsf/jupyterhub:fa26.1
```

#### What to expect

Emulation is slow. Budget 1–3 minutes between running the command and seeing the token URL, and expect notebook cells to run noticeably slower than they do on the hub. This is the cost of running an x86 image on an ARM chip. If you mainly need speed, use [the hub itself](https://ccsf.cloudbank.2i2c.cloud/), which runs on native x86 hardware.

---

### Step 2 — Pull the Image

1. Open a terminal:
   - **Mac:** Spotlight Search → `Terminal`
   - **Windows:** Search → `PowerShell` or `Command Prompt`
   - **Linux:** Any terminal emulator

2. Run the following command to download the course image (several GB, may take a while):

```bash
docker pull quay.io/ccsf/jupyterhub:fa26.1
```

On Apple Silicon, add the platform flag:

```bash
docker pull --platform linux/amd64 quay.io/ccsf/jupyterhub:fa26.1
```

3. Wait until you see `Status: Downloaded newer image for quay.io/ccsf/jupyterhub:fa26.1` before proceeding.

---

### Step 3 — Run the Container

#### Option A — Using the Terminal (recommended, and required on Apple Silicon)

```bash
docker run -p 8888:8888 quay.io/ccsf/jupyterhub:fa26.1
```

On Apple Silicon:

```bash
docker run --platform linux/amd64 -p 8888:8888 quay.io/ccsf/jupyterhub:fa26.1
```

To keep your work after the container stops, mount a folder from your computer into the container:

```bash
docker run -p 8888:8888 -v "$PWD":/home/jovyan/work -w /home/jovyan \
  quay.io/ccsf/jupyterhub:fa26.1
```

Anything you save into the `work` folder in JupyterLab will appear in the folder you launched from. Without this, files are lost when the container is removed. The `-w /home/jovyan` flag makes JupyterLab open in the home directory, matching what you see on the hub; the image otherwise starts in `/srv/repo`, where the repository contents live.

#### Option B — Using Docker Desktop's UI (Intel Macs, Windows, Linux)

1. Open Docker Desktop and click the **Images** tab in the left sidebar.
2. Find `quay.io/ccsf/jupyterhub` with the `fa26.1` tag and click **Run**.
3. Expand **Optional Settings** and set:
   - **Host port:** `8888`
   - **Container port:** `8888`
4. Click **Run**.

---

### Step 4 — Open JupyterLab in Your Browser

1. In your terminal (or in Docker Desktop → **Containers** → select your container → **Logs** tab), look for a line like:

```
http://127.0.0.1:8888/lab?token=abc123...
```

2. Copy the **full URL including the token** and paste it into your browser. Alternatively, **Ctrl+Click** (or **Cmd+Click** on Mac) the link directly in the terminal.

3. JupyterLab should open in your browser and be ready to use.

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
| `no matching manifest for linux/arm64/v8` | Apple Silicon Mac. Add `--platform linux/amd64` to your `docker pull` and `docker run` commands |
| Container exits immediately on an Apple Silicon Mac | Turn off Rosetta emulation. See [Step 1a](#step-1a--extra-setup-for-apple-silicon-macs) |
| `illegal instruction`, `Fatal glibc error`, or a segfault on an Apple Silicon Mac | Same cause: Rosetta. Turn it off in Docker Desktop → Settings → General, then Apply & Restart |
| Container is killed partway through startup | Raise Docker's memory limit to 8 GB or more in Settings → Resources |
| `no space left on device` during pull | Raise Docker's disk image size in Settings → Resources, or run `docker system prune -a` to clear old images |
| Everything runs, but very slowly, on an Apple Silicon Mac | Expected under emulation. Use the [hosted hub](https://ccsf.cloudbank.2i2c.cloud/) for heavier work |

#### Collecting details for a bug report

If none of the above helps, run these and include the output when you email for support:

```bash
docker version --format 'client={{.Client.Arch}} server={{.Server.Arch}}'
docker run --rm --platform linux/amd64 quay.io/ccsf/jupyterhub:fa26.1 \
  python -c "import numpy, torch; print(numpy.__version__, torch.__version__)"
```

If the second command crashes rather than printing two version numbers, the emulation layer is the problem, not your notebook.
