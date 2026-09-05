import { ENDPOINT } from "../consts";
import type { Movie } from "../types";

export async function searchMovie(query: string): Promise<Movie[]> {
    const URL = ENDPOINT + `/search/${query}`;
    try {
        const servResponse = await fetch(URL, { method: "POST" });
        if (!servResponse.ok) {
            throw new Error(`Response status ${servResponse.status}`);
        }

        const movies: Movie[] = await servResponse.json();
        return movies;
    } catch (error) {
        console.error("Unexpected error in searchMovie().", error);
        return []
    }
}