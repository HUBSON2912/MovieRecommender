import { ENDPOINT } from "../consts";
import type { Movie } from "../types";

export async function getBatchOfMovies(offset: number = 0): Promise<Movie[]> {
    const URL = ENDPOINT + `/movies/${offset}`;
    try {
        const servResponse = await fetch(URL, { method: "POST" });
        if (!servResponse.ok) {
            throw new Error(`Response status ${servResponse.status}`);
        }

        const movies: Movie[] = await servResponse.json();
        return movies;
    }
    catch (error) {
        console.error("Unexpected error in getBatchOfMovies().", error);
        throw error;
    }
}

export async function getMoviesByID(ids: number[]): Promise<Movie[]> {
    const URL = ENDPOINT + `/movies/ids`;
    try {
        const servResponse = await fetch(URL, {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify(ids)
        });
        if (!servResponse.ok) {
            throw new Error(`Response status ${servResponse.status}`);
        }

        const movies: Movie[] = await servResponse.json();
        return movies;
    }
    catch (error) {
        console.error("Unexpected error in getMoviesByID().", error);
        throw error;
    }
}