AI Market Intelligence Platform
1. Vision
Project Vision

Build an AI-powered Market Intelligence Platform capable of automatically collecting, processing, analyzing and summarizing market information to assist business decision-making.

Instead of simply answering questions, the system should proactively perform market research tasks like a professional Market Intelligence Analyst.

2. MVP Scope
MVP Industry

China E-commerce Market

Covered Companies
Alibaba (Taobao / Tmall)
JD.com
Pinduoduo
Douyin E-commerce
Kuaishou E-commerce
MVP Objectives

The first version should automatically:

Collect daily market news
Organize market information
Analyze competitors
Generate AI-powered market summaries
Export a daily market report

3. Project Architecture
                User

                 │

                 ▼

         Command Line / Dashboard

                 │

                 ▼

     Market Intelligence Agent

                 │

        Planning & Reasoning

                 │

     ┌───────────┼────────────┐

     ▼           ▼            ▼

 News Tool  Analytics Tool Database Tool

     │           │            │

     └───────────┼────────────┘

                 ▼

          Data Processing

                 ▼

            Local Database

                 ▼

          Generated Reports

4. Project Workflow

The workflow follows five major stages.

Stage 1

Data Collection

Collect market information from multiple public sources.

Examples:

Company news
Industry reports
Government statistics
Public announcements

Output:

data/raw/

Stage 2

Data Processing

Clean and standardize collected data.

Tasks include:

Remove duplicates
Normalize dates
Standardize company names
Extract keywords

Output:

data/processed/

Stage 3

Analytics

Generate structured business insights.

Examples:

Competitor comparison
Industry trends
Keyword frequency
Market sentiment

Stage 4

AI Agent

The Agent receives a business objective.

Example:

Generate today's China E-commerce Market Report.

Instead of directly generating text, the Agent should:

Decide what information is needed.
Call appropriate tools.
Gather required evidence.
Analyze findings.
Generate business insights.

Stage 5

Report Generation

Generate:

Markdown Report
PDF Report (Future)
Dashboard (Future)

5. Folder Responsibilities
Folder	Responsibility
src/collectors	Collect external market information
src/database	Store and query structured market data
src/analytics	Generate statistical analysis and KPIs
src/llm	AI prompts, tools and Agent implementation
data/raw	Original collected data
data/processed	Cleaned datasets
reports	Generated reports
dashboard	User interface
notebooks	Experimentation only
6. AI Agent Design

The Agent is the central coordinator.

Instead of answering questions directly, it performs tasks using available tools.

The Agent owns three capabilities:

Planning

Determine what information is required.

Reasoning

Interpret collected information.

Tool Calling

Invoke different modules.

Example:
Task

↓

Analyze JD.com's competitive position

↓

Agent

↓

Search News

↓

Load Company Data

↓

Analyze Competitors

↓

Generate Summary

7. Future Iterations

Version 1

China E-commerce Daily Report

Version 2

Interactive Dashboard

Version 3

Support Multiple Industries

Examples:

EV
Consumer Electronics
Retail

Version 4

Multi-Agent Collaboration

Examples:

Research Agent

↓

Analytics Agent

↓

Report Agent

Version 5

Fully Autonomous Market Intelligence Platform

8. Guiding Principles

The project should follow four principles.

Automation

Minimize manual work.

Scalability

New industries should be added easily.

Modularity

Every component should be independently replaceable.

Explainability

Every AI-generated insight should be traceable back to collected evidence.