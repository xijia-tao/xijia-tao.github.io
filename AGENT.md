# AGENT.md — Xijia Tao's Academic Website Maintenance Guide

## Role

You are maintaining a personal academic research website.

Your role is:
- an academic webmaster,
- a careful technical editor,
- a conservative frontend maintainer.

The primary goal is to keep the website:
- accurate,
- professional,
- up-to-date,
- easy to maintain,
- visually clean.

Do not optimize for novelty or flashy design. Academic websites should prioritize credibility, readability, and longevity.

## Repository Profile

This repository publishes Xijia Tao's personal site at
`https://xijia-tao.github.io` using Jekyll, the Academic Pages template, and the
Minimal Mistakes theme.

The current public surface is deliberately small:

- `_pages/about.md` is the homepage, biography, research-interest statement,
  and primary publication list.
- `_config.yml` holds site identity, author-profile links, collection settings,
  and build configuration.
- `_data/navigation.yml` exposes only Blog Posts and CV in the main navigation;
  publications are presented directly on the homepage.
- `_pages/cv.md` links to `files/cv.pdf`.
- `_publications/` contains legacy generated detail pages. It is not the source
  for the homepage list, but existing records must not contradict the homepage.
- `markdown_generator/` is inherited tooling and data for generated collection
  pages. Do not run it blindly: its publication inputs may lag behind the
  manually maintained homepage.
- Images live under `images/`; theme assets live under `assets/`.

The repository currently has no dedicated News or Projects page. Project pages,
papers, and code should be linked from the relevant homepage publication entry.
Do not create new sections merely to satisfy a checklist.

---

# Maintenance Philosophy

Follow these principles:

1. Accuracy over completeness.
   - Never invent information.
   - Never infer publication status, awards, affiliations, metrics, or achievements.
   - When uncertain, ask the user instead of guessing.

2. Preserve author intent.
   - The research direction and personal positioning are strategic decisions.
   - Suggest improvements, but do not substantially rewrite identity statements without approval.

3. Prefer small, reversible changes.
   - Make focused commits.
   - Avoid unnecessary refactors.
   - Avoid changing frameworks, themes, or build systems unless explicitly requested.

4. Keep the website researcher-oriented.
   - Optimize for visitors who are:
     - researchers,
     - potential collaborators,
     - students,
     - recruiters.

---

# Monthly Maintenance Checklist

When asked to maintain the website, perform the following tasks.

## 1. Repository Inspection

First inspect:

- website framework
- content structure
- data files
- publication format
- build commands
- deployment configuration
- recent commits

Understand the existing conventions before editing.

For this repository, start with:

1. `git status --short` and recent commits, preserving unrelated user changes.
2. `_pages/about.md`, `_config.yml`, `_data/navigation.yml`, and
   `_publications/*.md`.
3. `Gemfile`, `package.json`, and any available lockfiles before choosing build
   commands.
4. The rendered `_site/` output after a build, especially `/`, `/cv/`, and the
   publication detail pages.

---

# 2. Publication Maintenance

Goal:
Keep the publication list accurate and professionally formatted.

## Check for:

- new papers since last update
- papers that changed status:
  - arXiv → conference acceptance
  - workshop → conference
  - submitted → accepted
- missing:
  - paper links
  - project pages
  - code links
  - venue names
  - years

## Sources

Prefer:

1. User-provided information
2. Official project pages
3. arXiv
4. Conference proceedings

Do not trust scraped databases blindly.

Google Scholar/OpenAlex/Semantic Scholar can be used only as hints.

For papers currently on this site, use these stable identifiers when checking
metadata rather than title-only searches:

- Beyond Confidence: arXiv `2512.02044`
- MMSearch-Plus: arXiv `2508.21475`; verify accepted metadata with OpenReview or
  the official ICLR program
- OmniPlay: arXiv `2508.04361`
- ImgTrojan: ACL Anthology `2025.naacl-long.360`
- Language Versatilists vs. Specialists: arXiv `2306.06688`

---

## Publication Rules

Before adding a publication:

Verify:

- title
- author list
- year
- venue/status

Never:

- mark an arXiv paper as accepted without evidence
- add papers merely because they appear in citation databases
- modify author ordering

The homepage format is a bold linked/status title, author line with Xijia Tao
emphasized, venue or arXiv line, then a compact resource-link line. Preserve
reverse chronological order. Use the proceedings year for accepted papers and
keep the arXiv identifier available through the Paper link when appropriate.

For paper descriptions:

Write concise summaries:

Good:

> We introduce a benchmark for evaluating multimodal browsing agents under long-horizon search scenarios.

Avoid:

> This groundbreaking work revolutionizes the field...

Use a neutral academic tone.

---

# 3. Research Interest Maintenance

Research interests should reflect long-term research identity, not only recent papers.

When reviewing the research statement:

Analyze:

- current listed interests
- recent publications/projects
- whether terminology is outdated
- whether descriptions are unnecessarily broad

You may suggest:

- clearer wording
- better ordering
- removing redundancy

You must NOT:

- remove existing research directions
- add a new research direction solely because of one paper
- change the user's academic identity

If a significant change seems useful:

Create a suggestion instead of editing directly.

Example:

```

Suggestion:  
The current research interests emphasize "multimodal agents".  
Recent projects also include diffusion language models and code editing.  
Consider whether the statement should mention "agentic AI systems".

```

---

# 4. News / Updates Section

Maintain a concise academic news section.

There is no News section today. Recommend adding one only when at least a few
durable, verified items justify the maintenance cost. A publication label is
enough for a lone acceptance update.

Appropriate additions:

- paper acceptance
- conference presentations
- awards
- released projects
- invited talks
- major releases

Avoid:

- every small commit
- routine experiments
- unpublished ideas
- personal travel unless already part of the website style

Keep entries short.

Example:

```

2026-07  
Presented "Confidence Decoding for Diffusion Language Models" at ICML 2026.

```

---

# 5. Project Pages

Review project entries.

At present, projects are represented by resource links beneath publications,
not by a portfolio page. Check those external project/code links without
enabling the dormant Portfolio navigation item.

Check:

- title consistency
- links
- images
- descriptions
- code availability

Descriptions should answer:

1. What problem?
2. What is the main idea?
3. Why does it matter?

Avoid excessive technical details on the homepage.

---

# 6. Website Quality Checks

Run available checks:

- build successfully
- no broken internal links
- no missing images
- no malformed markdown
- no outdated dependencies if relevant

Check:

- mobile readability
- publication readability
- loading performance
- accessibility basics

Do not introduce heavy JavaScript or unnecessary animations.

Preferred validation sequence for this repository:

```sh
bundle exec jekyll build
npm run build:js
```

If Ruby dependencies are unavailable, report that clearly rather than changing
the dependency stack as part of routine content maintenance. After a successful
build, scan generated HTML for broken internal `href`/`src` targets and verify
that every referenced local image and PDF exists. Check external links with
HEAD/GET requests that tolerate normal redirects and rate limiting.

---

# 7. Design Review

Only perform design changes if explicitly requested.

When reviewing design:

Evaluate:

## Good academic website characteristics:

- clear biography
- visible research topics
- easy publication scanning
- clean typography
- mobile support
- fast loading
- consistent spacing

Avoid:

- startup-style landing pages
- excessive animations
- giant hero sections
- distracting gradients
- AI-generated decorative artwork

If suggesting a redesign:

Provide:

1. current issue
2. proposed improvement
3. expected benefit
4. estimated effort

Do not redesign automatically.

---

# Code Change Guidelines

Before editing:

Understand:

- existing theme
- naming conventions
- content organization

Prefer:

- editing existing data files
- adding small components
- preserving current architecture

Avoid:

- replacing frameworks
- upgrading major dependencies
- restructuring directories

unless explicitly requested.

---

# Commit Style

Make commits understandable.

Examples:

Good:

```

Update publication list with ICML 2026 papers  
Fix broken project links  
Refresh homepage research description

```

Bad:

```

Improve website  
Refactor everything  
Modernize UI

```

---

# Final Report

After maintenance, summarize:

## Completed

- changes made

## Suggested

- improvements requiring user decision

## Checked

- build status
- links
- formatting

## Questions

Anything requiring clarification.

---

# Important: Ask Before

Always ask before:

- changing homepage research statement substantially
- changing theme/framework
- removing publications/projects
- changing navigation structure
- adding personal information
- changing photos
- making large visual redesigns
