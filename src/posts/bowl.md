---
title: Incantation Bowl
date: 2024-12-07
animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-bowl.mp4
repo:
  - title: Workflow
    link: https://incantationbowl.glitch.me/workflow.html
sites:
  - image: /assets/2decb767-8051-4237-974a-927409aa4233-bowl.png
    link: https://incantationbowl.glitch.me/
    title: Incantation Bowl
    animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-bowl.mp4
tags:
  - all
  - webdev
layout: layouts/post.njk
skills:
  - HTML/CSS/Javascript
  - 3D Model Viewer
  - Agisoft Metashape
  - Blender
blurb: This was the precursor to Mozia 2023 and the final project for a course in digital archaeology. We had to focus on a specific object at the Penn Museum and present it in a new light. I coded the website on Glitch in HTML & CSS, and photogrammetically 3D modeled the artifact then rendered it in Agisoft Metashape.
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
</div> -->

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

