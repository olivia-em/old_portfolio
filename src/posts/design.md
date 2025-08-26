---
layout: layouts/post.njk
title: Static Art & Design
description:
date: 2024-06-10
thumbnail: /assets/95731519-6287-4bbd-a281-712ac2b13fef-radial.jpg
images:
  - /assets/95731519-6287-4bbd-a281-712ac2b13fef-wildflower.png
  - /assets/95731519-6287-4bbd-a281-712ac2b13fef-cover.png
  - /assets/95731519-6287-4bbd-a281-712ac2b13fef-AEposter2.png
  - /assets/95731519-6287-4bbd-a281-712ac2b13fef-Instagram.png
  - /assets/95731519-6287-4bbd-a281-712ac2b13fef-radial.jpg
  - /assets/2decb767-8051-4237-974a-927409aa4233-IMG_5895.JPG
  - /assets/2decb767-8051-4237-974a-927409aa4233-IMG_5896.JPG
  - /assets/2decb767-8051-4237-974a-927409aa4233-IMG_5893.JPG
  - /assets/2decb767-8051-4237-974a-927409aa4233-IMG_5894.JPG
  - /assets/2decb767-8051-4237-974a-927409aa4233-Lee-Olivia-RecordingFinal.png
  - /assets/2decb767-8051-4237-974a-927409aa4233-Lee-Olivia-RecordingStudies.png
  - /assets/2decb767-8051-4237-974a-927409aa4233-Olivia-Lee_FBC.png
tags:
  - static
  - all
blurb:
skills:
  - Figma
  - Adobe Suite
  - Collage
---

<div class="skill-list">       
  <h4 style="font-size: 1rem; color: #fe2f20;">Softwares & Languages Used:</h4>
      <div class="skills">   
    {%- for post in collections.posts -%}
  {%- if post.url == page.url -%}
    {%- if post.data.skills and post.data.skills.length > 0 -%}
      {%- for skill in post.data.skills -%}
     <h4 style="font-size: 1rem;"> {{skill}} </h4> 
      {%- endfor -%}
    {%- endif -%}
  {%- endif -%}
{%- endfor -%}  
    </div> 
  </div>
