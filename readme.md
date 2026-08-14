# ArchMaster

archmaster is a CERMAT preparation platform that is designed to prepare the student as effectively as posisble making most of his time.

## Vision

The main idea is that expensive platforms where the test sheets mimic CERMAT testing are too expensive and can be replaced by AI workflow and a platforms that comes with it that can track the students progress and things like his desired high-school or target points.

I want this project aspire to be a platform that can be deployed to several thousand of active users and to be a product that is worth purchasing not AI-slop exam preparation that already exists in some form somewhere.

The platform is meant to prepare the student by familiarizing him with CERMAT type question through repeated tesing and reinforcement. It is meant to replace the [Todáš](https://www.todas.cz) - a platform that provides students with practice CERMAT test in pdf form and live streams where the write and correct them.

## Tech Stack

- **Backend**: Python + FastAPI
- **Frontend**: TypeScript + React + Vite

## Important Product Principles

### AI does not design the UI/UX

### Do not let AI-generated UI patterns determine the product's design.

The UI and UX should be deliberately designed and kept consistent. Avoid generic "AI slop" interfaces, unnecessary dashboards, excessive cards, gradients, animations, or arbitrary components simply because they are common in AI-generated websites.

### Do not over-engineer or assume the final product

This project is currently in the idea and experimentation stage.

Do not assume that features, architecture, database structure, AI models, or workflows are already decided.

## Current Focus

The project is currently in an **experimentation and discovery phase**.

The main goal right now is to discover what actually makes students improve their
CERMAT results as effectively as possible between tests. I want to experiment
with different features, learning methods, feedback systems, and approaches to
find what genuinely helps students progress.

Most things built during this phase are expected to be temporary. Features
should be treated as experiments rather than commitments to the final product. and made to be easily tested in development enviroment.

The goal is not to keep adding features and optimizing an increasingly complex
system. Instead, the final product should be the result of **aggressive
simplification**: keep what demonstrably works, remove what does not, and
continuously question whether each part of the product is actually necessary.

> **Build → test → learn → delete → simplify → repeat.**

During this phase, prioritize **learning what the product should be** over
building a polished or permanent architecture.
