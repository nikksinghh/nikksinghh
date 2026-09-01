import json
import urllib.request
from pathlib import Path

USERNAME = "nikksinghh"
OUTPUT = Path("assets/github-stats.svg")


def github_api(url):
    request = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json"}
    )

    with urllib.request.urlopen(request) as response:
        return json.load(response)


user = github_api(f"https://api.github.com/users/{USERNAME}")
repos = github_api(
    f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
)

public_repos = user["public_repos"]
followers = user["followers"]

stars = sum(repo["stargazers_count"] for repo in repos)
forks = sum(repo["forks_count"] for repo in repos)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
width="700" height="220" viewBox="0 0 700 220">

<rect width="700" height="220" rx="15"
fill="#0d1117"/>

<text x="350" y="45"
text-anchor="middle"
font-family="Arial"
font-size="26"
font-weight="bold"
fill="#ffffff">
GitHub Stats
</text>

<text x="120" y="105"
text-anchor="middle"
font-family="Arial"
font-size="30"
font-weight="bold"
fill="#58a6ff">
{public_repos}
</text>

<text x="120" y="135"
text-anchor="middle"
font-family="Arial"
font-size="15"
fill="#8b949e">
Repositories
</text>

<text x="290" y="105"
text-anchor="middle"
font-family="Arial"
font-size="30"
font-weight="bold"
fill="#58a6ff">
{followers}
</text>

<text x="290" y="135"
text-anchor="middle"
font-family="Arial"
font-size="15"
fill="#8b949e">
Followers
</text>

<text x="460" y="105"
text-anchor="middle"
font-family="Arial"
font-size="30"
font-weight="bold"
fill="#58a6ff">
{stars}
</text>

<text x="460" y="135"
text-anchor="middle"
font-family="Arial"
font-size="15"
fill="#8b949e">
Stars
</text>

<text x="610" y="105"
text-anchor="middle"
font-family="Arial"
font-size="30"
font-weight="bold"
fill="#58a6ff">
{forks}
</text>

<text x="610" y="135"
text-anchor="middle"
font-family="Arial"
font-size="15"
fill="#8b949e">
Forks
</text>

</svg>
"""

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(svg, encoding="utf-8")

print("GitHub stats generated successfully.")
