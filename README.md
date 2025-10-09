# McCreary Family Heritage

[![MkDocs](https://img.shields.io/badge/MkDocs-1.6-blue.svg)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/Material%20for%20MkDocs-9.5-blue.svg)](https://squidfunk.github.io/mkdocs-material/)
[![Deployed on GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-brightgreen.svg)](https://dmccreary.github.io/mccreary-heitage/)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](docs/license.md)

A comprehensive website documenting the history, heritage, and genealogy of the McCreary family—from their origins in Scotland, through the Ulster Plantation in Ireland, to their migration and settlement across North America.

## 🌐 Live Site

Visit the website: **[https://dmccreary.github.io/mccreary-heitage/](https://dmccreary.github.io/mccreary-heitage/)**

## 📖 About

This site tells the story of the Scotch-Irish McCreary families spanning over 400 years (1500s-1900s). It serves multiple audiences:

- **Family Genealogists** researching McCreary ancestry and surname variations
- **Educators & Students** studying migration patterns and historical context
- **Heritage Tourists** planning visits to ancestral sites in Scotland and Ireland
- **Academic Researchers** accessing documented sources and scholarly materials
- **Local Historians** exploring regional settlement patterns

## 🗺️ Content Overview

The site covers:

- **Family History & Genealogy** - Documented family lines and research resources
- **Historical Timeline** - Major events from Scotland to the American frontier
- **Geography & Settlement Patterns** - Interactive maps showing migration routes
- **Heritage Tourism Guide** - Practical information for visiting ancestral sites
- **Educational Resources** - Lesson plans and primary sources for teachers
- **Culture & Traditions** - Scotch-Irish heritage, language, music, and customs
- **Research & Scholarship** - Academic resources and methodologies
- **Stories & Biographies** - Personal narratives bringing history to life

## 🚀 Development

### Prerequisites

- Python 3.x
- Conda or pip for package management
- Git

### Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/dmccreary/mccreary-heitage.git
   cd mccreary-heitage
   ```

2. **Set up the environment**
   ```sh
   conda create -n mkdocs python=3
   conda activate mkdocs
   pip install mkdocs "mkdocs-material[imaging]"
   ```

### Common Commands

**Build the site locally**
```sh
mkdocs build
```

**Run development server**
```sh
mkdocs serve
```
Then visit `http://localhost:8000` in your browser.

**Deploy to GitHub Pages**
```sh
mkdocs gh-deploy
```
Note: This deploys the site but does not commit source code changes. Remember to commit and push your changes separately.

## 📂 Project Structure

```
mccreary-heitage/
├── docs/                          # All site content
│   ├── content/                   # Main content organized in 9 sections
│   │   ├── 01-introduction/
│   │   ├── 02-family-history-and-genealogy/
│   │   ├── 03-timeline/
│   │   ├── 04-geography/
│   │   ├── 05-education/
│   │   ├── 06-heratage-tourism/
│   │   ├── 07-culture-and-traditions/
│   │   ├── 08-research/
│   │   └── 09-stories/
│   ├── prompts/                   # Design documentation and personas
│   ├── css/                       # Custom styling
│   ├── js/                        # Custom JavaScript
│   ├── img/                       # Images and logos
│   ├── index.md                   # Homepage
│   ├── glossary.md                # Terminology definitions
│   └── references.md              # Bibliography and resources
├── mkdocs.yml                     # Site configuration
├── CLAUDE.md                      # AI assistant guidance
└── README.md                      # This file
```

## 🤝 Contributing

Contributions are welcome! If you have:

- Additional family history information
- Corrections or clarifications
- Photos or documents to share
- Suggestions for improvements

Please contact Dan McCreary via [LinkedIn](https://www.linkedin.com/in/danmccreary/) or open an issue on GitHub.

## 📜 License

All content is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](docs/license.md).

You are free to share and adapt the material for non-commercial purposes, as long as you provide attribution and distribute under the same license.

## 🙏 Acknowledgements

This site was built using the following excellent open source projects:

### Core Technologies
- **[MkDocs](https://www.mkdocs.org/)** - Fast, simple static site generator for project documentation
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** - Modern, feature-rich theme for MkDocs with extensive customization options

### Python & Ecosystem
- **[Python](https://www.python.org/)** - The programming language powering MkDocs
- **[Python-Markdown](https://python-markdown.github.io/)** - Markdown parser with extensions
- **[PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)** - Enhanced markdown features including syntax highlighting, admonitions, and code blocks

### Hosting & Deployment
- **[GitHub](https://github.com/)** - Version control and repository hosting
- **[GitHub Pages](https://pages.github.com/)** - Free, reliable static site hosting

### Development Tools
- **[Conda](https://docs.conda.io/)** - Package and environment management
- **[Git](https://git-scm.com/)** - Distributed version control system

### Additional Libraries
- **[Cairo](https://cairographics.org/)**, **[FreeType](https://freetype.org/)**, and image processing libraries - Supporting Material theme's social card generation

We're grateful to the maintainers and contributors of these projects for making tools like this website possible.

## 📞 Contact

**Dan McCreary**
Connect on [LinkedIn](https://www.linkedin.com/in/danmccreary/)

---

*Last updated: October 2024*
