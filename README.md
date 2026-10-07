# Duy Hoang — Academic Portfolio

A central index of 24 academic projects with 44 files drawn exclusively from the seven project folders supplied on October 7, 2026. This collection replaces the previous website archive.

**Website:** https://bigbodydubot.github.io/WebProtfolio/

## Browse

- Chemistry: spectrophotometric calibration, internal standards, acid-base titration and measurement statistics.
- Software: computer networks, HTTP sockets, matrix projections, Linux modules, signals, synchronization, message queues and xv6 scheduling.
- Data: statistical literacy, descriptive summaries, regression, probability, z-scores and a Python/SQLite enrollment application.
- Cybersecurity: Linux access control, Set-UID, memory protections, packet handling, firewalls and web-security labs.

Each project explains the work, its purpose and the documented outcome. Reports, measurements, code and presentations are linked from the project pages. Cybersecurity pages include lab setup descriptions based on the supplied reports. The Set-UID, buffer-overflow and packet-spoofing pages also provide downloadable ZIP folders from the locally supplied setup packages; original SEED lab scaffolds remain attributed. Duplicate buffer-overflow archives were consolidated and an editor swap file was omitted. Collaborator and course-scaffold credits remain intact.

## Collection and attribution

Only materials from the newly supplied Computer Networks, Analytical Chemistry, Computer Security, Data Science and Statistics, Linear Algebra, Database Systems and Operating Systems folders are used. The user authorized inclusion of these supplied project files even when their full name is absent. Topic-based filenames preserve the original formats; projects.json records original filenames, file roles and original attribution.

Standalone images and restaurant-related projects are excluded according to the user's preferences. Instructor briefs, example workbooks and instructor-supplied datasets are omitted. Course names and numbers are removed from project labels. The third-party news article used by the statistical-literacy assignment is not republished. The message-queue homework ZIP was unpacked into two C source files; its standalone screenshot is excluded. Content hashes were checked to avoid exact duplicate attachments.

Academic reports are preserved as supplied. Project descriptions distinguish recorded findings from confirmed accuracy or production outcomes and note material limitations in the original work.

## Renaming and dependencies

The enrollment application resolves University_Enrollment_Database_Duy_Hoang.db beside its source file. Download both into the same folder before running it with Python 3. The kernel module build file targets Linux_Module_Lifecycle_Duy_Hoang.c; use make -f Linux_Module_Build_Duy_Hoang in that folder on a matching Linux kernel development environment. These are filename compatibility changes; coursework logic is preserved.

The HTTP server and client are local Python exercises. Their HTML test page is displayed as escaped source in the portfolio. Packet Tracer files require Cisco Packet Tracer. The xv6 scheduler file requires its surrounding source tree. Security scripts are displayed as source, not executed by the website.

## Update the site

1. Add a supporting file under files/<project-id>/ with a descriptive filename.
2. Add or edit its resource entry in projects.json, including role, byte size and attribution.
3. Run python build.py to regenerate the index, project pages and source previews. Python 3 is the only build dependency.
4. When removing a resource or project, remove its obsolete generated page or source preview too.
5. Commit the updated collection and generated pages, then push to main.

For a local preview, run python -m http.server 8000 from this folder and open http://localhost:8000.

The existing page layout and styling are retained. The project list shows six projects per page, with numbered navigation links above and below it. Search and subject filters apply to the complete collection. Page links can be bookmarked and browser Back/Forward restores the selected page. Project links and downloads work without JavaScript. There are no analytics, external fonts or third-party page scripts.

## GitHub Pages

Publish from the main branch and repository root in Settings → Pages. The .nojekyll file allows GitHub Pages to serve the generated files directly. Project and file URLs are relative to support the /WebProtfolio/ base path.

## File structure

- index.html: central project index
- projects.json: project descriptions, file metadata and attribution
- projects/: generated project pages
- source/: generated code and text previews
- files/: project work, measurements and code
- styles.css, app.js: existing presentation and filtering
- build.py: standard-library static site generator

Original collaborator contributions, scaffold comments and library references retain their attribution. No blanket license is applied to academic attachments.
