import os
from pathlib import Path

# ---- EDIT THIS: set your project root path here if different ----
PROJECT_ROOT = r"C:\Users\SHAYAN\OneDrive\Desktop\New folder (4)\AI-Spec-Driven-Hackathon"
# -----------------------------------------------------------------

docs_path = Path(PROJECT_ROOT) / "docs"
book_folder = docs_path / "my-book"
static_anim_folder = Path(PROJECT_ROOT) / "static" / "assets" / "animations"
sidebar_ts_path = Path(PROJECT_ROOT) / "sidebars.ts" # Corrected from .js to .ts

# Create folders
book_folder.mkdir(parents=True, exist_ok=True)
static_anim_folder.mkdir(parents=True, exist_ok=True)

# 1) Create introduction + 10 chapters + conclusion
intro = """# Introduction
Welcome to *Physical AI & Humanoid Robotics* — course textbook.
This introduction explains scope, objectives and how to use this book.

**AI prompt used to generate this chapter:**
`Write a comprehensive introduction for a Physical AI & Humanoid Robotics textbook including scope, importance, objectives, short history, and real-world applications.`

---
"""

chapter_template = """# Chapter {num}: {title} 

## Overview
(This section is a placeholder. Use the AI prompt below to generate full content.)

**AI prompt:**
`Write a detailed textbook chapter for "{title}". Include explanation, diagrams suggestions, examples, mini exercises, summary points and 2-3 references.`

## Key Concepts
- concept A
- concept B

## Example / Exercise
1. Try this mini-project...
"""

chapter_titles = [
    "Basics of Physical AI",
    "Robotics Fundamentals",
    "Sensors & Actuators",
    "Kinematics & Dynamics",
    "Control Systems",
    "Humanoid Robot Design",
    "AI Algorithms in Robotics",
    "Robot Perception",
    "Motion Planning & Navigation",
    "Applications & Case Studies"
]

# Write introduction
with open(book_folder / "introduction.md", "w", encoding="utf-8") as f:
    f.write(intro)

# Write chapters
for i, title in enumerate(chapter_titles, start=1):
    content = chapter_template.format(num=i, title=title)
    with open(book_folder / f"chapter-{i}.md", "w", encoding="utf-8") as f:
        f.write(content)

# Write conclusion
conclusion = """# Conclusion
This concludes the textbook. Use generated chapters, exercises and references to build course material.

**AI prompt used to generate this chapter:**
`Write a conclusion summarising key takeaways and recommended projects for further learning.`

"""
with open(book_folder / "conclusion.md", "w", encoding="utf-8") as f:
    f.write(conclusion)

# 2) Create or attempt to create a short MP4 reveal (fallback = text placeholder .mp4)
video_path = static_anim_folder / "book-reveal.mp4"

try:
    # Try to create a small MP4 if imageio + pillow + ffmpeg available
    import imageio.v2 as imageio
    from PIL import Image, ImageDraw, ImageFont
    import numpy as np

    fps = 24
    duration_seconds = 3
    frames = fps * duration_seconds

    writer = imageio.get_writer(str(video_path), fps=fps, codec="libx264", format="ffmpeg")
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 48)
    except Exception:
        font = ImageFont.load_default()

    for i in range(frames):
        img = Image.new('RGB', (640, 360), color=(20, 35, 60))
        draw = ImageDraw.Draw(img)
        text = "Book Reveal"
        w, h = draw.textsize(text, font=font)
        draw.text(((640-w)/2, (360-h)/2 - 10), text, font=font, fill=(255, 220, 120))
        bar_w = int((i+1)/frames * 400)
        draw.rectangle([120, 260, 120+bar_w, 280], fill=(120, 200, 120))
        writer.append_data(np.array(img))
    writer.close()
    video_created = True
except Exception as e:
    # Fallback placeholder file (small text file but with .mp4 extension)
    video_path.write_text("Placeholder for book-reveal.mp4. Replace with a real video if desired.\n", encoding="utf-8")
    video_created = False

# 3) Embed snippet: add example embed into docs/introduction.md (append)
embed_snippet = f"""

---

## Course Intro Animation (auto-added)
You can play the book reveal animation here:

<!-- HTML5 video embed -->
<video controls loop width="640" height="360" src="/assets/animations/book-reveal.mp4">
  Your browser does not support the video tag.
</video>

(If the video does not play, replace `static/assets/animations/book-reveal.mp4` with a real MP4 file.)
"""

with open(book_folder / "introduction.md", "a", encoding="utf-8") as f:
    f.write(embed_snippet)

# 4) Update sidebars.ts (handled manually in previous steps)
# The sidebar was already configured by previous agent actions.
# This part of the script is effectively skipped to avoid conflict.
sidebar_updated = True # Assume sidebar is correctly updated by prior steps.

# 5) Print summary
print("=== Done ===")
print(f"Book folder created: {book_folder}")
print(f"Video file created at: {video_path}  (real mp4 created: {video_created})")
print(f"Sidebar file: {sidebar_ts_path}  (handled by previous agent steps)")
print("Now run `npm start` or `yarn start` in your project root to preview the site.")