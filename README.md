# Introduction
This is my summer project. The aim of this project was to learn more about machine learning and recommendation systems. During work I decided to implement is as API and create some frontend.

# This project vs real one
I learned that in real usage the model should be common for all the users. The real model should be retrained after every rate of any user (or periodically: every night, every week). I've built simplified service: users can create model for themself and choose agent that fits them best. Models are not retrained but user can order to train a new one having regard to their ratings.

# What I learned
Working on the project I learn something about:
- Funk SVD
- FastAPI
- Apache virtual hosts and reverse proxy
- TypeScript
- React + MaterialUI
- Unit tests in Python

# About testing
I had some truble with `Movie.transform` method in `back/src/custom_types.py` so I wrote unit tests to check anytime if it works. 

I didn't plan to write unit tests for the rest of code because it is not a big project; tests were very useful, but not necessary. Finally I wrote some unit tests in `pytest` but they aren't a key point I think. I made them for skill rather than for real need.

# Source of data
https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/data

Mosts of data included are not required in this project.

This dataset could be better. Mosts of paths lead to the pictures that don't exist. Some users rated movies with ID that doesn't exist. Also, it's quite old dataset. It contains movies that were released before 2017.

# Theory
- [An Introduction to Matrix factorization and Factorization
Machines in Recommendation System, and Beyond](https://arxiv.org/abs/2203.11026) by Yuefeng Zhang
- [The Evolution of Cybernetics. A Journal](https://sifter.org/~simon/journal/index.html) by Simon Funk. In particular, the note "Netflix Update: Try This at Home" (Monday, December 11, 2006)
