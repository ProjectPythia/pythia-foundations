```{image} ../../images/GitHub-logo.png
:alt: GitHub Logo
:width: 400px
```

# Configuring Your GitHub Account

## Overview:

1. Configure your GitHub account for secure logins via ssh and/or https
1. Set up notifications on repositories you own or follow

## Prerequisites

| Concepts                                                   | Importance  | Notes                        |
| ---------------------------------------------------------- | ----------- | ---------------------------- |
| [What is GitHub?](what-is-github)                          | Necessary   | GitHub user account required |
| [GitHub Repositories](github-repos)                        | Necessary   |                              |
| [Issues and Discussions](github-issues)                    | Recommended |                              |
| [Cloning and Forking a Repository](github-cloning-forking) | Recommended |                              |

- **Time to learn**: 35 minutes

---

## GitHub secure key generation

When you signed up for your free account on [GitHub](https://github.com), you established a _user ID_ and its corresponding _password_. Many of the repositories that GitHub serves are readable from anywhere, not even requiring a GitHub account.

However, especially when you use the git command-line interface to access a GitHub-hosted repo, there are cases when you need to provide an additional set of login credentials. Some of these cases are:

1. When you want to clone a _private_, as opposed to _public_ GitHub repository (**read-access**)
2. When you wish to _push_ to a repo (**write-access**)

For these use-cases, you won't be able to simply type your GitHub user ID and password from the command line. Instead, you need to set up _access tokens_ that live in two places: in your GitHub account, and in your local computer's file system.

GitHub supports two means of key-based access: via _https_, and via _ssh_.

For example, one can clone [Project Pythia's Sandbox repository](https://github.com/ProjectPythia/github-sandbox) using a URL for the https protocol:

```{image} ../../images/GitHub_Setup_Advanced_https_URL.png
:alt: GitHub Clone https
:width: 600px
```

---

The URL in this case is **https://github.com/ProjectPythia/github-sandbox.git**

Similarly, if you click on the **SSH** tab:

```{image} ../../images/GitHub_Setup_Advanced_ssh_URL.png
:alt: GitHub Clone ssh
:width: 600px
```

---

Here, the URL is **git@github.com:ProjectPythia/github-sandbox.git**

## Generate a secure personal access token for https

First, you will create a secure token in your GitHub account settings, and then use the token on your local computer.

Follow the steps with helpful screenshots at [GitHub's PAT Creation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) page.

```{admonition} Tip:
:class: tip
If using the *https* protocol to *push* to a remote repo, you must have generated and downloaded a personal access token. You *may* also need it when cloning, *if* the remote repo is *not* open to all.
```

## Generate an SSH public/private keypair

First, on your local computer, you will create an SSH _public/private keypair_, and then upload the _public key_ to your GitHub account.

Follow the steps with helpful screenshots at [GitHub's Connecting to GitHub with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) page.

```{admonition} Tip:
:class: tip
If using the *ssh* protocol to clone *or* push, you *must* have generated and created an ssh key-pair.
```

---

```{admonition} HTTPS vs SSH: Either is fine!
:class: note
Either **https** or **ssh** works fine. Choose whatever you prefer. See [this overview](https://www.toolsqa.com/git/ssh-protocol/) of the pros and cons of each protocol.
```

---

## GitHub notifications

In keeping with the social network aspect of GitHub, you can _follow_ particular repositories that are of interest to you. Additionally, once you begin contributing to a repository, you may wish to be notified when Pull Requests are made, Issues are posted, your code review is requested, and so on. While it's easy to have GitHub email you at the address you used when you registered for your GitHub account, you may wish to avoid email clutter.

### Email notifications

Let's say you wish to monitor (or _watch_) the Project Pythia GitHub Sandbox repository and receive emails about it.

Click on the **Watch** link near the top of the page:

```{image} ../../images/GitHub_Setup_Advanced_Watch.png
:alt: GitHub Watch
:width: 600px
```

---

You can then select what type of notifications you wish to receive. For example, you may want to receive _all notifications_ related to that repo:

```{image} ../../images/GitHub_Setup_Advanced_Watch_All_Activity.png
:alt: GitHub Watch All Activity
:width: 600px
```

---

You will then receive email at the address you used when you signed up for GitHub whenever activity occurs on that repo.

```{image} ../../images/GitHub_Setup_Advanced_Unwatch.png
:alt: GitHub Unwatch
:width: 600px
```

---

You can stop watching that repo by just clicking on the now-labeled _Unwatch_ link again, and choosing _Participating and @mentions_ to toggle it back to _Unwatch_.

## Stop spamming me, GitHub!

It's easy to become overwhelmed with email from one or more repos that you are following and/or participating in! In this case, you may wish to disable email notifications.
In order to set your notification settings, go to **https://github.com/settings/notifications**. You can, for example, uncheck the **Email** boxes to cease receiving notifications that way:

```{image} ../../images/GitHub_Setup_Advanced_Notification_Settings.png
:alt: GitHub Notification Settings
:width: 600px
```

---

If you turn email notifications off, get in the habit of clicking on the _Notifications_ icon when logged into GitHub:

```{image} ../../images/GitHub_Setup_Advanced_Notifications.png
:alt: GitHub Notifications
:width: 600px
```

---

You can click on the _Notifications_ icon and scroll through all notifications from repos that you opted into receiving notifications from:

```{image} ../../images/GitHub_Setup_Advanced_Notifications_Browser.png
:alt: GitHub Notification Browser
:width: 600px
```

---

Use the _Filter notifications_ control to display only those that meet certain criteria. For example, say you only wanted to view topics related to the _MetPy_ repo:

```{image} ../../images/GitHub_Setup_Advanced_Notification_Filter.png
:alt: GitHub Notification Filter
:width: 600px
```

---

```{admonition} Tip:
:class: tip
In the list of notifications, you can unsubscribe as shown below.
```

```{image} ../../images/GitHub_Setup_Advanced_Notifications_Unsubscribe.png
:alt: GitHub Notification Unsubscribe
:width: 600px
```

---

## Summary

- GitHub uses **secure tokens** to enable _write_ (and sometimes _read_) _access_ to GitHub repositories.
- You can opt-in to notifications on a repo. The default, which can be easily changed, is to receive email.

### What's Next?

In the next section, we will learn the basics of version control using command-line `git`.

## References

1. [GitHub Personal Access Token (https)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
1. [GitHub Public/Private Keypair (ssh)](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)
1. [Remotes in GitHub (Carpentries Tutorial)](https://swcarpentry.github.io/git-novice/07-github.html)
