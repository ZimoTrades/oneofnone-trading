from flask import Flask, render_template, Response
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/models')
def models():
    return render_template('models.html')

@app.route('/series')
def series():
    return render_template('series.html')

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/episode/<ep_id>')
def episode(ep_id):
    valid_episodes = ['01', '02', '03', '04', '05', '06', '07', '08']
    if ep_id not in valid_episodes:
        return "Episode not found", 404
    return render_template(f'episodes/episode_{ep_id}.html')

@app.route('/sitemap.xml')
def sitemap():
    pages = [
        ('https://www.oneofnonetrading.com/', '1.0', 'weekly'),
        ('https://www.oneofnonetrading.com/models', '0.9', 'weekly'),
        ('https://www.oneofnonetrading.com/series', '0.9', 'weekly'),
        ('https://www.oneofnonetrading.com/roadmap', '0.8', 'monthly'),
        ('https://www.oneofnonetrading.com/community', '0.8', 'monthly'),
        ('https://www.oneofnonetrading.com/episode/01', '0.7', 'monthly'),
        ('https://www.oneofnonetrading.com/episode/02', '0.7', 'monthly'),
        ('https://www.oneofnonetrading.com/episode/03', '0.7', 'monthly'),
        ('https://www.oneofnonetrading.com/episode/04', '0.7', 'monthly'),
        ('https://www.oneofnonetrading.com/episode/05', '0.7', 'monthly'),
        ('https://www.oneofnonetrading.com/episode/06', '0.7', 'monthly'),
        ('https://www.oneofnonetrading.com/episode/07', '0.7', 'monthly'),
        ('https://www.oneofnonetrading.com/episode/08', '0.7', 'monthly'),
    ]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url, priority, freq in pages:
        xml += f'  <url>\n'
        xml += f'    <loc>{url}</loc>\n'
        xml += f'    <changefreq>{freq}</changefreq>\n'
        xml += f'    <priority>{priority}</priority>\n'
        xml += f'  </url>\n'
    xml += '</urlset>'
    return Response(xml, mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    content = "User-agent: *\nAllow: /\nSitemap: https://www.oneofnonetrading.com/sitemap.xml"
    return Response(content, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
