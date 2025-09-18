---
title: Mozia 2023
date: 2024-12-07
animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-kiln.mp4
sites:
  - image: /assets/2decb767-8051-4237-974a-927409aa4233-mozia-screengrab.png
    link: https://mozia-2023.glitch.me/
    title: Mozia 2023
    animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-kiln.mp4
tags: 
  - webdev 
  - all
layout: layouts/post.njk
skills:
  - HTML/CSS
  - 3D Model Viewer
  - Glitch
  - Leaflet.js
  - QGIS
  - Agisoft Metashape
blurb: I received a summer fellowship from the Price Lab at the University of Pennsylvania in 2023 to explore the intersection of digital archaeology and digital humanities. I intended to use data from an archaeological excavation I was working on to design my own project which combines the GIScience / 3D visualization with web design. I built this website on Glitch using HTML, CSS, and Javascript, including the Leaflet.js library. On the page, Il Forno, you can experience the excavation of a kiln through images, orthomosaics, and 3D models, while I explain how these assets were created, walk you through the excavation, and briefly discuss potential for growth.
---

<!-- <div class="sites-container">
{%- for post in collections.posts -%}                           
  {%- if post.url == page.url -%} 
    {%- for site in post.data.sites -%}
    <a target="_blank" href="{{ site.link }}">
      {% if site.animation %}
        <div class="sites video-background">
          <video autoplay loop muted playsinline class="video-content">
            <source src="{{ site.animation | url }}" type="video/mp4">
            Your browser does not support the video tag.
          </video>
          <h4 class="overlay-content">
            < {{ site.title }} >
          </h4>
        </div>
      {% else %}
        <div class="sites" style="background-image: url('{{ site.image | url }}');">
          <h4 class="overlay-content">
            < {{ site.title }} >
          </h4>
        </div>
      {% endif %}
    </a>
  {%- endfor -%}
  {%- endif -%}
{%- endfor -%}
</div>
 -->

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

