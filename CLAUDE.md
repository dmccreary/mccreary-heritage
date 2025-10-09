# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a McCreary family heritage website built using MkDocs with the Material theme. The site documents the Scotch-Irish McCreary family history, including their migration from Scotland through Ireland (Ulster Plantation) to North America. The site serves multiple audiences: family genealogists, educators, students, heritage tourists, and academic researchers.

## Development Commands

### Environment Setup
```sh
# The project uses conda for environment management
conda activate mkdocs
# If environment doesn't exist:
conda create -n mkdocs python=3
conda activate mkdocs
pip install mkdocs "mkdocs-material[imaging]"
```

### Building and Testing
```sh
# Build the site (outputs to ./site directory)
mkdocs build

# Run local development server on http://localhost:8000
mkdocs serve

# Deploy to GitHub Pages (does NOT commit code to git)
mkdocs gh-deploy
```

### Git Workflow
After making changes:
```sh
git add [files]
git commit -m "descriptive message"
git push
```

## Content Architecture

### Content Organization
- **Main documentation**: `docs/` directory
- **Numbered content sections**: `docs/content/01-introduction/`, `docs/content/02-family-history-and-genealogy/`, etc. (9 sections total)
- **Design documentation**: `docs/prompts/` contains personas and site-layout planning documents
- **Static assets**: `docs/img/`, `docs/css/`, `docs/js/`
- **Site configuration**: `mkdocs.yml` at root

### Content Structure Strategy
The site follows a deliberate structure optimized for different user personas:
1. **Family History & Genealogy** - Primary audience (genealogists)
2. **Historical Timeline & Context** - Chronological narrative
3. **Geography & Settlement Patterns** - Migration visualization
4. **Heritage Tourism Guide** - Travel resources
5. **Educational Resources** - Teachers and students
6. **Culture & Traditions** - Scotch-Irish heritage
7. **Research & Scholarship** - Academic resources
8. **Stories & Biographies** - Personal narratives

### Content Guidelines
- Use Scottish Gaelic terminology appropriately (e.g., Mac Ruairidh)
- Include surname variations: McCreary, MacCreary, McCreery, McCrory, MacRory, Magrory
- Cross-reference the glossary for specialized terms using relative links: `[term](../glossary.md#term-anchor)`
- Content is licensed Creative Commons ShareAlike Attribution Noncommercial

## Technical Stack

### MkDocs Material Theme Features (Enabled)
- Code copy buttons (`content.code.copy`)
- Navigation expansion, path breadcrumbs, pruning, indexes
- TOC following and navigation top/footer
- Edit action icons (links to GitHub)
- Search plugin
- Syntax highlighting with line numbers
- Admonitions and details extensions

### Theme Configuration
- Primary color: blue
- Accent color: orange
- Logo: `docs/img/logo.png`
- Custom CSS: `docs/css/extra.css`
- Custom JS: `docs/js/extra.js`

### Edit Links
Edit URI configured to `blob/master/docs` - clicking edit icons takes users to GitHub source

## Navigation Structure

The `mkdocs.yml` nav section defines the top-level navigation. When adding new pages:
1. Create markdown file in appropriate `docs/content/XX-section/` directory
2. Update `nav:` section in `mkdocs.yml` if top-level navigation change needed
3. Use descriptive titles that match user mental models

## Image Processing Notes

Material theme's social card generation requires system libraries on macOS:
```sh
brew install cairo freetype libffi libjpeg libpng zlib
# Add to ~/.zshrc:
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
```

Note: These are Apple Silicon specific paths. Social plugin is currently commented out in mkdocs.yml.

## Project Context

### Site URLs
- Live site: https://dmccreary.github.io/mccreary-heitage/
- Repository: https://github.com/dmccreary/mccreary-heitage
- Contact: Dan McCreary via LinkedIn

### Historical Scope
- Time period: 1500s-1900s
- Geographic focus: Scotland → Ulster (Ireland) → North America (PA, VA, NC, SC, TN, KY)
- Cultural context: Presbyterian Scotch-Irish migration and settlement patterns
- Key historical events: Ulster Plantation (1600s), Great Migration to Americas (1700s-1800s)

### Audience Considerations
When creating or editing content, consider these primary user groups:
- Family genealogists (largest expected audience)
- K-12 educators and students
- Heritage tourists planning trips
- Academic researchers
- Local historians

## VS Code Configuration

Custom dictionary words are configured in `.vscode/settings.json` for domain-specific terminology (e.g., Ruairidh, townlands, Magrory).
