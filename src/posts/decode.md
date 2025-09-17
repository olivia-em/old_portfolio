---
title: Decode
date: 2023-12-07
thumbnail: /assets/95731519-6287-4bbd-a281-712ac2b13fef-decode3-min.jpg
sites:
  - animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-rects.mp4
    link: https://olivia-em.github.io/codeyourway/decode/decode8/index.html
    title: Decode 8
  - image: /assets/decode10.png
    link: https://olivia-em.github.io/codeyourway/decode/decode10/index.html
    title: Decode 10
  - image: /assets/decode11.png
    link: https://olivia-em.github.io/codeyourway/decode/decode11/index.html
    title: Decode 11
  - image: /assets/2decb767-8051-4237-974a-927409aa4233-decode1-min.png
    link: https://olivia-em.github.io/codeyourway/decode/decode1/index.html
    title: Decode 1
  - animation: /assets/95731519-6287-4bbd-a281-712ac2b13fef-decode3.mp4
    link: https://olivia-em.github.io/codeyourway/decode/decode3/index.html
    title: Decode 3
  - image: /assets/2decb767-8051-4237-974a-927409aa4233-decode4-min.png
    link: https://olivia-em.github.io/codeyourway/decode/decode4/index.html
    title: Decode 4
tags: 
  - code 
  - all
repo: 
  - https://github.com/olivia-em/codeyourway
blog:
 - https://olivia-em.github.io/docblog/cyw/week2/
skills:
  - p5.js
  - WEBGL
layout: layouts/post.njk
---


<div class="cont">
  
  <div class="skills">   
        {%- for post in collections.posts -%}
  {%- if post.url == page.url -%}
    {%- if post.data.blog and post.data.blog.length > 0 -%}
      {%- for blo in post.data.blog -%}

 <h4 style="color: #fe2f20;"> <a target="_blank" style="color: #fe2f20;" href="{{blog}}">
    Workflow
    </a></h4>
      {%- endfor -%}
    {%- endif -%}
  {%- endif -%}
{%- endfor -%} 
      
      {%- for post in collections.posts -%}
  {%- if post.url == page.url -%}
    {%- if post.data.repo and post.data.repo.length > 0 -%}
      {%- for rep in post.data.repo -%}
  <h4 style="color: #fe2f20;"><a target="_blank" style="color: #fe2f20;" href="{{repo}}">
    Repository
   </a></h4>
      {%- endfor -%}
    {%- endif -%}
  {%- endif -%}
{%- endfor -%} 
      </div>      
  
  <p class="desc">
    <i>Decoding</i> is a learning / experimentation process where you predict a sketch just based on reading the code. Then, you take some time to rewrite the code into
    something of your own creation. This helps me understand and therefore predict the functionality of various code conventions and then train myself to use those
    conventions in my own style. 
  </p>
  <p class="desc">
    This is a selection of Javascript sketches I made using this process, and all are either interactive or animated. In the repository link above, each .js file has the original code commented out at the bottom. 
    </p>
      </div>
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
