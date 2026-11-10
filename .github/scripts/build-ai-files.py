#!/usr/bin/env python3
"""Regenerate sitemap-main.xml lastmod dates and llms-full.txt.

Usage: build-ai-files.py <site_root> [<repo_root>]

  site_root  directory whose sitemap-main.xml and llms-full.txt get (over)written
  repo_root  git checkout used for last-modified dates and blog markdown
             (defaults to site_root)

Needs full git history (actions/checkout fetch-depth: 0) so lastmod is real.
"""
import re, subprocess, sys
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://fleetagentic.ai"
site = Path(sys.argv[1]).resolve()
repo = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else site

PAGES = [  # (url path, source file)
    ("/", "index.html"),
    ("/solutions/legal/", "solutions/legal/index.html"),
    ("/solutions/healthcare/", "solutions/healthcare/index.html"),
    ("/solutions/defense/", "solutions/defense/index.html"),
    ("/carrier/", "carrier/index.html"),
    ("/learn/the-index-is-the-leak/", "learn/the-index-is-the-leak/index.html"),
    ("/case-studies/", "case-studies/index.html"),
    ("/case-studies/defense-cmmc/", "case-studies/defense-cmmc/index.html"),
]

def git_date(path):
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(path)],
                         cwd=repo, capture_output=True, text=True).stdout.strip()
    return out

# ---- sitemap-main.xml -------------------------------------------------------
urls = []
for url, src in PAGES:
    d = git_date(src) or "2026-11-10"
    urls.append(f"  <url><loc>{BASE}{url}</loc><lastmod>{d}</lastmod></url>")
(site / "sitemap-main.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(urls) + "\n</urlset>\n")

# ---- llms-full.txt ----------------------------------------------------------
SKIP = {"script", "style", "nav", "header", "footer", "svg", "noscript", "form", "button", "head"}
BLOCK = {"h1", "h2", "h3", "h4", "p", "li", "summary", "dt", "dd", "tr", "blockquote"}

class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.buf, self.skip, self.tag = [], [], 0, None
    def handle_starttag(self, t, a):
        if t in SKIP: self.skip += 1
        elif t in BLOCK: self.flush(); self.tag = t
    def handle_endtag(self, t):
        if t in SKIP: self.skip = max(0, self.skip - 1)
        elif t in BLOCK: self.flush()
    def handle_data(self, d):
        if not self.skip: self.buf.append(d)
    def flush(self):
        text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        self.buf = []
        if not text: return
        pre = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "li": "- ", "summary": "### "}.get(self.tag, "")
        line = pre + text
        if not self.out or self.out[-1] != line: self.out.append(line)

def page_text(src):
    html = (repo / src).read_text()
    p = Text(); p.feed(html); p.flush()
    return "\n\n".join(p.out)

doc = [
    "# Fleet Agentic — full site text",
    "",
    "> Fleet Agentic (formerly DPLYD; legal entity DPLYD, Inc.) is fully managed private AI and AI agent teams deployed inside a customer's own network, from hardware to full platform, for regulated industries. This file concatenates the text of every public page for LLM ingestion. Index and key facts: " + BASE + "/llms.txt",
    "",
]
for url, src in PAGES:
    doc += ["---", "", f"Source: {BASE}{url}  (last modified {git_date(src)})", "", page_text(src), ""]

for md in sorted((repo / "_blog/content").glob("*.md")):
    if md.name.startswith("_"): continue
    raw = md.read_text()
    m = re.match(r"---\n(.*?)\n---\n(.*)", raw, re.S)
    if not m: continue
    fm, body = m.groups()
    if re.search(r"^draft:\s*true", fm, re.M): continue
    title = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.M).group(1)
    slug = (re.search(r'^slug:\s*"?(.*?)"?\s*$', fm, re.M) or [None, md.stem])[1]
    date = re.search(r"^date:\s*(\S+)", fm, re.M).group(1)[:10]
    doc += ["---", "", f"Source: {BASE}/blog/{slug}/  (published {date})", "", f"# {title}", "", body.strip(), ""]

(site / "llms-full.txt").write_text("\n".join(doc))
print("wrote sitemap-main.xml and llms-full.txt")
