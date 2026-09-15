import { useEffect, useState } from "react";
import type { Movie, Rate } from "../types";
import { getSavedRatings } from "../api/localstorage";
import MovieCard from "../components/movieCard";
import { getMoviesByID } from "../api/movies";

export default function RatedPage() {
    const [isError, setIsError] = useState<boolean>(false);
    // todo error handling
    const [savedRatings, setSavedRatings] = useState<number[]>([]);
    const [ratedMovies, setRatedMovies] = useState<Movie[]>([])
    // read ratings
    useEffect(() => {
        setSavedRatings(getSavedRatings().map(x => x.movieId))
    }, []);
    // get movies when ratings are ready
    useEffect(() => {
        if (savedRatings.length == 0)
            return;
        console.log(savedRatings);
        getMoviesByID(savedRatings)
            .then(res => setRatedMovies(res))
            .catch(() => setIsError(true));
    }, [savedRatings]);

    return (
        <>
            {
                ratedMovies.map((value) => {
                    return (<MovieCard movie={value} key={`${value.title}-${value.id}`} />)
                })
            }
        </>
    );
}