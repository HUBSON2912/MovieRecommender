export type Page = "search" | "rated" | "recommendations" | "about";
export type PageContextType = { page: Page, setPage: (p: Page) => void };

export type Genre = { id: number, name: string };
export type Movie = {
    adult: boolean,
    genres: string[],  // just names
    id: number,
    imdb_id:string,
    overview: string,
    popularity: number,
    poster_path: string, // image.tmdb.org api -> developer.themoviedb.org/docs/image-basics
    release_date: Date,
    title: string,
    vote_average: number,
    vote_count: number
};