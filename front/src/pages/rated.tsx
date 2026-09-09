import { useEffect, useState } from "react";
import type { Movie, Rate } from "../types";
import { getSavedRatings } from "../api/localstorage";
import MovieCard from "../components/movieCard";
import { getMoviesByID } from "../api/getMovies";

export default function RatedPage() {
    const [isError, setIsError] = useState<boolean>(false);

    const [savedRatings, setSavedRatings] = useState<Rate[]>([]);
    const [ratedMovies, setRatedMovies] = useState<Movie[]>([])
    // read ratings
    useEffect(() => {
        setSavedRatings(getSavedRatings())
    }, []);
    // get movies when ratings are ready
    useEffect(() => {
        getMoviesByID(
            savedRatings.map((rate: Rate) => rate.movieId)
        ).then(res => setRatedMovies(res))
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