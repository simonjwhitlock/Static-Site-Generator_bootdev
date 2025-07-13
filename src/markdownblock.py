from enum import Enum
import re


class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    LISTU = "unordered_list"
    LISTO = "ordered_list"


def markdown_to_blocks(markdown):
    markdown_split = markdown.split("\n\n")
    markdown_blocks = []
    for split in markdown_split:
        split = split.strip()
        if split == "":
            continue
        markdown_blocks.append(split)
    return markdown_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    if re.match(r"^\#{1,6}\s+", block):
        return BlockType.HEAD
    elif len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        linetype = (BlockType.QUOTE)
        for line in block.split("\n"):
            if not line.startswith(">"):
                return BlockType.PARA
        return linetype
    elif re.match(r"\-", block):
        linetype = (BlockType.LISTU)
        for line in lines:
            if not re.match(r"^\-", line):
                return BlockType.PARA
        return linetype
    elif re.match(r"1\.", block):
        linetype = (BlockType.LISTO)
        line_no = 1
        for line in lines:
            if not re.match(rf"{line_no}\.", line):
                return BlockType.PARA
            line_no += 1
        return linetype
    return BlockType.PARA


def demo_block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEAD
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARA
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARA
        return BlockType.LISTU
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARA
            i += 1
        return BlockType.LISTO
    return BlockType.PARA