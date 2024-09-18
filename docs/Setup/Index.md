# Environment Setup

## Cloning the Repositories

The weekplanner setup depends on you having the two main Git repositories: [weekplanner](https://github.com/aau-giraf/weekplanner) and [web-api](https://github.com/aau-giraf/web-api) – in order to get these repositories, you need to have installed Git locally. See this [guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) if you don't have it already (if you're on a Mac, Git is installed during the installation guide for GIRAF).

To clone each of these repositories, create a directory, where you want your files to be kept. Be mindful of **not** storing the project in Dropbox, Google Drive or similar, as it might introduce unwanted behaviour, especially with file permissions etc., which isn't fun to debug.

Then open the terminal of your choice (e.g. Terminal, iTerm, PowerShell etc.), and clone the repositories into the directory by running:

`git clone https://github.com/aau-giraf/weekplanner.git`

and

`git clone https://github.com/aau-giraf/web-api.git`

when you have done this, proceed to the setup guide for your operating system, which you can find in the sidebar.

## Pushing to GitHub

To be able to contribute to GIRAF, you need to setup SSH keys for your GitHub account:

## Adding SSH Keys to GitHub (Mac and Windows)

## 1. Generate an SSH key

_Use Terminal on Mac, or Git Bash on Windows_

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

_Note: If you're using Windows and haven't installed Git Bash, download and install it from the official Git website._

## 2. Copy the SSH key

### For Mac:

```
pbcopy < ~/.ssh/id_ed25519.pub
```

### For Windows (Git Bash):

```
cat ~/.ssh/id_ed25519.pub | clip
```

Alternatively, you can manually copy the output of:

```
cat ~/.ssh/id_ed25519.pub
```

## 3. Add the key to GitHub

1. Go to GitHub and log in
2. Click your profile photo in the top right, then click "Settings"
3. In the left sidebar, click "SSH and GPG keys"
4. Click "New SSH key" or "Add SSH key"
5. In the "Title" field, add a descriptive label for the new key
6. Paste your key into the "Key" field
7. Click "Add SSH key"

## 4. Test the connection

### For Mac (Terminal) and Windows (Git Bash):

```
ssh -T git@github.com
```

You should see a message like: "Hi username! You've successfully authenticated, but GitHub does not provide shell access."

## Troubleshooting

- If you're on Windows and Git Bash isn't working, you can use the Command Prompt or PowerShell, but some commands may differ.
- Ensure your SSH agent is running. On Mac or Git Bash, use:
  ```
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_ed25519
  ```
- If you're still having issues, check GitHub's official documentation or support resources.
