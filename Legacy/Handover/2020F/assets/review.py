import requests
from requests.auth import HTTPBasicAuth
import os
import time
import json

# ==== SETUP ====

# Your Github username
USERNAME = ""
# Create a personal access token: https://github.com/settings/tokens and give it repository access
TOKEN = ""

# How many teams should review each pull request
TEAMS_PER_PR = 2

# The list of aau-giraf repositories supported by the script. Just add more if needed.
repositories = (
    "weekplanner", 
    "wiki", 
    "web-api", 
    "api_client",
    "giraf-production-swarm", 
    "web-api-dotnetcore-build"
)

# The webhook for discord/slack. We used this for discord, the script might have to be changed a bit to work with slack.
# Leave this empty to not send discord message
WEBHOOK_URI = ""

# ==== TEAMS ====

TEAM_PREFIX = "sw6"
TEAM_SUFFIX = "f20"

# Mapping from aau group names to discord role ID's.
# We used this to tag the teams in our #review channel on discord
# If using discord, you can get the team id's by enabling developer mode,
#  and then right click on the role and click "Copy ID"
DISCORD_TEAM_IDS = {
    "sw607f20": "677102688478953473",
    "sw608f20": "677102844788080640",
    "sw609f20": "677102922152148992",
    "sw610f20": "677102975910674442",
    "sw611f20": "677103044785078272",
    "sw612f20": "677103114914103296",
    "sw613f20": "677103232031522816",
    "sw614f20": "677103277548109846",
    "sw615f20": "677103313346625540",
    "sw616f20": "677103380115750912",
    "sw617f20": "677103407869198359",
}

# ==== CONSTANTS ====

GITHUB_API_URL = "https://api.github.com"
PR_REVIEWS_TEMPLATE = GITHUB_API_URL + \
    "/repos/aau-giraf/:repo/pulls/:pull_number/reviews"
PR_REVIEW_REQUEST_TEMPLATE = GITHUB_API_URL + \
    "/repos/aau-giraf/:repo/pulls/:pull_number/requested_reviewers"

# The review checklists
CODE_CHECKLIST_URL = "https://raw.githubusercontent.com/aau-giraf/wiki/master/docs/process_manual/review_checklists/review_checklist_code.md"
WIKI_CHECKLIST_URL = "https://raw.githubusercontent.com/aau-giraf/wiki/master/docs/process_manual/review_checklists/review_checklist_wiki.md"


# ==== SCRIPT ====

def main():
    if not USERNAME:
        print("USERNAME is not set, exiting")  
        exit()
    if not TOKEN:
        print("TOKEN is not set, exiting")
        exit()

    while(True is not False):
        repo = chooseRepo()
        pr = specifyPR(repo)
        teams = specifyXteams(TEAMS_PER_PR)
        if confirm(repo, pr, teams) != "y":
            print("Resetting")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        if WEBHOOK_URI:
            sendMessageInDiscordReviewChannel(repo, pr, teams)

        url = createURL(PR_REVIEWS_TEMPLATE, repo, pr)
        request_review_url = createURL(PR_REVIEW_REQUEST_TEMPLATE, repo, pr)
        message = getChecklistText(repo)

        req = requests.post(url=request_review_url, data=json.dumps({"reviewers": [
        ], "team_reviewers": teams}), auth=HTTPBasicAuth(USERNAME, TOKEN))
        print("OK: Reviewers assigned!" if req.status_code == 200 else req.text)

        for team in teams:
            data = {'body': insertTeamToMessage(
                message, team), 'event': 'COMMENT'}

            req = requests.post(url=url, data=json.dumps(
                data), auth=HTTPBasicAuth(USERNAME, TOKEN))
            print("OK" if req.status_code == 200 else req.text)


def chooseRepo():
    print("Choose repository to create checklist comment in: ")
    i = 1
    for repo in repositories:
        print(str(i) + ": " + repo)
        i += 1

    return repositories[int(input()) - 1]


def specifyPR(repo):
    return input("Enter pull request number on " + repo + ": ")


def sendMessageInDiscordReviewChannel(repo, pr, teams):
    req = requests.post(WEBHOOK_URI, data={
                        'content': '<@&{}> og <@&{}>: I er sat på review til <{}>'
                        .format(DISCORD_TEAM_IDS[teams[0]],
                                DISCORD_TEAM_IDS[teams[1]],
                                'https://github.com/aau-giraf/{}/pull/{}'.format(repo, pr))})

    print("OK: Message sent to discord!" if req.status_code == 200 else req.text)


def specifyXteams(x):
    teams = []
    for number in range(1, x+1):
        teams.append(createGroupName(
            int(input("Enter the " + str(number) + ". team to be assigned: "))))
    return teams


def confirm(repo, pr, teams):
    print("Confirm by entering \"y\" that " + repo + "#" + pr + " ", end="")
    for team in teams:
        print(team + " ", end="")
    print("is correct: ")

    return input()


def createGroupName(group_number: int):
    return TEAM_PREFIX + str.format('{:02d}', group_number) + TEAM_SUFFIX


def createURL(template, repo, pull_request):
    url = template.replace(":repo", repo)
    url = url.replace(":pull_number", pull_request)
    return url


def getChecklistText(repo):
    if (repo == "wiki"):
        url = WIKI_CHECKLIST_URL
    else:
        url = CODE_CHECKLIST_URL

    req = requests.get(url)
    text = req.text
    text = text.replace(
        "I marked @user as the reviewer, but you might change it as you like.", "")

    return text


def insertTeamToMessage(message, team):
    return message.replace("@aau-giraf/team", "@aau-giraf/" + team)


def getFullTeamNames(teams):
    fullTeams = teams
    for team in fullTeams:
        team = "aau-giraf/" + team

    return teams


if __name__ == "__main__":
    main()
