# Academic CV

This directory contains the LaTeX source for Xijia Tao's academic CV. The
homepage (`../_pages/about.md`) is the canonical source for publication status,
author order, and links.

## Build

Install a TeX distribution that provides `latexmk`, `tectonic`, or `pdflatex`,
then run:

```sh
make
```

After reviewing the generated `xijia_tao_cv.pdf`, publish it to the website:

```sh
make publish
```

The publish target replaces `../files/cv.pdf`, which is linked from the site's
CV page. Run `make clean` to remove generated files.

## Updating

- Edit biographical, education, and experience content in `xijia_tao_cv.tex`.
- Edit publication entries in `publications.tex`.
- Keep publication metadata synchronized with `../_pages/about.md`.
- Use `\me` for Xijia Tao's name in author lists and escape LaTeX special
  characters such as `&` and `%`.
