# One of None Trading — Flask Website

Full rebuild of oneofnonetrading.com using Python (Flask) + HTML + CSS.

---

## Project Structure

```
oneofnone-flask/
├── app.py                  # Flask application — all routes defined here
├── templates/
│   ├── base.html           # Base template — nav, footer, shared head
│   ├── home.html           # Homepage
│   ├── models.html         # Models page
│   ├── series.html         # Series page
│   ├── roadmap.html        # Roadmap page
│   └── community.html      # Community page
├── static/
│   ├── css/
│   │   └── style.css       # Complete design system — all shared styles
│   └── js/
│       └── main.js         # Minimal JS
└── README.md
```

---

## Local Setup

### 1. Install Python
Download from https://python.org if not already installed. Python 3.8+ required.

### 2. Install Flask
Open terminal and run:
```bash
pip install flask
```

### 3. Run the development server
Navigate to the project folder in terminal:
```bash
cd oneofnone-flask
python app.py
```

Open your browser and go to:
```
http://localhost:5000
```

---

## Deploying to a Live Server

### Option A — PythonAnywhere (Recommended, Free Tier Available)

1. Go to https://www.pythonanywhere.com and create a free account
2. Go to the **Files** tab and upload your project folder
3. Go to the **Web** tab and click **Add a new web app**
4. Select **Flask** as the framework
5. Set the source code path to your uploaded folder
6. Set the WSGI file path — PythonAnywhere provides a template, update it to point to your `app.py`
7. Click **Reload** — your site is live

### Option B — Railway (Simple, Free Tier Available)

1. Go to https://railway.app
2. Connect your GitHub account
3. Push your project to a GitHub repo
4. Import the repo into Railway
5. Railway auto-detects Flask — add a `Procfile` with:
   ```
   web: python app.py
   ```
6. Set the PORT environment variable if needed
7. Deploy — done

### Option C — VPS (Full Control)

Any VPS (DigitalOcean, Linode, Vultr) running Ubuntu:
```bash
pip install flask gunicorn
gunicorn -w 4 app:app
```
Use Nginx as a reverse proxy and Certbot for SSL.

---

## Connecting Your Domain

Regardless of host:
1. Add your domain in your hosting provider's settings
2. Update DNS records at your domain registrar:
   - A record pointing to your server IP
   - CNAME for www pointing to your domain
3. Wait up to 48 hours for DNS propagation

---

## Updating Content

### Adding a new episode to the Series page
Open `templates/series.html` and find the `episodes` list inside the Jinja2 template. Add a new tuple:
```
("09", "Episode Title", "Short description.", "live", "https://youtube.com/...", "https://yoursite.com/episode9"),
```

### Updating Model stats
Open `templates/models.html` and update the stats in the stats-bar section.

### Adding live results
Find the Live Results section in `templates/models.html` and replace the placeholder block with actual data.

### Updating the Roadmap
Open `templates/roadmap.html` and update the `phases` list — change status from `upcoming` to `active` or `complete` as milestones are reached.

---

## Design System

All design tokens are CSS variables in `static/css/style.css`:

| Variable | Value | Use |
|---|---|---|
| `--accent` | `#00aaff` | Blue — links, highlights, labels |
| `--green` | `#00cc88` | Live status, positive indicators |
| `--amber` | `#f5a623` | In-progress, warnings |
| `--bg-0` | `#060809` | Primary background |
| `--mono` | IBM Plex Mono | All headings, labels, code |
| `--sans` | IBM Plex Sans | Body text |
