import os
from urllib.parse import urljoin
from datetime import datetime

# 사이트 URL 설정
BASE_URL = "https://yeonkyupark.github.io/"

# 출력 파일
output = "sitemap.xml"

def generate_sitemap():
    urls = []
    for root, dirs, files in os.walk("_site"):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, "_site")
                url = urljoin(BASE_URL, rel_path.replace("\\", "/"))
                urls.append(url)
    
    with open(os.path.join("_site", output), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in urls:
            f.write("  <url>\n")
            f.write(f"    <loc>{url}</loc>\n")
            f.write(f"    <lastmod>{datetime.utcnow().date()}</lastmod>\n")
            f.write("  </url>\n")
        f.write('</urlset>')

if __name__ == "__main__":
    generate_sitemap()
