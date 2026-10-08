---
title: MCP en skills
description: Standaardmanieren om agents tools, data en instructies te geven.
---

# MCP en skills

<p class="rm-lede">MCP is een standaardmanier om tools en databronnen aan elke AI-applicatie te koppelen; skills zijn verpakte instructies die een agent pas laadt als hij ze nodig heeft.</p>

<div class="rm-meta" markdown>
<span>Fase 7 van 9</span>
<span>Ongeveer 3 uur</span>
<span>Bouwt voort op: agents en tool calling</span>
</div>

!!! curating "Deze fase wordt nog samengesteld"
    Cursusonderdelen en oefeningen worden nog gekozen.

## Leren

- [What is the Model Context Protocol?](https://modelcontextprotocol.io/docs/getting-started/intro){ .rm-item .rm-refresh data-source="Docs · MCP" data-time="15 min" } De officiële introductie: wat MCP is en waarom het bestaat.
- [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills){ .rm-item data-source="Docs · GitHub" data-time="15 min" } Hoe skills werken in GitHub Copilot, inclusief waar je ze in een repository neerzet.

## Interviewvragen

??? interview rm-refresh "Welk probleem lost MCP op?"
    Zonder standaard heeft elke AI-applicatie een eigen maatwerkkoppeling nodig voor elke tool of databron. MCP definieert één protocol: je bouwt één keer een **MCP-server** (bijvoorbeeld voor je database of ticketsysteem), en elke MCP-compatibele client (Claude, Copilot, je eigen agent) kan hem gebruiken. Het wordt vaak vergeleken met USB-C voor AI-tools.

??? interview rm-refresh "Wat is het verschil tussen een tool, een MCP-server en een skill?"
    Een **tool** is één functie die het model kan aanroepen. Een **MCP-server** is een programma dat een set tools (en data) aanbiedt aan elke compatibele client via een standaardprotocol. Een **skill** is een map met instructies, en eventueel scripts, die een agent vertelt *hoe* hij een bepaald soort taak uitvoert; de agent laadt hem alleen als dat relevant is, wat zijn context klein houdt.

??? interview rm-refresh "Wat zijn de securityrisico's van een MCP-server koppelen?"
    Een MCP-server kan code uitvoeren en bij data komen met alle rechten die je hem geeft, en zijn toolbeschrijvingen zijn tekst die het model leest. Een kwaadaardige of gecompromitteerde server kan dus instructies injecteren. Gebruik alleen servers die je vertrouwt, geef ze minimale rechten en controleer welke tools ze aanbieden.
