import requests

def get_pairs():
    """
    Henter token-par fra DEX Screener API og returnerer en liste med dicts.
    """
    url = "https://api.dexscreener.com/latest/dex/pairs"
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"Fejl ved hentning af data: {e}")
        return []

    pairs = []
    for pair in data.get("pairs", []):
        pairs.append({
            "pair": pair.get("pairAddress"),
            "token0": (pair.get("token0") or {}).get("symbol"),
            "token1": (pair.get("token1") or {}).get("symbol"),
            "liquidity": (pair.get("liquidity") or {}).get("usd", 0)
        })
    return pairs
