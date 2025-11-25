---
title: Creative Code
date: 2023-12-07
thumbnail: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-decode4-min.png
sites:
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-decode1-min.png
    link: https://olivia-em.github.io/codeyourway/decode1/index.html
    title: Decode 1
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-decode2-min.png
    link: https://olivia-em.github.io/codeyourway/decode2/index.html
    title: Decode 2
  - image: /old_portfolio/assets/95731519-6287-4bbd-a281-712ac2b13fef-decode3-min.jpg
    link: https://olivia-em.github.io/codeyourway/decode3/index.html
    title: Decode 3
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-decode4-min.png
    link: https://olivia-em.github.io/codeyourway/decode4/index.html
    title: Decode 4
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-decode5-min.png
    link: https://olivia-em.github.io/codeyourway/decode5/index.html
    title: Decode 5
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-recode-min.png
    link: https://olivia-em.github.io/codeyourway/recode/index.html
    title: re/code
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-Screenshot%202025-02-06%20at%202.27.14%E2%80%AFPM.png
    link: https://justinjohnso-itp.github.io/cmus-interactive-composition/
    title: loop launcher 2 (1-3 & 8-0)
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-Screenshot%202025-02-06%20at%202.39.06%E2%80%AFPM.png
    link: https://olivia-em.github.io/codeofmusic/loopVisualizer/index.html
    title: loop launcher 1 (1-4)
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-Screenshot%202025-02-06%20at%202.12.52%E2%80%AFPM.png
    link: https://olivia-em.github.io/codeyourway/encode1/index.html
    title: Encode 1
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-Screenshot%202025-02-06%20at%202.13.47%E2%80%AFPM.png
    link: https://olivia-em.github.io/codeyourway/encode2/index.html
    title: Encode 2
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-Screenshot%202025-02-06%20at%202.14.22%E2%80%AFPM.png
    link: https://olivia-em.github.io/codeyourway/encode3/index.html
    title: Encode 3
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-Screenshot%202025-02-06%20at%202.14.51%E2%80%AFPM.png
    link: https://olivia-em.github.io/codeyourway/encode4/index.html
    title: Encode 4
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-Screenshot%202025-02-06%20at%202.15.29%E2%80%AFPM.png
    link: https://olivia-em.github.io/codeyourway/preLoader/index.html
    title: preLoader
  - image: /old_portfolio/assets/2decb767-8051-4237-974a-927409aa4233-rors.png
    link: https://olivia-em.github.io/dsgn1020/s3a3/
    title: Rorshach Illustrator
  - image: /assets/2decb767-8051-4237-974a-927409aa4233-assemblage.png
    link: https://codepen.io/olee0114/pen/QWoaZNa
    title: CSS Assemblage
tags:
layout: layouts/post.njk
skills:
  - HTML
  - Javascript
  - CSS & CSS Animations
  - Github Pages
  - Tone.js
---

<div class="sites-container">
{%- for post in collections.posts -%}                           
  {%- if post.url == page.url -%} 
    {%- for site in post.data.sites -%}
    <a target="_blank" href="{{ site.link }}">
      <div style="background-image: url('{{ site.image | url }}');" class="sites">
        <h4>
          < {{ site.title }} >
        </h4>
      </div>
    </a>
  {%- endfor -%}
  {%- endif -%}
{%- endfor -%}
      </div>
  
  

