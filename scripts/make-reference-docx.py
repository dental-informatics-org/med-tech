#!/usr/bin/env python3
"""Build scripts/reference.docx — a pandoc reference document that enforces the
house style for every exported Word/PDF file:

    * Font:         Arial
    * Body size:    12 pt
    * Line spacing: 1.5
    * Alignment:    justified

It starts from pandoc's built-in default reference and edits the Word XML so the
style cascades to all body text (via docDefaults + the Normal style) and all
headings (via the theme fonts). Re-run whenever pandoc changes its default.
"""
import io
import re
import subprocess
import zipfile
from pathlib import Path

OUT = Path(__file__).resolve().parent / "reference.docx"

ARIAL = '<w:rFonts w:ascii="Arial" w:eastAsia="Arial" w:hAnsi="Arial" w:cs="Arial" />'


def edit_styles(xml: str) -> str:
    # 1) default run font -> Arial (keep size 24 = 12pt)
    xml = re.sub(r'<w:rFonts w:asciiTheme="minorHAnsi"[^>]*/>', ARIAL, xml, count=1)
    # 2) default paragraph -> add 1.5 line spacing + justify
    xml = xml.replace(
        '<w:pPr>\n        <w:spacing w:after="200" />\n      </w:pPr>',
        '<w:pPr><w:spacing w:after="200" w:line="360" w:lineRule="auto" />'
        '<w:jc w:val="both" /></w:pPr>')
    # 3) Normal style -> explicit Arial 12, 1.5, justify (most styles inherit from it)
    normal_inject = (
        '<w:name w:val="Normal" />\n    <w:qFormat />\n'
        '    <w:pPr><w:spacing w:line="360" w:lineRule="auto" />'
        '<w:jc w:val="both" /></w:pPr>\n'
        f'    <w:rPr>{ARIAL}<w:sz w:val="24" /><w:szCs w:val="24" /></w:rPr>')
    xml = xml.replace('<w:name w:val="Normal" />\n    <w:qFormat />', normal_inject, 1)

    # 4) headings must NOT be justified (they inherit "both" from Normal) -> left-align
    headings = {"Heading1", "Heading2", "Heading3", "Heading4", "Heading5",
                "Heading6", "Subtitle", "TOCHeading"}

    def left_align(m):
        block, sid = m.group(0), m.group(1)
        if sid not in headings:
            return block
        if "<w:jc " in block:
            return re.sub(r'<w:jc w:val="[^"]*" ?/>', '<w:jc w:val="left" />', block, count=1)
        if "<w:pPr>" in block:
            return block.replace("<w:pPr>", '<w:pPr><w:jc w:val="left" />', 1)
        return block.replace("</w:style>", '<w:pPr><w:jc w:val="left" /></w:pPr></w:style>', 1)

    xml = re.sub(r'<w:style [^>]*w:styleId="([^"]+)"[^>]*>.*?</w:style>',
                 left_align, xml, flags=re.S)
    return xml


def edit_theme(xml: str) -> str:
    # major (headings) + minor (body) theme fonts -> Arial
    xml = xml.replace('typeface="Aptos Display"', 'typeface="Arial"')
    xml = xml.replace('typeface="Aptos"', 'typeface="Arial"')
    return xml


def main():
    base = subprocess.run(
        ["pandoc", "--print-default-data-file", "reference.docx"],
        check=True, capture_output=True).stdout
    src = zipfile.ZipFile(io.BytesIO(base))
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as out:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == "word/styles.xml":
                data = edit_styles(data.decode("utf-8")).encode("utf-8")
            elif item.filename == "word/theme/theme1.xml":
                data = edit_theme(data.decode("utf-8")).encode("utf-8")
            out.writestr(item, data)
    OUT.write_bytes(buf.getvalue())
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
