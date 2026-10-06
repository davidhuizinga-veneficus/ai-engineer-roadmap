---
title: MCP and skills
description: Standard ways to give agents tools, data and instructions.
---

# MCP and skills

<p class="rm-lede">Less urgent than the earlier stages, but increasingly mentioned. MCP is a standard way to connect tools and data sources to any AI application; skills are packaged instructions an agent loads only when it needs them.</p>

<div class="rm-meta" markdown>
<span>Stage 7 of 9</span>
<span>About 3 hours</span>
<span>Builds on: agents and tool calling</span>
</div>

!!! curating "This stage is being curated"
    Course sections and exercises are being selected.

## Learn

- [What is the Model Context Protocol?](https://modelcontextprotocol.io/docs/getting-started/intro){ .rm-item .rm-refresh data-source="Docs · MCP" data-time="15 min" } The official introduction: what MCP is and why it exists.
- [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills){ .rm-item data-source="Docs · GitHub" data-time="15 min" } How skills work in GitHub Copilot, including where to put them in a repository.

## Interview questions

??? interview rm-refresh "What problem does MCP solve?"
    Without a standard, every AI application needs its own custom integration for every tool or data source. MCP defines one protocol: you build an **MCP server** once (for example for your database or ticketing system), and any MCP-compatible client (Claude, Copilot, your own agent) can use it. It's often compared to USB-C for AI tools.

??? interview rm-refresh "What is the difference between a tool, an MCP server and a skill?"
    A **tool** is a single function the model can call. An **MCP server** is a program that offers a set of tools (and data) to any compatible client over a standard protocol. A **skill** is a folder of instructions, and optionally scripts, that tells an agent *how* to do a kind of task; the agent loads it only when relevant, which keeps its context small.

??? interview rm-refresh "What are the security risks of connecting an MCP server?"
    An MCP server can run code and access data with whatever permissions you give it, and its tool descriptions are text the model reads, so a malicious or compromised server can inject instructions. Only use servers you trust, give them minimal permissions, and review what tools they expose.
