---
title: LLM-security
description: Hoe LLM-applicaties worden aangevallen, en hoe je de schade beperkt.
---

# LLM-security

<p class="rm-lede">Het traineeship behandelde security in het algemeen. LLM's brengen nieuwe problemen mee: tekst in een document kan een instructie worden, en een model kan lekken wat het te zien kreeg. Deze fase behandelt de risico's die interviewers je verwachten te kunnen noemen.</p>

<div class="rm-meta" markdown>
<span>Fase 6 van 9</span>
<span>Ongeveer 2,5 uur</span>
<span>Bouwt voort op: de securitymodule van het traineeship</span>
</div>

!!! curating "Deze fase wordt nog samengesteld"
    Cursusonderdelen en oefeningen worden nog gekozen.

## Leren

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/){ .rm-item .rm-refresh data-source="Naslag · OWASP" data-time="30 min" } De standaardlijst met LLM-risico's. Bekijk ze alle tien globaal en lees prompt injection in detail.

## Interviewvragen

??? interview rm-refresh "Wat is prompt injection?"
    Tekst die het model als instructie behandelt, terwijl die uit een onbetrouwbare bron komt: een gebruikersbericht, een webpagina, een e-mail of een opgehaald document. "Negeer je eerdere instructies en…" is het klassieke voorbeeld. *Indirecte* prompt injection, verstopt in content die de applicatie ophaalt, is het lastigere geval, omdat de gebruiker het nooit heeft getypt.

??? interview rm-refresh "Hoe verdedig je je tegen prompt injection?"
    Er bestaat geen volledige oplossing, dus beperk wat een geslaagde aanval kan aanrichten: geef het model en zijn tools de **minste rechten**, vraag **menselijke goedkeuring** voor risicovolle acties, houd onbetrouwbare content duidelijk gescheiden van instructies, **valideer output** voordat je erop handelt, en monitor op ongebruikelijk gedrag. Zeg er duidelijk bij dat alleen prompts filteren niet genoeg is.

??? interview rm-refresh "Welke privacykwesties spelen er als je data naar een LLM-provider stuurt?"
    Persoonsgegevens of vertrouwelijke data verlaten je omgeving, dus je moet weten waar ze worden verwerkt (in de EU?), of de provider ze opslaat of erop traint, en of dat past binnen de AVG en de contracten met je klant. Maatregelen: zakelijke overeenkomsten zonder training op jouw data, hosting in de EU, en persoonsgegevens verwijderen voordat ze worden verstuurd.
