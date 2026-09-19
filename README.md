# 🚀 ResearchForge AI

> 🔍 A multi-agent AI research & content generation system that gathers
> insights from multiple sources 🌐, intelligently orchestrates
> specialized agents 🤖, and transforms research into engaging,
> Medium-ready articles ✍️ using Agno.

------------------------------------------------------------------------

## 💡 Overview

**ResearchForge AI** is a multi-agent research and content generation
platform built with **Agno** and **Groq**.

Instead of relying on a single AI agent, the system uses a team of
specialized research agents, where each agent focuses on a different
information source such as **ArXiv, Web Search, Hacker News, Wikipedia,
YouTube, Reddit, X, and news articles**.

An orchestrator agent coordinates the research process, combines the
findings, and generates a structured **Medium-style article**.

The user reviews the generated draft, and only after confirmation is the
final article saved as a Markdown file.

------------------------------------------------------------------------

## ✨ Key Features

-   🤖 Multi-Agent Architecture with specialized research agents
-   🔬 ArXiv Research for academic papers and research topics
-   🌐 Web Research using Web Search & DuckDuckGo
-   📰 News Research and article content extraction
-   🧑‍💻 Hacker News research for technology trends
-   📚 Wikipedia knowledge gathering
-   𝕏 X Research with post metrics
-   ▶️ YouTube transcript, metadata and timestamp analysis
-   👥 Reddit post and subreddit research
-   📧 Gmail Agent for drafting, searching and managing emails
-   ✍️ AI-powered Medium Article Generation
-   👨‍💻 Human-in-the-loop approval before saving articles
-   📄 Markdown-based article storage
-   📥 Automatic storage of downloaded research papers
-   ⚡ AgentOS for serving the agentic application

------------------------------------------------------------------------

## 🧠 Architecture

``` text
                         👤 User
                           │
                           ▼
                    ⚡ AgentOS
                           │
                           ▼
              🧠 Medium Article Team
                           │
                           ▼
                🎯 Orchestrator Agent
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   🔬 ArXiv           🌐 Web Search      🧑‍💻 Hacker News
   Agent              Agent              Agent
        │                  │                  │
        ├──────────┬───────┼──────────┬───────┤
        ▼          ▼       ▼          ▼       ▼
     📰 News    📚 Wiki   𝕏 X      ▶️ YouTube  👥 Reddit
     Agent      Agent     Agent      Agent      Agent
        │
        ▼
   📧 Gmail Agent
        │
        ▼
   📊 Research Findings
        │
        ▼
   ✍️ Medium Article Draft
        │
        ▼
   👤 User Approval
        │
        ▼
   📄 Markdown Article
```

------------------------------------------------------------------------

## 🔄 How It Works

### 1. 🎯 User provides a topic

The user provides a technology, research, or current-topic query.

### 2. 🧠 Orchestrator analyzes the request

The team leader understands the request and decides which specialized
research agents should be used.

### 3. 🔍 Specialized agents perform research

Each agent focuses on its respective information source:

-   🔬 **ArXiv** → Academic research papers
-   🌐 **Web Search** → Recent web information
-   🧑‍💻 **Hacker News** → Technology discussions
-   📰 **News** → Articles and reports
-   📚 **Wikipedia** → Background knowledge
-   𝕏 **X** → Social discussions and post metrics
-   ▶️ **YouTube** → Videos, transcripts and metadata
-   👥 **Reddit** → Community discussions and posts

### 4. 🧩 Research is combined

The orchestrator collects the relevant findings and avoids unnecessary
additional searches once sufficient information has been gathered.

### 5. ✍️ Article generation

The system transforms the collected research into a structured, engaging
Medium-style article.

### 6. 👤 Human approval

The generated article is presented to the user for review.

### 7. 📄 Final output

After confirmation, the article is saved as a `.md` file inside the
`medium_articles/` directory.

------------------------------------------------------------------------

## 🛠️ Tech Stack

  Technology                Purpose
  ------------------------- ---------------------------------
  🐍 Python                 Core application
  🤖 Agno                   Multi-agent framework
  ⚡ AgentOS                Agent application serving
  🧠 Groq                   LLM inference
  🔬 ArXivTools             Research paper discovery
  🌐 WebSearchTools         Web research
  🔎 DuckDuckGoTools        Web search
  🧑‍💻 HackerNewsTools        Hacker News research
  📰 Newspaper4kTools       News article extraction
  📚 WikipediaTools         Wikipedia research
  𝕏 XTools                  X post research and metrics
  ▶️ YouTubeTools           Video and transcript research
  👥 RedditTools            Reddit research
  📧 GmailTools             Email management
  💾 InMemoryDb             Agent/team state
  📁 LocalFileSystemTools   Article and file storage
  🔐 python-dotenv          Environment variable management

------------------------------------------------------------------------

## 🤖 Specialized Agents

### 🔬 ArXiv Research Agent

Searches ArXiv for relevant academic papers and downloads research
material into the `research_papers/` directory.

### 🌐 Web Search Agent

Performs web research using Web Search and DuckDuckGo and returns
relevant information and source URLs.

### 🧑‍💻 Hacker News Research Agent

Gathers information from Hacker News and researches recent
technology-related discussions and articles.

### 📰 News Article Research Agent

Reads online articles and extracts relevant content for research and
summarization.

### 📚 Wikipedia Research Agent

Gathers background information and references from Wikipedia based on
the requested topic.

### 𝕏 X Research Agent

Searches X posts related to the topic and can include available post
metrics in its research.

### ▶️ YouTube Research Agent

Researches YouTube videos, transcripts, metadata and timestamps to
extract useful information.

### 👥 Reddit Research Agent

Searches Reddit posts and communities to gather discussions, opinions
and relevant information.

### 📧 Gmail Agent

Provides Gmail capabilities for searching, reading and drafting emails,
with confirmation required before sending.

------------------------------------------------------------------------

## 📂 Project Structure

``` text
ResearchForge-AI/
│
├── 📁 research_papers/
│   └── Downloaded ArXiv research papers
│
├── 📁 medium_articles/
│   └── Generated Medium articles (.md)
│
├── 📄 app.py
│   └── AgentOS application and multi-agent architecture
│
├── 📄 main.py
│   └── Application entry point / supporting logic
│
├── 📄 requirements.txt
│   └── Python dependencies
│
├── 📄 pyproject.toml
│   └── Project configuration
│
├── 📄 uv.lock
│   └── Locked dependency versions
│
├── 📄 .gitignore
│   └── Protects secrets, virtual environments and temporary files
│
└── 📄 README.md
    └── Project documentation
```

------------------------------------------------------------------------

## 🔐 Security

Sensitive credentials are stored using environment variables instead of
being hard-coded into the application.

Example:

``` env
GROQ_API_KEY=your_api_key_here
```

The `.gitignore` prevents sensitive and local development files such as
the following from being committed:

``` text
.env
token.json
credentials.json
.venv/
__pycache__/
```

------------------------------------------------------------------------

## 🎯 Project Goal

ResearchForge AI demonstrates how **multiple specialized AI agents can
collaborate on a complex research workflow** instead of relying on a
single general-purpose agent.

The project combines:

**Multi-Agent AI + Web Research + Information Extraction + Content
Generation + Human-in-the-Loop**

into a single practical workflow.

------------------------------------------------------------------------

## 🚀 Future Scope

-   🔎 Improved source verification and citation management
-   🧠 Persistent research memory
-   📊 Research quality and source-ranking mechanisms
-   🌐 Web-based frontend dashboard
-   📝 Direct publishing workflow
-   🔄 Automated research pipelines
-   📈 Research analytics and monitoring

------------------------------------------------------------------------

## 👨‍💻 Built With

**Agno • Groq • Python • AgentOS • ArXiv • Web Search • Hacker News •
Wikipedia • X • YouTube • Reddit • Gmail • Newspaper4k**

------------------------------------------------------------------------

> ⚡ **Research smarter. Connect multiple sources. Turn knowledge into
> content.**
