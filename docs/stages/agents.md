---
title: Agents and tool calling
description: Let an LLM decide which tools to call, in a loop, until a task is done.
---

# Agents and tool calling

<p class="rm-lede">Prompting tells a model what to say. An agent lets the model decide what to <em>do</em>: it picks a tool, reads the result, and repeats until the task is finished. Interviewers want to hear that you know the difference, and when a fixed workflow is the better choice.</p>

<div class="rm-meta" markdown>
<span>Stage 3 of 9</span>
<span>About 4 hours</span>
<span>Builds on: LLM foundations</span>
</div>

## What you should be able to explain

- How **tool calling** works: the model returns a structured request ("call `get_weather` with `city="Utrecht"`"), *your code* runs the tool, and the result goes back into the conversation.
- The **agent loop**: model → tool call → tool result → model, until the model answers without calling a tool.
- The difference between a **workflow** (you hard-code the steps) and an **agent** (the model chooses the steps), and why most production systems are mostly workflow.
- What an agent **framework** like LangGraph adds on top of that loop: state, branching, retries, memory, human approval steps.

## Learn

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents){ .rm-item .rm-refresh data-source="Article · Anthropic" data-time="20 min" } The clearest explanation of workflows versus agents, with the common patterns named. Read this first.
- [Function calling guide](https://platform.openai.com/docs/guides/function-calling){ .rm-item data-source="Docs · OpenAI" data-time="25 min" } How a tool is described to the model and what the request and response look like. The same idea works with every provider.
- [Hugging Face Agents Course, Unit 1](https://huggingface.co/learn/agents-course/unit1/introduction){ .rm-item data-source="Course · Hugging Face" data-time="1.5 hours" } Free, hands-on introduction to the thought → action → observation cycle.
- [Designing Agentic Systems with LangChain](https://www.datacamp.com/courses/designing-agentic-systems-with-langchain){ .rm-item data-source="Course · DataCamp" data-time="About 1 hour, chapter 1" } Do chapter 1, "The Essentials of LangChain agents": tool calling and ReAct agents with hands-on exercises. Chapters 2–3 (chatbots with LangGraph) are optional extra depth.

## Practise

- [Build your first agent with tools](https://huggingface.co/learn/agents-course/unit1/tutorial){ .rm-item .rm-exercise data-source="Exercise · Hugging Face" data-time="45 min" } Give an agent two tools and watch it decide which to use.
- [Introduction to LangGraph, module 1](https://academy.langchain.com/courses/intro-to-langgraph){ .rm-item .rm-exercise data-source="Exercise · LangChain Academy" data-time="1 hour" } Rebuild the agent loop as a graph, so you can see every step it takes.

## Go deeper { .rm-full-only }

- [AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/){ .rm-item data-source="Short course · DeepLearning.AI" data-time="1.5 hours" } Builds an agent from scratch first, then with LangGraph, including persistence and human-in-the-loop.
- [Hugging Face Agents Course, full course](https://huggingface.co/learn/agents-course){ .rm-item data-source="Course · Hugging Face" data-time="Several days" } Frameworks compared side by side, plus a final agent project with a certificate.

## Check your understanding

??? selfcheck "Who actually runs the tool: the model or your code?"
    Your code. The model only returns a structured request with the tool name and arguments. Your program executes the tool, then sends the result back to the model as a new message. The model never touches your database or API directly.

??? selfcheck "When does the agent loop stop?"
    When the model replies with a normal answer instead of another tool call. In practice you also add a maximum number of steps, so a confused agent can't loop forever and burn tokens.

??? selfcheck "Name one task where you would choose a fixed workflow over an agent."
    For example: "summarise every incoming support ticket and tag its category". The steps are always the same, so hard-coding them is cheaper, faster and easier to test than letting a model decide.

## Interview questions

??? interview rm-refresh "What is the difference between an LLM workflow and an agent?"
    In a **workflow**, the developer decides the sequence of steps in code: retrieve, then summarise, then classify. In an **agent**, the model decides the next step at runtime, choosing which tool to call, based on what it has seen so far. Workflows are predictable and cheap; agents handle open-ended tasks but are harder to test and control. A good answer adds: start with a workflow and only make a part agentic when the steps genuinely can't be known in advance.

??? interview rm-refresh "Walk me through what happens during a single tool call."
    1. You send the conversation plus a list of tool descriptions (name, purpose, JSON schema of the arguments).
    2. The model replies with a tool call instead of text: the tool name and arguments as JSON.
    3. Your code validates the arguments and runs the tool.
    4. You append the tool result to the conversation and call the model again.
    5. The model either calls another tool or gives the final answer.

??? interview rm-refresh "How would you stop an agent from going off the rails in production?"
    Mention several layers: a **maximum number of steps** and a token or cost budget; **validating tool arguments** before running anything; giving tools the **least privilege** they need (read-only where possible); **human approval** for irreversible actions like sending email or making payments; and **logging every step** (tracing) so you can see why it went wrong.

??? interview "What does a framework like LangGraph give you over writing the loop yourself?"
    The loop itself is about twenty lines of code. A framework adds the parts that get hard at scale: explicit **state** passed between steps, **branching** and cycles as a graph, **persistence** so a run can pause and resume, **human-in-the-loop** checkpoints, streaming, and built-in tracing. The trade-off is an extra abstraction to learn and debug. Interviewers like to hear that you could build it without the framework.

??? interview "How do you write a good tool description?"
    Treat it like documentation for a new colleague: a clear name, one sentence on *when* to use the tool (and when not to), precise argument names and types, and examples of valid values. Keep the number of tools small and their purposes distinct; overlapping tools are the most common reason a model picks the wrong one.

??? interview "How would you test an agent?"
    Test the **tools** as normal functions with unit tests. Test the **agent** with a fixed set of example tasks and check the outcome *and* the path: did it call the right tools, in a sensible order, within the step budget? Because outputs vary, run each case several times and track a pass rate rather than expecting exact matches. More in the evaluation stage.
