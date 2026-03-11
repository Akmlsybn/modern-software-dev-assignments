import os
from dotenv import load_dotenv # Tambahkan ini
from mcp.server.fastmcp import FastMCP
import httpx
import json

# Load environment variables dari file .env
load_dotenv()

# Inisialisasi Server
mcp = FastMCP("WibuMCPServer")

BASE_URL = "https://api.myanimelist.net/v2"

CLIENT_ID = os.getenv("MAL_CLIENT_ID") 
HEADERS = {"X-MAL-CLIENT-ID": CLIENT_ID}

@mcp.tool()
async def search_anime(title: str) -> str:
    """Cari anime berdasarkan judul dan kembalikan 5 hasil teratas beserta sinopsisnya."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            url = f"{BASE_URL}/anime?q={title}&limit=5&fields=id,title,synopsis,mean"
            response = await client.get(url, headers=HEADERS)
            
            if response.status_code in [401, 403]:
                return "Error: Client ID MyAnimeList tidak valid atau akses ditolak."
            
            response.raise_for_status()
            data = response.json().get("data", [])
            
            if not data:
                return f"Anime dengan judul '{title}' tidak ditemukan."
                
            results = []
            for item in data:
                node = item["node"]
                results.append({
                    "Judul": node.get("title", "N/A"),
                    "Skor MAL": node.get("mean", "N/A"),
                    "Sinopsis": node.get("synopsis", "Tidak ada sinopsis.")[:250] + "..."
                })
            return json.dumps(results, indent=2)
            
        except httpx.TimeoutException:
            return "Error: Request ke MyAnimeList timeout (lebih dari 10 detik)."
        except Exception as e:
            return f"Error jaringan: {str(e)}"

@mcp.tool()
async def get_top_anime() -> str:
    """Dapatkan daftar 5 anime dengan rating tertinggi di MyAnimeList."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            url = f"{BASE_URL}/anime/ranking?ranking_type=all&limit=5&fields=id,title,mean"
            response = await client.get(url, headers=HEADERS)
            response.raise_for_status()
            
            data = response.json().get("data", [])
            results = [f"{i+1}. {item['node']['title']} (Skor: {item['node'].get('mean', 'N/A')})" for i, item in enumerate(data)]
            
            return "🏆 Top 5 Anime di MAL:\n" + "\n".join(results)
            
        except httpx.TimeoutException:
            return "Error: Request ke MyAnimeList timeout."
        except Exception as e:
            return f"Error jaringan: {str(e)}"

if __name__ == "__main__":
    mcp.run()