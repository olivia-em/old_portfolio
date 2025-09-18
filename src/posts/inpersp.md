---
title: Lessons in Perspective
date: 2025-04-21
thumbnail: /assets/LIP.png
sites:
  - image: /assets/LIP.png
    link: https://lessons-inperspective.netlify.app/
    title: Lessons in Perspective
repo: 
  - title: Github Repository
    link: https://github.com/olivia-em/inperspective
tags:
  - webdev
  - code
  - all
layout: layouts/post.njk
skills:
  - React
  - Three.js
  - Creative Writing
blurb: Lessons in Perspective is an interactive, web-based poetry collection that explores how every relationship is shaped by the ones that came before it. Built with React and Three.js, this collection makes the browser a space for 3D concrete poetry. Clicking, rotating, and exploring the 3D environment reveals how meaning changes with perspective; your interaction with the present can unravel the past, illustrating connections that are invisible but felt. Lessons in Perspective offers a poetic meditation on love, memory, and the invisible architectures of life.
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

