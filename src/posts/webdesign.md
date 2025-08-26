---
title: Smaller Projects
thumbnail: /assets/2decb767-8051-4237-974a-927409aa4233-justbones.png
date: 2023-12-07
sites:
  - image: /assets/95731519-6287-4bbd-a281-712ac2b13fef-port-ex.jpg
    link: https://oliviaemlee.glitch.me/
    title: Former Portfolio
  - image: /assets/2decb767-8051-4237-974a-927409aa4233-justbones.png
    link: https://olivia-em.github.io/justBones/
    title: justBones
  - image: /assets/2decb767-8051-4237-974a-927409aa4233-docblog.png
    link: https://docblog-olee.glitch.me/
    title: ITP Documentation Blog
  - image: /assets/2decb767-8051-4237-974a-927409aa4233-desktopp.png
    link: https://olivia-em.github.io/dsgn1020/
    title: DSGN Desktop
  - image: /assets/2decb767-8051-4237-974a-927409aa4233-meam-screengrab.png
    link: https://meamlabs.seas.upenn.edu/
    title: MEAM Labs
  - image: /assets/2decb767-8051-4237-974a-927409aa4233-sounddevils.png
    link: https://olivia-em.github.io/dsgn1020/s3a2/
    title: IFTTT Applet
  - image: /assets/2decb767-8051-4237-974a-927409aa4233-IMG_9231.jpg
    link: https://olivia-em.github.io/dsgn1020/s1a3/
    title: Looking for a sign?
  - image: /assets/2decb767-8051-4237-974a-927409aa4233-closet.png
    link: https://olivia-em.github.io/dsgn1020/s2a2/
    title: Playing Dress-Up!
tags:
  - webdev
  - all
layout: layouts/post.njk
skills:
  - HTML
  - Javascript
  - CSS & CSS Animations
  - Wordpress
  - Glitch
  - Github Pages
---

<div class="sites-container">
{%- for post in collections.posts -%}                           
  {%- if post.url == page.url -%} 
    {%- for site in post.data.sites -%}
    <a target="_blank" href="{{ site.link }}">
      <div style="background-image: url('{{ site.image }}');" class="sites">
        <h4>
          < {{ site.title }} >
        </h4>
      </div>
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
