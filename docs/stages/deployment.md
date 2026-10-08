---
title: Docker en deployment
description: Maak van een notebook een service die overal op dezelfde manier draait.
---

# Docker en deployment

<p class="rm-lede">Vacatures vragen om applicaties, niet om notebooks. In deze fase neem je een werkend prototype, verpak je het in een API, zet je het in een container en laat je het ergens anders draaien dan op je eigen laptop.</p>

<div class="rm-meta" markdown>
<span>Fase 8 van 9</span>
<span>Ongeveer 4,5 uur</span>
<span>Bouwt voort op: je ervaring met Azure en Git</span>
</div>

!!! curating "Deze fase is nog niet compleet"
    Er ontbreekt nog materiaal over projectstructuur (pyproject.toml en uv).

## Leren

- [Ultimate Docker Bootcamp for ML, GenAI and Agentic AI](https://www.udemy.com/course/mastering-aiml-with-docker/){ .rm-item data-source="Cursus · Udemy" data-time="Ongeveer 2,5 uur, Dockerfile- en Compose-secties" } Docker met voorbeelden uit machine learning: je verpakt een ML-app in een image en draait meerdere services samen met Docker Compose. Sla de laatste twee secties (Docker Model Runner en MCP Toolkit) over, die hebben Docker Desktop en krachtige hardware nodig.
- [Deploying AI into Production with FastAPI](https://www.datacamp.com/courses/deploying-ai-into-production-with-fastapi){ .rm-item data-source="Cursus · DataCamp" data-time="Ongeveer 1 uur 45 min, hoofdstuk 2–3" } Authenticatie met API-keys, rate limiting en async: de zorgen die bij een LLM-service horen. Draait in de browser.

!!! todo "Opfrisvideo nog te kiezen"
    Kies een korte uitlegvideo over Docker voor de opfrisroute van een halve dag.

## Interviewvragen

??? interview rm-refresh "Welk probleem lost Docker op?"
    "Het werkt op mijn machine." Een container verpakt je code samen met de exacte dependencies en runtime, zodat het hetzelfde draait op je laptop, in CI en in de cloud. Het maakt deployments ook herhaalbaar: je levert een image op, geen lijst met installatiestappen.

??? interview rm-refresh "Hoe zou je een LLM-applicatie beschikbaar maken voor andere teams?"
    Verpak het in een **API** (bijvoorbeeld FastAPI) met een duidelijk schema voor verzoeken en antwoorden, zet het in een **container** en draai het op een managed platform zoals Azure Container Apps. Voeg authenticatie, rate limiting, timeouts voor trage modelaanroepen en logging toe. Bewaar API-keys in een secret store, nooit in de image.

??? interview rm-refresh "LLM-aanroepen zijn traag. Hoe houd je de applicatie responsief?"
    **Stream** het antwoord zodat gebruikers direct tekst zien; maak aanroepen **asynchroon** zodat één traag verzoek de rest niet blokkeert; **cache** antwoorden op herhaalde vragen; en gebruik een kleiner, sneller model voor eenvoudige stappen. Langlopende agenttaken kunnen als achtergrondtaak draaien, waarvan de gebruiker later de status bekijkt.
