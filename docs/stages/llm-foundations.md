---
title: LLM-basiskennis
description: Hoe large language models van buitenaf werken, en hoe je er een aanroept vanuit code.
---

# LLM-basiskennis

<p class="rm-lede">Voordat je iets bouwt bovenop een LLM, moet je weten wat je aanroept: wat een token is, waarom dezelfde prompt verschillende antwoorden kan geven, hoe je betrouwbaar structured output krijgt en wat een embedding is.</p>

<div class="rm-meta" markdown>
<span>Fase 1 van 9</span>
<span>Ongeveer 3 uur</span>
<span>Bouwt voort op: je data science-achtergrond</span>
</div>

!!! curating "Deze fase wordt nog samengesteld"
    Cursusonderdelen en oefeningen worden nog gekozen. De essentie hieronder is genoeg voor de opfrisroute van een halve dag.

## Leren

- [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g){ .rm-item .rm-refresh data-source="Video · Andrej Karpathy" data-time="1 uur" } Een rondleiding van een uur langs wat LLM's zijn, hoe ze getraind worden en waar ze de mist in gaan.

## Interviewvragen

??? interview rm-refresh "Wat is een token, en waarom doet dat ertoe voor kosten en limieten?"
    Een token is een stukje tekst dat het model leest en schrijft, vaak een deel van een woord; in het Engels gemiddeld ongeveer vier tekens. Modellen rekenen per input- en outputtoken af, en het context window (hoeveel tekst in één verzoek past) wordt gemeten in tokens. Lange prompts en lange antwoorden kosten dus meer en kunnen tegen de limiet aanlopen.

??? interview rm-refresh "Wat doet temperature?"
    Het bepaalt hoeveel willekeur er is als het model het volgende token kiest. Een lage temperature (bijna 0) laat bijna altijd het meest waarschijnlijke token winnen, wat consistente antwoorden geeft: goed voor extractie en classificatie. Een hogere temperature spreidt de keuze, wat gevarieerdere output geeft: handig voor brainstormen. Het maakt het model niet meer of minder "correct".

??? interview rm-refresh "Hoe krijg je betrouwbaar JSON uit een LLM?"
    Gebruik de **structured output**-functie van de provider met een JSON-schema (bijvoorbeeld via Pydantic), zodat het antwoord in die vorm moet passen. Valideer het daarna alsnog in code, en bepaal wat er gebeurt als het misgaat: opnieuw proberen of terugvallen op iets anders. Alleen in de prompt om JSON vragen werkt meestal, en dat is niet goed genoeg voor productie.
