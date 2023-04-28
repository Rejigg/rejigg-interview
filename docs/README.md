# Rejigg Interview

## Summary

A single-user demo of Rejigg's Leads feature. It serves Leads at `http://localhost:3000/`.

Users use this page to search through Leads and select their favorites.

## Instructions

Feel free to use any technologies -- even ChatGPT -- or documentation you'd like.

### 1. Search Functionality

Add a search feature which allows the User to filter Leads by a Business's name, Business's description, Owner's Name, and Owner's "about me" fields.

### 2. UI Improvements

Without removing any fields, clean up the UI. Focus on improving the layout of the cards the button which shows only the User's favorites.

Extra credit: Write a few bullet points with ideas for additional UI improvements.

### 3. Improve the performance

Improve the responsiveness of the app, again without removing displayed fields (feel free to make breaking changes to the API though).

Additionally, write a couple of sentences about:

- (a) how you diagnosed performance issues,
- (b) any issues you found but were unable to fix, and
- (c) ideas for further optimizing improving performance

### 4. Submit your response

When you're finished, zip up this directory and email it back to us along with:

- a short description of the changes you made (as if you were about to submit it all as a pull request)
- answers to questions 2 and 3.

## Getting Started

### 1. Install and start [Docker](https://www.docker.com/get-started/).

### 2. Get the code:

```
git clone https://github.com/Rejigg/rejigg-interview.git
cd rejigg-interview
```

### 3. Start the app:

```
make
open http://localhost:3000/
```

> If you don't want to use Docker, you can follow along with the commands in the [Makefile](/Makefile) instead.

## What We Look For

We're most interested in how you think and communicate, and we put a lot of weight on the written portions of the interview. If you aren't a subject matter expert, don't worry, comments or psuedo code are almost as good as the real thing.

## Helpful Resources

- The [Makefile](/Makefile) has helpers for installing packages
- [DRF](https://www.django-rest-framework.org/)
- [Django Filters](https://django-filter.readthedocs.io/en/stable/)
- [MUI Components](https://mui.com/components/)
