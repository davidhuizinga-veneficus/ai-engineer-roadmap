---
title: Evaluatie en observability
description: Weet of je LLM-applicatie echt werkt, en zie wat hij in productie doet.
---

# Evaluatie en observability

<p class="rm-lede">"Het zag er goed uit toen ik het probeerde" is geen evaluatie. Deze fase gaat over het omzetten van kwaliteit in cijfers die je kunt volgen, en over genoeg loggen om achteraf een slecht antwoord te begrijpen.</p>

<div class="rm-meta" markdown>
<span>Fase 4 van 9</span>
<span>Ongeveer 3 uur</span>
<span>Bouwt voort op: RAG, agents</span>
</div>

!!! curating "Deze fase wordt nog samengesteld"
    Cursusonderdelen en oefeningen worden nog gekozen.

## Leren

- [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/){ .rm-item .rm-refresh data-source="Artikel · Hamel Husain" data-time="25 min" } Een praktisch pleidooi om vroeg evaluaties te bouwen, van iemand die dat voor zijn werk doet.

## Interviewvragen

??? interview rm-refresh "Hoe evalueer je een LLM-applicatie?"
    Bouw een **testset** van realistische inputs met verwachte uitkomsten, het liefst uit echt gebruik. Beoordeel de output met een mix van **controles in code** (geldige JSON, bevat een bronvermelding), **LLM-as-judge** voor vagere kwaliteiten zoals behulpzaamheid, en **menselijke beoordeling** op een steekproef. Draai dit bij elke wijziging, zodat je ziet of een nieuwe prompt of een nieuw model het beter of slechter maakt.

??? interview rm-refresh "Wat is LLM-as-judge, en wat zijn de risico's?"
    Een (meestal sterk) LLM gebruiken om de output van een ander model te beoordelen op criteria die je zelf opschrijft. Het schaalt veel beter dan menselijke beoordeling. Risico's: de judge heeft eigen voorkeuren (bijvoorbeeld voor langere antwoorden of zijn eigen stijl), en de scores verschuiven als je de judge-prompt aanpast. Toets de judge eerst aan een set door mensen gelabelde voorbeelden voordat je erop vertrouwt.

??? interview rm-refresh "Wat zou je loggen voor een LLM-applicatie in productie?"
    Elk verzoek als **trace**: de input, de volledige prompt die is verstuurd, opgehaalde documenten, tool calls en resultaten, de output, latency, aantallen tokens en kosten, en de modelversie. Plus feedback van gebruikers waar je die hebt. Let op privacy: persoonsgegevens in prompts vragen dezelfde zorg als alle andere persoonsgegevens.
