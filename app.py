from agno.agent import Agent 
from agno.models.groq import Groq
from agno.team import Team
from agno.os import AgentOS
from agno.tools.arxiv import ArxivTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.websearch import WebSearchTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.wikipedia import WikipediaTools
from agno.tools.x import XTools
from agno.tools.youtube import YouTubeTools
from agno.tools.reddit import RedditTools
from agno.tools.google.gmail import GmailTools 
from agno.db.in_memory import InMemoryDb
from agno.tools.local_file_system import LocalFileSystemTools
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

dir_path=Path("./research_papers/")
dir_path.mkdir(exist_ok=True)

target_dir=Path("./medium_articles/")
target_dir.mkdir(exist_ok=True)

api_key=os.getenv("GROQ_API_KEY","").strip()

orchestrator_model=Groq(id="openai/gpt-oss-120b",api_key=api_key)
model=Groq(id="openai/gpt-oss-20b",api_key=api_key)

db=InMemoryDb()

arxiv_research_agent=Agent(
    id="arxiv-research-agent",
    name="Arxiv Research Agent",
    model=model,
    role="Arxiv Research Assistant",
    instructions=["you are an research assistant that gathers the reseach papers from the Arxiv",
                  "use the available tools to search for research papers ,authors, topics as per user's request",
                  "summarize your findings clearly and consisely"],
    tools=[ArxivTools(download_dir=dir_path)],
    add_datetime_to_context=True
)

web_search_agent = Agent(
    id="web-search-agent",
    name="Web Search Agent",
    model=model,
    role="Web Research Assistant",
    instructions=[
        "You are a web research assistant.",
        "Search the web for the user's requested topic.",
        "For simple questions, perform only one search.",
        "Return the top 3 relevant results.",
        "Do not perform additional searches after getting useful results.",
        "Summarize the results briefly and include source URLs."
    ],
    tools=[
        WebSearchTools(fixed_max_results=3,timelimit="w"),
        DuckDuckGoTools(fixed_max_results=3,timelimit="w")
    ],
    tool_call_limit=1,
    add_datetime_to_context=True
)

hackernews_research_agent=Agent(
    id="hackernews-research-agent",
    name="Hackernews Research Agent",
    model=model,
    role="Hackernews research assistant",
    instructions=["you are the expert research assitant that can access hackernews",
                  "get relevant information for the recent topics and get information about the article for the topic user requested for",
                  "summarize your findings in proper format"],
    add_datetime_to_context=True,
    tools=[HackerNewsTools()]
)

news_article_research_agent=Agent(
    id="news-article-research-agent",
    name="News Article Research Agent",
    model=model,
    role="News Article Research Assistant",
    instructions=["you are the research assistant that can read the content of articles",
                  "whenever an url is provided you can read the content of article and can also get its data",
                  "using the available tools search for articles and summarize them and gather relevant information"],
    add_datetime_to_context=True,
    tools=[Newspaper4kTools(include_summary=True)]
)

wikipedia_research_agent=Agent(
    id="wikipedia-research-agent",
    name="Wikipedia Research Agent",
    model=model,
    role="Wikipedia Research Assistant",
    instructions=["you are an expert research assistant that gather information from Wikipedia based on the topic user requested for",
                  "u have the capability to search for articles and gather its content ",
                  "sumarize your findings and mention the appropriate resource and reference in your output"],
    add_datetime_to_context=True,
    tools=[WikipediaTools()]
)

x_research_agent=Agent(
    id="x-research-agent",
    name="X Research Agent",
    model=model,
    role="X(formally twitter) Research Assistant",
    instructions=["you are the research assistant that gathers the information from X (formally twitter)",
                  "You have the ability to search for the post and gathers the relevant information",
                  "Do include the metrics information for the post ",
                  "summarize your research in clear and consised manner"],
    add_datetime_to_context=True,
    tools=[XTools(include_post_metrics=True,wait_on_rate_limit=True,include_tools=["search_posts"])]
)

youtube_research_agent=Agent(
    id="youtube-research-agent",
    name="Youtube Research Agent",
    model=model,
    role="Youtube Research assistant",
    instructions=["you are an research assiatant that gathers information from youtube",
                  "you have the capability to read youtube video , transcript and summarize them ",
                  "you can also read metadata related to youtube videos",
                  "you can also fetch timestamps of a particular video",
                  "summarize the transcript in clear and consise manner"],
    add_datetime_to_context=True,
    tools=[YouTubeTools()]
)

reddit_reseach_agent=Agent(
    id="reddit-research-agent",
    name="Reddit Research Agent",
    model=model,
    role="Reddit Research Assistant",
    instructions=["you are a research assistant that gathers information from Reddit",
                  "you have access to read, posts and also gathers the data for subreddits",
                  "You can also gather the latest posts from reddits"],
    add_datetime_to_context=True,
    tools=[RedditTools([
    "get_subreddit_info",
    "get_subreddit_posts",
    "search_subreddits",
    "get_post_details",
    "search_posts"
])]
)

gmail_agent=Agent(
    id="gmail-agent",
    name="Gmail Agent",
    model=model,
    role="Manages mails through gmail",
    instructions=["you are the helpful agents that can draft messages using gmail",
                  "you have the capability to draft mails and read mails and send mails whenever requested by the user",
                  "you have the capability to search for mails and read the content of mails",
                  "always make sure to confirm the draft before sending it to the mail id ",
                  "make sure to write the mails with proper format including a relevant subject line"],
    add_datetime_to_context=True,
    tools=[GmailTools(oauth_port=3000)]
)

medium_article_team=Team(
    id="medium-article-creation",
    name="Medium Article Creation Team",
    role="Team Leader which manages research and content creation",
    db=db,
    members=[arxiv_research_agent,
             web_search_agent,
             hackernews_research_agent,
             news_article_research_agent,
             wikipedia_research_agent,
             x_research_agent,
             youtube_research_agent,
             reddit_reseach_agent,
             gmail_agent],
    model=orchestrator_model,
    instructions=["you are a team leader managing multiple sub agents in your team",
                  "you have access to agents which can do research based on the topic on various sources such as arxiv, hackernews,newspaper article ,wikipedia, youtube, X(formally twitter),reddit and websearch using web search and duckduckgo search",
                  "you have the capability to read and write emails",
                  "your task is to understand topic given by user and fetch relevant research information using your team members",
                  "once you have enough research materials your primary task is to create medium(platform) styled articles",
                  "for checking how articles are written on medium you can use the article research agents",
                  "once you have created the medium article, show user the final draft",
                  "only when the user confirms the draft , save it to the file system in a markdown format as .md file using the file name suggested by user ",
                  "if a user does not give a filename , then use the self created name based on the topic on which article was created",
                  "Do not keep searching after sufficient information has been collected"
                  ],
    add_datetime_to_context=True,
    add_history_to_context=True,
    num_history_runs=3,
    tools=[LocalFileSystemTools(target_directory=target_dir,default_extension="md")],
    stream=True,
    markdown=True
)

agent_os=AgentOS(
    id="medium-article-os",
    name="Medium Article Generator OS",
    description="An agent that conduct research of latest tech topis across multiple platforms and generates medium article based on its finding",
    teams=[medium_article_team]
)

app=agent_os.get_app()

if __name__=="__main__":
    agent_os.serve(
        app="app:app",
        reload=True
    )
