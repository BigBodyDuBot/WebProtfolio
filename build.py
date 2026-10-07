"""Rebuild static HTML from projects.json. Python 3, standard library only."""
from pathlib import Path
from html import escape as e
import json, re

ROOT=Path(__file__).resolve().parent
projects=json.loads((ROOT/'projects.json').read_text(encoding='utf-8'))
REPO='https://github.com/BigBodyDuBot/WebProtfolio'
def page(title,body,prefix='',script=False,description='Duy Hoang’s named academic projects in software, data and cybersecurity.'):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} | Duy Hoang</title><meta name="description" content="{e(description)}"><meta name="theme-color" content="#183c34"><link rel="stylesheet" href="{prefix}styles.css">{('<script src="app.js" defer></script>' if script else '')}</head><body><a class="skip" href="#main">Skip to content</a><div class="wrap"><header><a class="brand" href="{prefix}index.html"><span>DH</span>Duy Hoang</a><nav aria-label="Main navigation"><a href="{prefix}index.html#projects">Projects</a><a href="{prefix}index.html#about">About</a><a href="{REPO}">GitHub ↗</a></nav></header><main id="main">{body}</main><footer><span>Duy Hoang · Academic portfolio</span><span>Montclair State University · Expected December 2026</span></footer></div></body></html>'''

def size(n):return f'{n/1024/1024:.1f} MB' if n>=1048576 else f'{max(1,round(n/1024))} KB'
source_ext={'C','CPP','CS','JAVA','PY','S','PL','RKT','TXT','IPYNB'}
def source_view(p,r):
    path=ROOT/r['path']; view=Path('source')/p['id']/(path.name+'.html')
    text=path.read_text(encoding='utf-8',errors='replace')
    if r['format']=='IPYNB':
        nb=json.loads(text); parts=[]
        for i,cell in enumerate(nb.get('cells',[]),1):
            value=''.join(cell.get('source',[]))
            if not value.strip():continue
            parts.append(f'<h2>Cell {i} · {e(cell.get("cell_type",""))}</h2><pre class="code">{e(value)}</pre>')
        content='<p class="file-intro">Notebook source cells are shown below. Download the original notebook for saved outputs and attachments.</p>'+''.join(parts)
    else:content=f'<pre class="code">{e(text)}</pre>'
    body=f'<a class="back" href="../../projects/{p["id"]}.html">← Back to project</a><h1 class="source-title">{e(r["name"])}</h1><a class="download" href="../../{r["path"]}" download>Download original · {e(r["format"])}</a>{content}'
    dest=ROOT/view;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(page(r['name'],body,'../../'),encoding='utf-8')
    return '../'+view.as_posix()

def resource(p,r):
    fmt=r['format'];href='../'+r['path'];action='Open report' if fmt=='PDF' else 'Download original'
    if fmt in source_ext:href=source_view(p,r);action='Read source'
    download=' download' if action=='Download original' else ''
    label=r.get('label') or re.sub(r'[_]+',' ',Path(r['name']).stem).strip()
    if label.isupper():label=label.capitalize()
    return f'<a class="resource" href="{href}"{download} title="{e(r["name"])}"><span class="file-name">{e(label)}</span><span class="file-meta">{action} ↗ &nbsp;·&nbsp; {e(fmt)} &nbsp;·&nbsp; {size(r["bytes"])}</span></a>'

cards=[]
for n,p in enumerate(projects,1):
    tags=''.join(f'<span>{e(t)}</span>' for t in p['tags'])
    search=e(' '.join([p['title'],p['category'],p['summary'],p['did']]+p['tags']).lower(),quote=True)
    cards.append(f'<article class="card" data-category="{p["category"]}" data-search="{search}"><div class="meta"><span>{p["category"]}</span><span>{n:02d}</span></div><h3><a href="projects/{p["id"]}.html">{e(p["title"])}</a></h3><p>{e(p["summary"])}</p><div class="tags">{tags}</div><div class="bottom"><span>{len(p["resources"])} project files</span><span class="arrow" aria-hidden="true">↗</span></div></article>')
    resources=[resource(p,r) for r in p['resources']]
    extra=f'<details><summary>More files &amp; earlier versions ({len(resources)-3})</summary>{"".join(resources[3:])}</details>' if len(resources)>3 else ''
    note=f'<div class="notice"><strong>About this coursework</strong><br>{e(p["note"])}</div>' if p['note'] else ''
    credit=f'<p class="credit">{e(p["credit"])}</p>' if p['credit'] else ''
    body=f'''<a class="back" href="../index.html?category={p['category']}#projects">← All {p['category'].lower()} projects</a><div class="project-hero"><div class="eyebrow">{p['category']} / Academic project {n:02d}</div><h1>{e(p['title'])}</h1><p class="intro">{e(p['summary'])}</p><div class="pills">{tags}</div></div><div class="project-body"><div class="story"><section><h2>What I did</h2><p>{e(p['did'])}</p></section><section><h2>Why it matters</h2><p>{e(p['why'])}</p></section><section><h2>What came out of it</h2><p>{e(p['outcome'])}</p></section>{note}{credit}</div><aside class="resources" aria-label="Project files"><h2>Explore the work</h2><p class="file-intro">Reports, calculations and source files from this project. Office documents download in their original format.</p>{''.join(resources[:3])}{extra}</aside></div><p class="return"><a href="../index.html#projects">← Browse the complete archive</a></p>'''
    dest=ROOT/'projects'/f'{p["id"]}.html';dest.parent.mkdir(exist_ok=True);dest.write_text(page(p['title'],body,'../',description=p['summary']),encoding='utf-8')

buttons=''.join(f'<button type="button" data-filter="{c}" aria-pressed="{str(c=="All").lower()}">{c}</button>' for c in ['All']+[c for c in ['Chemistry','Software','Data','Cybersecurity'] if any(p['category']==c for p in projects)])
body=f'''<section class="hero"><div><div class="eyebrow">The academic project archive</div><h1>Curiosity, tested.<br>Work, <em>documented.</em></h1><p class="intro">A collection of school projects in computing, data and security—the questions I explored, the methods I used and the work behind the results.</p></div><aside class="profile" aria-label="Education"><strong>Duy Hoang</strong><p>B.S. Computer Science<br>Chemistry minor<br>Montclair State University</p><span class="date">Expected graduation · <strong>December 2026</strong></span></aside></section><section id="projects" aria-labelledby="project-heading"><div class="section-top"><h2 id="project-heading">Explore the projects</h2><p id="count" role="status" aria-live="polite">{len(projects)} of {len(projects)} projects</p></div><div class="tools"><div class="filters" role="group" aria-label="Filter by subject">{buttons}</div><label class="search"><span class="sr-only">Search projects</span><input id="search" type="search" placeholder="Search projects, tools or topics…" autocomplete="off"></label></div><noscript><p>All projects are shown below. Search and filters need JavaScript; project pages and downloads work without it.</p></noscript><div class="grid">{''.join(cards)}</div><div class="empty" id="empty" hidden><h3>No projects match this search.</h3><p>Try another topic or browse the full archive.</p><button id="reset" type="button">Clear search and filters</button></div></section><section class="about" id="about"><div><div class="eyebrow">A little context</div><h2>Computing meets<br>chemical curiosity.</h2></div><div><p>I’m a Computer Science student with a Chemistry minor at Montclair State University, graduating in December 2026. This archive brings my named school-project reports, presentations and source files together in one place.</p><p>Each project explains what I worked on, why the method matters and what I produced. Every supporting file includes Duy Hoang or Duy Linh Hoang in its filename or visible contents.</p><a href="{REPO}">Browse the repository ↗</a></div></section>'''
(ROOT/'index.html').write_text(page('School projects',body,script=True),encoding='utf-8')
(ROOT/'404.html').write_text(page('Page not found','<section class="hero"><div><h1>That page is missing.</h1><p><a href="/WebProtfolio/">Return to the project archive →</a></p></div></section>',prefix='/WebProtfolio/'),encoding='utf-8')
print(f'Built {len(projects)} project pages and source previews.')
