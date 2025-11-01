# Peter Faucitt Interdict Documents

This directory contains the original scanned images and OCR-generated markdown transcripts of the Peter Faucitt Interdict legal documents.

## Contents

- **Original Images**: 51 JPG files (`CCE20250924_0001.jpg` through `CCE20250924_0051.jpg`)
- **Cover Image**: `CCE20250924.jpg`
- **Complete Transcript**: `peter-faucitt-interdict-complete.md` - Combined OCR transcript of all pages
- **Individual Pages**: `markdown/` directory contains individual markdown files for each page

## OCR Processing

The documents were processed using Tesseract OCR on September 30, 2025. The OCR output includes:

1. Individual markdown files for each page (in the `markdown/` subdirectory)
2. A complete combined document (`peter-faucitt-interdict-complete.md`)

### Notes on OCR Quality

- The OCR process may contain errors typical of automated text recognition
- Some formatting and special characters may not be perfectly preserved
- Page numbers and source file references are included for each page
- The documents appear to be legal interdict papers involving multiple respondents

## File Structure

```
/docs/peter-faucitt-interdict/
├── README.md                                    # This file
├── peter-faucitt-interdict-complete.md         # Complete OCR transcript
├── markdown/                                    # Individual page transcripts
│   ├── page_0001.md
│   ├── page_0002.md
│   └── ... (51 files total)
├── CCE20250924.jpg                             # Cover image
└── CCE20250924_0001.jpg through _0051.jpg     # Original scanned pages
```

## Usage

- For reading the full document, use `peter-faucitt-interdict-complete.md`
- For referencing specific pages, use the individual files in the `markdown/` directory
- Original images are preserved for verification or re-processing if needed