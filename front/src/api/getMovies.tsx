import { ENDPOINT } from "../consts";
import type { Movie } from "../types";

export async function getMovies(offset:number=0) : Promise<Movie[]> {
    const URL=ENDPOINT+`/get/movies/${offset}`;
    try {
        const servResponse=await fetch(URL, {method: "POST"});
        if(!servResponse.ok) {
            throw new Error(`Response status ${servResponse.status}`);
        }
        console.log(servResponse);

        const movies:Movie[]=await servResponse.json();
        console.log(movies);
        return movies;
    }
    catch(error) {
        console.error("Unexpected error in getMovies().", error);
        return []
    }
}