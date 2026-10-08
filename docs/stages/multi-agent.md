---
title: Multi-agent systemen
description: Meerdere agents die samenwerken, en waarom dat vaak niet het antwoord is.
---

# Multi-agent systemen

<p class="rm-lede">Multi-agent systemen verdelen een taak over meerdere gespecialiseerde agents. Ze kunnen grote, parallelle onderzoekstaken aan, maar vermenigvuldigen ook de kosten en het aantal plekken waar het mis kan gaan. Interviewers willen vooral horen dat je weet wanneer je ze <em>niet</em> moet gebruiken.</p>

<div class="rm-meta" markdown>
<span>Fase 5 van 9</span>
<span>Ongeveer 10 min</span>
<span>Bouwt voort op: agents</span>
</div>

!!! curating "Deze fase is nog niet compleet"
    Er ontbreekt nog materiaal over patronen voor meerdere agents en over wanneer je ze juist niet gebruikt.

## Leren

- [Multi-Agent Systems Explained](https://www.youtube.com/watch?v=sWH0T4Zez6I){ .rm-item .rm-refresh data-source="Video · IBM Technology" data-time="8 min" } Een korte uitleg van hoe meerdere agents samenwerken.

## Interviewvragen

??? interview rm-refresh "Wanneer zou je meerdere agents gebruiken in plaats van één?"
    Als een taak uiteenvalt in **onafhankelijke delen die parallel kunnen draaien**, zoals meerdere onderwerpen tegelijk onderzoeken, of als de context van één agent zou overlopen. Elke sub-agent werkt in zijn eigen context en geeft een korte samenvatting terug aan een orchestrator. Voor taken waarin elke stap afhangt van de vorige is één agent eenvoudiger en betrouwbaarder.

??? interview rm-refresh "Wat zijn de nadelen van multi-agent systemen?"
    Veel hogere **tokenkosten** (elke agent heeft zijn eigen context), meer **plekken waar het misgaat**, agents die werken met **inconsistente informatie**, en veel lastiger **debuggen** en evalueren. Veel problemen die multi-agent lijken, los je beter op met één agent met goede tools, of met een vaste workflow.

??? interview rm-refresh "Beschrijf het orchestrator–worker-patroon."
    Een **orchestrator**-agent deelt de taak op in deeltaken, geeft elke deeltaak aan een **worker**-agent (vaak parallel) en voegt de resultaten samen. Workers krijgen alleen de context die ze voor hun deel nodig hebben. De orchestrator beslist of het samengevoegde resultaat goed genoeg is of dat er meer werk nodig is.
