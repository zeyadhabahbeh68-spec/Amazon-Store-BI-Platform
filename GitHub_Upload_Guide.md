# GitHub Upload Guide

Use this package to document the graduation project using Markdown files instead of Word files.

## Recommended Repository Structure

```text
Amazon-Store-BI-Platform/
├── README.md
├── docs/
├── images/
├── data/
└── src/
```

## Upload Order

1. Upload `README.md` to the repository root.
2. Upload all files inside `docs/` to the `docs` folder.
3. Upload all charts and screenshots inside `images/` to the `images` folder.
4. Upload CSV files inside `data/` to the `data` folder.
5. Upload `app1.py` inside `src/`.

## Important Image Path Rule

Markdown files inside `docs/` must refer to images using:

```md
![Figure Title](../images/image_name.png)
```

The `../` is required because the Markdown file is inside the `docs` folder, while the images are stored in the root-level `images` folder.
