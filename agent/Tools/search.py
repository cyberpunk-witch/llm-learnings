#!/usr/bin/env python3
from ddgs import DDGS
from typing import Optional, List, Dict
import json

def search(
    query: str,
    region: Optional[str] = "us-en",
    safesearch: Optional[str] = "moderate", 
    timelimit: Optional[str] = "y",
    num_results: Optional[int] = 5,  # Default to manageable number
    format: Optional[str] = "clean"  # "clean", "json", "raw"
) -> str:
    """
    Searches the internet using DDGS.
    Returns formatted results suitable for LLM processing.
    
    format options:
    - "clean": Title and snippet only, newline separated
    - "json": Structured JSON string
    - "raw": Original DDGS format
    """
    try:
        results = list(DDGS().text(
            query=query, 
            region=region, 
            safesearch=safesearch, 
            timelimit=timelimit, 
            max_results=num_results or 5
        ))
        
        if not results:
            return f"No results found for: {query}"
            
        if format == "clean":
            # LLM-friendly format
            formatted = []
            for i, result in enumerate(results, 1):
                title = result.get('title', 'No title')
                snippet = result.get('body', 'No snippet')
                url = result.get('href', '')
                formatted.append(f"{i}. {title}\n   {snippet}\n   Source: {url}\n")
            return "\n".join(formatted)
            
        elif format == "json":
            # Keep only useful fields
            clean_results = []
            for result in results:
                clean_results.append({
                    'title': result.get('title', ''),
                    'snippet': result.get('body', ''),
                    'url': result.get('href', '')
                })
            return json.dumps(clean_results, indent=2)
            
        else:  # raw
            return str(results)
            
    except Exception as e:
        return f"Search error: {str(e)}"

# Convenience functions for specific use cases
def search_for_evidence(claim: str, num_results: int = 3) -> str:
    """Search specifically for evidence about a claim"""
    query = f'evidence research study "{claim}"'
    return search(query, num_results=num_results, format="clean")

def search_recent(query: str, num_results: int = 5) -> str:
    """Search for recent information"""
    return search(query, timelimit="m", num_results=num_results, format="clean")