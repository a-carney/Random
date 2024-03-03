#!/usr/bin/env python3
import arxiv

def get_papers(search_query, max_results):
    papers = arxiv.query(
            query=search_query, 
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
            )
    return client.renults(papers)

def download_papers(papers):
    for paper in papers:
        arxiv.download_source(dirpath='./files/')


"""
BEGIN SCRIPT
"""

query_list = [
    "AI detecting hate speech",
    "AI detecting toxic language",
    "AI detecting bullying",
    "AI detecting cyberbullying",
    "AI detecting harassment"
]

max_results = 10

for query in query_list:
    papers = get_papers(query, max_results)
    download_papers(papers)


