import os
import google.generativeai as genai
from tavily import TavilyClient
import pandas as pd

class OBBBALeadBot:
    def __init__(self, gemini_key, tavily_key):
        genai.configure(api_key=gemini_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.tavily = TavilyClient(api_key=tavily_key)

    def find_eligible_startups(self):
        """OBBBA 세액공제 자격이 있는 미국 소프트웨어 스타트업을 검색합니다."""
        query = "US software startups founded 2022-2024 with R&D focus and revenue under $31M"
        results = self.tavily.search(query=query, search_depth="advanced")
        
        leads = []
        for res in results['results']:
            # Gemini를 통한 적격성 판단
            prompt = f"Analyze if this company is likely to have R&D tax credit eligibility based on OBBBA: {res['content']}"
            response = self.model.generate_content(prompt)
            leads.append({"company": res['title'], "analysis": response.text, "url": res['url']})
        
        return pd.DataFrame(leads)

if __name__ == "__main__":
    bot = OBBBALeadBot(os.getenv("GEMINI_KEY"), os.getenv("TAVILY_KEY"))
    df = bot.find_eligible_startups()
    df.to_csv("leads_database.csv", index=False)
