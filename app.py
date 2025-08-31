# utils/get_parts.py
import requests

DEX_URL = "https://api.dexscreener.com/latest/dex/pairs"

def get_pairs():
    resp = requests.get(
        DEX_URL,
        headers={"Accept": "application/json", "User-Agent": "early-token-dashboard/1.0"},
        timeout=15,
    )
    resp.raise_for_status()

    try:
        data = resp.json()
    except ValueError:
        # Serveren returnerede ikke JSON (fx HTML-fejlside/rate limit)
        raise RuntimeError("API returnerede ikke gyldig JSON. Prøv igen om lidt.")

    pairs = []
    for pair in data.get("pairs", []):
        pairs.append({
            "pair": pair.get("pairAddress"),
            "token0": (pair.get("token0") or {}).get("symbol"),
            "token1": (pair.get("token1") or {}).get("symbol"),
            "liquidity": (pair.get("liquidity") or {}).get("usd", 0),
        })
    return pairs
