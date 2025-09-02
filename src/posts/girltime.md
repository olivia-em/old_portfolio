---
layout: layouts/post.njk
title: Girl Time
date: 2025-11-14
repo:
  - title: Github Repository
    link: https://github.com/olivia-em/GirlTime
  - title: Other Documentation
    link: https://prishajain.notion.site/girltime
thumbnail: /assets/95731519-6287-4bbd-a281-712ac2b13fef-IMG_7812.JPG
media:
  - type: image
    src: /assets/95731519-6287-4bbd-a281-712ac2b13fef-IMG_7635.JPG
  - type: image
    src: /assets/95731519-6287-4bbd-a281-712ac2b13fef-IMG_7587.JPG
  - type: video
    src: /assets/95731519-6287-4bbd-a281-712ac2b13fef-IMG_1361_2.mov
  - type: image
    src: /assets/95731519-6287-4bbd-a281-712ac2b13fef-IMG_1364.jpg
  - type: video
    src: /assets/95731519-6287-4bbd-a281-712ac2b13fef-girltime-vid.MOV
  - type: image
    src: /assets/95731519-6287-4bbd-a281-712ac2b13fef-IMG_7103.JPG
  - type: image
    src: /assets/95731519-6287-4bbd-a281-712ac2b13fef-IMG_7168.JPG
  - type: video
    src: /assets/IMG_7219.MOV

tags:
  - code
  - vidart
  - all
blurb: |
  Girl Time is an immersive installation, created in collaboration with Prisha Jain and dedicated to sharing femme stories. This installation draws inspiration from the deeply personal conversations that unfold in women's restrooms—spaces of vulnerability, camaraderie, and unfiltered expression. Through interactive and generative elements, Girl Time invites users to step into the experience of being female-identifying, capturing its beauty and struggle. No two users will have the same experience, the same way no two women do.

  Girl Time comes together using Arduino, p5.js, and Tone.js. The removable objects are magnetized, and the magnets are detected by hall effect sensors. Through serial communication, the sensors send messages to p5, which initiates sound and video corresponding to the object, with added randomness.
skills:
  - Arduino IDE
  - p5.js
  - tone.js
  - Adobe Creative Suite
  - CAD & Design for Fabrication
  - Rapid Prototyping
documentation:
---
     <div style="margin-top:20px;color: #fe2f20;" class="skills">   
     {%- for post in collections.posts -%}
{%- if post.url == page.url -%}
{%- if post.data.repo and post.data.repo.length > 0 -%}
{%- for rep in post.data.repo -%}
<a target="_blank" href="{{ rep.link }}"><h6 style="color: #fe2f20; text-align:center;">
< {{ rep.title }} ></h6></a>
{%- endfor -%}
{%- endif -%}
{%- endif -%}
{%- endfor -%}
    </div>
<div class="skill-list">       
  <h4 style="font-size: 1rem; color: #fe2f20;">Skills:</h4> 
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

