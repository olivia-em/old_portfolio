---
title: Encode
date: 2023-12-07
animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-circles2.mp4
sites:
  - image: /assets/encode1.png
    link: https://olivia-em.github.io/codeyourway/encode/encode1/index.html
    title: Encode 1
  - image: /assets/encode2.png
    link: https://olivia-em.github.io/codeyourway/encode/encode2/index.html
    title: Encode 2
  - image: /assets/encode3.png
    link: https://olivia-em.github.io/codeyourway/encode/encode3/index.html
    title: Encode 3
  - image: /assets/encode4.png
    link: https://olivia-em.github.io/codeyourway/encode/encode4/index.html
    title: Encode 4
  - image: /assets/95731519-6287-4bbd-a281-712ac2b13fef-encode7.jpg
    link: https://olivia-em.github.io/codeyourway/encode/encode7/index.html
    title: Encode 7
tags: 
  - code 
  - all
repo: 
  - title: Github Repository
    link: https://github.com/olivia-em/codeyourway
  - title: Workflow
    link: https://olivia-em.github.io/docblog/cyw/week1/
skills:
  - p5.js
  - WEBGL
blurb: Encoding is a learning / experimentation process where you look at a sketch and attempt to recreate it in pseudocode. Then, you take some time to rewrite the code into something of your own creation. This helps me breakdown an output into smaller components that can be described by and then train myself to use those to recreate it. This can also help you recreate non-coded art into Javascript. This is a selection of Javascript sketches I made using this process, and all are either interactive or animated. In the repository link above, each .js file has the original code commented out at the bottom. 
layout: layouts/post.njk
---
   
<div class="sites-container">
  {%- for post in collections.posts -%}                           
    {%- if post.url == page.url -%} 
      {%- for site in post.data.sites -%}
        <a target="_blank" href="{{ site.link }}">
          {% if site.animation %}
            <!-- Render video if animation exists -->
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
            <!-- Otherwise, use image as background -->
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
