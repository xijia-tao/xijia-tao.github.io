# Website Context

## Owner and Positioning

This is the personal academic website of **Xijia Tao** (also Ciel; 陶熙佳), a
PhD student in the HKUNLP lab at the University of Hong Kong. The public author
profile lists Hong Kong as the location and links to Google Scholar, GitHub,
LinkedIn, and X.

The homepage currently describes two active research themes:

- multimodal deep research / multimodal browsing agents
- diffusion large language models

The publication record also supplies context in agent skill compression,
vision-language model safety, and multilingual transfer. These additional
directions should remain visible through the publication list, but should not
automatically be promoted into the short current-research statement.

## Public Content Inventory

The homepage (`_pages/about.md`) is the canonical visitor-facing overview. It
contains a short biography followed by a reverse-chronological publication
list:

1. SoftSkill — behavioral compression for contextual adaptation; arXiv
   2606.20333
2. Self-Distilled Trajectory-Aware Boltzmann Modeling — diffusion-language-model
   post-training; arXiv 2605.11854
3. Beyond Confidence — diffusion-language-model decoding; arXiv 2512.02044
4. MMSearch-Plus — multimodal browsing-agent benchmark; ICLR 2026 and arXiv
   2508.21475
5. OmniPlay — omni-modal game-playing benchmark; arXiv 2508.04361
6. ImgTrojan — vision-language-model jailbreaking; NAACL 2025, ACL Anthology
   2025.naacl-long.360
7. Language Versatilists vs. Specialists — multilingual transfer; arXiv
   2306.06688

The homepage, not `_publications/`, is the primary publication list.
`_publications/` currently contains legacy generated detail records for
ImgTrojan and Language Versatilists vs. Specialists; keep their metadata
consistent when touching those papers.

Other public pages are mostly inherited Academic Pages scaffolding. The main
navigation intentionally exposes only Blog Posts and CV. The CV page links to
`files/cv.pdf`. There is no dedicated News or Projects section; project pages
and repositories are linked as resources beneath publication entries.

## Technical Shape

- Static site generator: Jekyll / GitHub Pages
- Theme lineage: Academic Pages on Minimal Mistakes
- Primary configuration: `_config.yml`
- Navigation: `_data/navigation.yml`
- Homepage: `_pages/about.md`
- Publication detail collection: `_publications/`
- Local media: `images/` and `files/`
- Ruby build: `bundle exec jekyll build`
- JavaScript bundle: `npm run build:js`
- Production URL: `https://xijia-tao.github.io`

The theme and build stack are old but stable. Routine content maintenance must
not become an unsolicited dependency, framework, or visual redesign project.

## Audience and Editorial Voice

Primary visitors are academic researchers, potential collaborators,
prospective students, and research-oriented recruiters. The desired style is:

- concise and factual
- minimal, professional, and researcher-oriented
- easy to scan on desktop and mobile
- neutral about claims and contributions
- free of startup language, inflated adjectives, decorative artwork, and heavy
  interaction

Preserve the friendly first-person opening and the owner's use of the names
“Ciel” and “陶熙佳.” Avoid time-fragile biography phrases such as a numbered PhD
year unless the owner explicitly wants to maintain them.

## Maintenance Boundaries

Safe routine changes include verified publication metadata, working resource
links, typographical fixes, and small consistency improvements. Ask before
changing research identity, navigation, personal contact details, profile
photos, or the visual design. Never infer acceptances, awards, affiliations,
author order, or publication status.
