---
title: Parametrics
date: 2024-12-04
animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-flower.mp4
sites:
  - animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-flower.mp4
    link: https://olivia-em.github.io/codeyourway/recode/screensaver/index.html
    title: Screensaver
  - animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-ball.mp4
    link: https://olivia-em.github.io/codeyourway/explore/explore2/index.html
    title: Explore 2
  - animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-para1.mp4
    link: https://olivia-em.github.io/codeyourway/explore/explore3/index.html
    title: Explore 3
  - animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-lights.mp4
    link: https://olivia-em.github.io/codeyourway/explore/explore4/index.html
    title: Explore 4
  - animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-para2.mp4
    link: https://olivia-em.github.io/codeyourway/explore/explore5/index.html
    title: Explore 5
  - image: /assets/preloader.png
    link: https://olivia-em.github.io/codeyourway/recode/preLoader/index.html
    title: preLoader
tags: 
  - code 
  - all
repo: 
  - title: Github Repository
    link: https://github.com/olivia-em/codeyourway
skills:
  - p5.js
  - WEBGL
blurb: A collection of parametric sketches exploring generative design and interactive animations. These p5.js experiments focus on mathematical patterns, organic forms, and dynamic visual systems that respond to user input or evolve over time.
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
