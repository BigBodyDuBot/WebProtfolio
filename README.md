# Duy Hoang — Academic Portfolio

A central index of 15 school projects and 42 supporting files bearing **Duy Hoang** or **Duy Linh Hoang** in the original filename or visible contents.

**Website:** https://BigBodyDuBot.github.io/WebProtfolio/

## Browse

- Software: graphics, operating systems, concurrency, languages, algorithms and digital logic.
- Data: relational schemas, database coursework and analytical reasoning.
- Cybersecurity: Linux access controls, memory safety, networking and web security labs.

Each project explains the work, its purpose and the resulting academic deliverables. Reports and original files are linked from the project page. Retained source files can also be read directly on the site.

## Name-based inclusion rule

Only coursework with **Duy Hoang** or **Duy Linh Hoang** in its original filename or visible contents is included. Names split by spaces or line breaks are recognized; scans were also checked visually. A computer username in a filesystem path, generated website heading, surname alone, or another file from the same project does not qualify a file. Coauthored work is retained when it includes the required name, with the other authors still credited.

The name review retained 42 of the previous 104 attachments. Projects without a qualifying attachment were removed, including the chemistry projects. Each retained resource in `projects.json` records where its name was verified.

This is a coursework portfolio. Draft analyses are identified on the relevant pages. Claims are limited to the documented academic work; no commercial outcomes or production deployments are implied. Original coauthor and course-scaffold credits are retained. Standalone photographs, unrelated personal files, resumes, restaurant material and exam files are not included. Exact duplicate files are omitted; other versions remain grouped with their project.

## Update the site

1. Verify that a supporting file contains one of the two full names, then add it under `files/<project-id>/`.
2. Add or edit a project in `projects.json`. Use the existing entries as a template, including relative file paths, byte sizes, `name_match` and `name_match_location`.
3. Run `python build.py` to regenerate the index, project pages and source previews. Python 3 is the only build dependency.
4. Commit the updated data, files and generated pages, then push to `main`.

For a local preview, run `python -m http.server 8000` from this folder and open http://localhost:8000.

The site uses HTML, CSS and a small JavaScript search/filter enhancement. All project links and downloads work without JavaScript. There are no analytics, external fonts or third-party page scripts.

## GitHub Pages

Publish from the `main` branch and the repository root (`/`) in **Settings → Pages**. `.nojekyll` allows GitHub Pages to serve the generated files directly. All project and file URLs are relative to support the `/WebProtfolio/` base path.

## File structure

- `index.html`: central project index
- `projects.json`: editable project descriptions and file metadata
- `projects/`: generated project pages
- `source/`: generated read-only code and notebook previews
- `files/`: original coursework and reports
- `styles.css`, `app.js`: presentation and filtering
- `build.py`: standard-library static site generator

Original course materials, collaborator contributions and library references retain their existing attribution. No blanket license is applied to the academic attachments.
