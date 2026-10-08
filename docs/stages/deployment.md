---
title: Docker en deployment
description: Maak van een notebook een service die overal op dezelfde manier draait.
---

# Docker en deployment

<p class="rm-lede">Vacatures vragen om applicaties, niet om notebooks. In deze fase neem je een werkend prototype, verpak je het in een API, zet je het in een container en laat je het ergens anders draaien dan op je eigen laptop.</p>

<div class="rm-meta" markdown>
<span>Fase 5 van 9</span>
<span>Ongeveer 3,5 uur</span>
<span>Bouwt voort op: je ervaring met Azure en Git</span>
</div>

!!! curating "Deze fase wordt nog samengesteld"
    Cursusonderdelen en oefeningen worden nog gekozen.

## Leren

- [Docker: Get started](https://docs.docker.com/get-started/){ .rm-item .rm-refresh data-source="Docs · Docker" data-time="30 min" } Wat images en containers zijn, en hoe je je eerste bouwt en draait.
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/){ .rm-item data-source="Docs · FastAPI" data-time="1 uur" } Maak van een Python-functie een web-API met automatische documentatie.

## Interviewvragen

??? interview rm-refresh "Welk probleem lost Docker op?"
    "Het werkt op mijn machine." Een container verpakt je code samen met de exacte dependencies en runtime, zodat het hetzelfde draait op je laptop, in CI en in de cloud. Het maakt deployments ook herhaalbaar: je levert een image op, geen lijst met installatiestappen.

??? interview rm-refresh "Hoe zou je een LLM-applicatie beschikbaar maken voor andere teams?"
    Verpak het in een **API** (bijvoorbeeld FastAPI) met een duidelijk schema voor verzoeken en antwoorden, zet het in een **container** en draai het op een managed platform zoals Azure Container Apps. Voeg authenticatie, rate limiting, timeouts voor trage modelaanroepen en logging toe. Bewaar API-keys in een secret store, nooit in de image.

??? interview rm-refresh "LLM-aanroepen zijn traag. Hoe houd je de applicatie responsief?"
    **Stream** het antwoord zodat gebruikers direct tekst zien; maak aanroepen **asynchroon** zodat één traag verzoek de rest niet blokkeert; **cache** antwoorden op herhaalde vragen; en gebruik een kleiner, sneller model voor eenvoudige stappen. Langlopende agenttaken kunnen als achtergrondtaak draaien, waarvan de gebruiker later de status bekijkt.
