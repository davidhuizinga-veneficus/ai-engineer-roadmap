---
title: Agents en tool calling
description: Laat een LLM in een loop zelf bepalen welke tools het aanroept, tot een taak klaar is.
---

# Agents en tool calling

<p class="rm-lede">Met prompting vertel je een model wat het moet zeggen. Met een agent laat je het model bepalen wat het moet <em>doen</em>: het kiest een tool, leest het resultaat en herhaalt dat tot de taak klaar is. Interviewers willen horen dat je het verschil kent, en wanneer een vaste workflow de betere keuze is.</p>

<div class="rm-meta" markdown>
<span>Fase 3 van 9</span>
<span>Ongeveer 4 uur</span>
<span>Bouwt voort op: LLM-basiskennis</span>
</div>

## Wat je moet kunnen uitleggen

- Hoe **tool calling** werkt: het model geeft een gestructureerd verzoek terug ("roep `get_weather` aan met `city="Utrecht"`"), *jouw code* voert de tool uit, en het resultaat gaat terug het gesprek in.
- De **agent loop**: model → tool call → resultaat van de tool → model, tot het model antwoordt zonder een tool aan te roepen.
- Het verschil tussen een **workflow** (jij legt de stappen vast in code) en een **agent** (het model kiest de stappen), en waarom de meeste productiesystemen vooral workflow zijn.
- Wat een agent-**framework** zoals LangGraph toevoegt aan die loop: state, vertakkingen, retries, geheugen en stappen waarin een mens goedkeuring geeft.

## Leren

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents){ .rm-item .rm-refresh data-source="Artikel · Anthropic" data-time="20 min" } De helderste uitleg van workflows tegenover agents, met de gangbare patronen bij naam genoemd. Lees dit als eerste.
- [Function calling guide](https://platform.openai.com/docs/guides/function-calling){ .rm-item data-source="Docs · OpenAI" data-time="25 min" } Hoe je een tool aan het model beschrijft en hoe het verzoek en antwoord eruitzien. Hetzelfde idee werkt bij elke provider.
- [Hugging Face Agents Course, Unit 1](https://huggingface.co/learn/agents-course/unit1/introduction){ .rm-item data-source="Cursus · Hugging Face" data-time="1,5 uur" } Gratis, praktische introductie tot de cyclus van denken → actie → observatie.
- [Designing Agentic Systems with LangChain](https://www.datacamp.com/courses/designing-agentic-systems-with-langchain){ .rm-item data-source="Cursus · DataCamp" data-time="Ongeveer 1 uur, hoofdstuk 1" } Doe hoofdstuk 1, "The Essentials of LangChain agents": tool calling en ReAct-agents met praktische oefeningen. Hoofdstuk 2–3 (chatbots met LangGraph) zijn optionele verdieping.

## Oefenen

- [Build your first agent with tools](https://huggingface.co/learn/agents-course/unit1/tutorial){ .rm-item .rm-exercise data-source="Oefening · Hugging Face" data-time="45 min" } Geef een agent twee tools en kijk hoe hij bepaalt welke hij gebruikt.
- [Introduction to LangGraph, module 1](https://academy.langchain.com/courses/intro-to-langgraph){ .rm-item .rm-exercise data-source="Oefening · LangChain Academy" data-time="1 uur" } Bouw de agent loop opnieuw als graph, zodat je elke stap ziet die hij zet.

## Verdieping { .rm-full-only }

- [AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/){ .rm-item data-source="Korte cursus · DeepLearning.AI" data-time="1,5 uur" } Bouwt eerst een agent vanaf nul en daarna met LangGraph, inclusief persistence en human-in-the-loop.
- [Hugging Face Agents Course, volledige cursus](https://huggingface.co/learn/agents-course){ .rm-item data-source="Cursus · Hugging Face" data-time="Meerdere dagen" } Frameworks naast elkaar vergeleken, plus een eindproject met een agent en een certificaat.

## Check je begrip

??? selfcheck "Wie voert de tool eigenlijk uit: het model of jouw code?"
    Jouw code. Het model geeft alleen een gestructureerd verzoek terug met de naam van de tool en de argumenten. Jouw programma voert de tool uit en stuurt het resultaat als nieuw bericht terug naar het model. Het model komt nooit zelf aan je database of API.

??? selfcheck "Wanneer stopt de agent loop?"
    Als het model een gewoon antwoord geeft in plaats van nog een tool call. In de praktijk stel je ook een maximaal aantal stappen in, zodat een verwarde agent niet eindeloos doorloopt en tokens verbrandt.

??? selfcheck "Noem een taak waarvoor je een vaste workflow zou kiezen in plaats van een agent."
    Bijvoorbeeld: "vat elk binnenkomend supportticket samen en geef het een categorie". De stappen zijn altijd hetzelfde, dus ze vastleggen in code is goedkoper, sneller en beter te testen dan een model laten beslissen.

## Interviewvragen

??? interview rm-refresh "Wat is het verschil tussen een LLM-workflow en een agent?"
    In een **workflow** bepaalt de developer de volgorde van stappen in code: eerst ophalen, dan samenvatten, dan classificeren. Bij een **agent** bepaalt het model tijdens het draaien de volgende stap, en dus welke tool het aanroept, op basis van wat het tot nu toe heeft gezien. Workflows zijn voorspelbaar en goedkoop; agents kunnen open taken aan, maar zijn lastiger te testen en te beheersen. Een goed antwoord voegt toe: begin met een workflow en maak een onderdeel pas agentic als de stappen echt niet vooraf te bepalen zijn.

??? interview rm-refresh "Leg uit wat er gebeurt tijdens één tool call."
    1. Je stuurt het gesprek mee, plus een lijst met toolbeschrijvingen (naam, doel, JSON-schema van de argumenten).
    2. Het model antwoordt met een tool call in plaats van tekst: de naam van de tool en de argumenten als JSON.
    3. Jouw code valideert de argumenten en voert de tool uit.
    4. Je voegt het resultaat toe aan het gesprek en roept het model opnieuw aan.
    5. Het model roept nog een tool aan of geeft het eindantwoord.

??? interview rm-refresh "Hoe voorkom je dat een agent in productie ontspoort?"
    Noem meerdere lagen: een **maximaal aantal stappen** en een budget voor tokens of kosten; **argumenten valideren** voordat je iets uitvoert; tools de **minste rechten** geven die ze nodig hebben (waar mogelijk alleen-lezen); **menselijke goedkeuring** voor onomkeerbare acties zoals e-mails versturen of betalingen doen; en **elke stap loggen** (tracing), zodat je kunt zien waarom het misging.

??? interview "Wat geeft een framework als LangGraph je ten opzichte van de loop zelf schrijven?"
    De loop zelf is ongeveer twintig regels code. Een framework voegt de onderdelen toe die op schaal lastig worden: expliciete **state** die tussen stappen wordt doorgegeven, **vertakkingen** en cycli als graph, **persistence** zodat een run kan pauzeren en hervatten, **human-in-the-loop**-momenten, streaming en ingebouwde tracing. De keerzijde is een extra abstractie om te leren en te debuggen. Interviewers horen graag dat je het ook zonder framework zou kunnen bouwen.

??? interview "Hoe schrijf je een goede toolbeschrijving?"
    Behandel het als documentatie voor een nieuwe collega: een duidelijke naam, één zin over *wanneer* je de tool gebruikt (en wanneer niet), precieze namen en types voor de argumenten, en voorbeelden van geldige waarden. Houd het aantal tools klein en hun doelen duidelijk verschillend; overlappende tools zijn de meest voorkomende reden dat een model de verkeerde kiest.

??? interview "Hoe test je een agent?"
    Test de **tools** als gewone functies met unit tests. Test de **agent** met een vaste set voorbeeldtaken en controleer de uitkomst *en* de route: riep hij de juiste tools aan, in een logische volgorde, binnen het stappenbudget? Omdat de output varieert, draai je elke case meerdere keren en houd je een slagingspercentage bij in plaats van exacte overeenkomsten te verwachten. Meer hierover in de evaluatiefase.
