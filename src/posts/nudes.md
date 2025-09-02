---
layout: layouts/post.njk
title: theNudes
description: 
date: 2023-11-14
thumbnail: /assets/nudes.jpeg
images: 
videos:
  - /assets/theNudes.mp4
tags: 
  - vidart 
  - all
blurb: 
skills:
  - Adobe After Effects
  - Adobe Firefly 
documentation: 
  - https://olivia-em.github.io/docblog/projects/generativevid/
---
 <br>
 <div class="cont">
   <p class="desc">
     Tasked with using AI for a short video assignment, I decided to go in a more understated direction. I used excerpts from Anne Carson's Glass, Irony, and God as prompts for image generation in Adobe Firefly. The excerpts I chose are visions that come to the protagonist. Considering the discourse around AI and its relationship to the arts, which frames it as hallucinatory rather than realistic, I thought using these visions as prompts would be fitting. 
    </p>
 </div>
<div class="skill-list">       
  <h4 style="font-size: 1rem; color: #fe2f20;">Softwares Used:</h4> 
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
  