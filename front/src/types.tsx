export type Page = "search" | "rated" | "recommendations" | "about";
export type PageContextType = { page: Page, setPage: (p: Page) => void };

export type Rate = { movieId: number, rate: number };

/**
 * @param {Rate[]} ratings - array of all ratings 
 * @param {Function} setRatings - override existing rate or add a new one
 * @param {Function} delRatings - delete rate with given movieId
 */
export type RatingsContextType = { 
    ratings: Rate[], 
    setRatings: (r: Rate) => void,
    delRatings: (id:number)=>void
};

export type Movie = {
    adult: boolean,
    genres: string[],  // just names
    id: number,
    imdb_id: string,
    overview: string,
    popularity: number,
    poster_path: string, // image.tmdb.org api -> developer.themoviedb.org/docs/image-basics
    release_date: string,
    title: string,
    vote_average: number,
    vote_count: number
};