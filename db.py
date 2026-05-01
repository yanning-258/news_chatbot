"""
this script is to set up connection with postgresDB with docker

2 Collections
1. summaries
this stores the daily articles the user read
2. digests
this stores the weekly digest generated from 

# summaries table
{
  "date": "2026-04-30",
  "topic": "NVDA",
  "headline": "Nvidia beats earnings...",
  "url": "https://...",
  "summary": "...",        # what the AI produced
  "created_at": datetime
}

# digests table
{
  "week_start": "2026-04-28",
  "week_end": "2026-05-04",
  "content": "...",        # AI-generated weekly summary
  "created_at": datetime
}
"""

#Connection to MongoDB
#Part 1: Set up client



#Part 2: Helper functions