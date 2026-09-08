import { useEffect, useState } from "react";
import type { Movie, Rate } from "../types";
import { getSavedRatings } from "../api/localstorage";
import MovieCard from "../components/movieCard";
import { getMoviesByID } from "../api/getMovies";

export default function RatedPage() {
    const [isError, setIsError] = useState<boolean>(false);

    const [savedRatings, setSavedRatings] = useState<Rate[]>([]);
    const [ratedMovies, setRatedMovies] = useState<Movie[]>([])
    useEffect(() => {
        getMoviesByID(
                getSavedRatings().map((rate: Rate) => rate.movieId)
            ).then(res=>setRatedMovies(res))
            .catch(()=>setIsError(true));
        // console.log(savedRatings, ratedMovies);
    }, [])

    return (
        <>
        <p>{JSON.stringify(ratedMovies)}</p>
            {
                ratedMovies.map((value) => {
                    return (<MovieCard movie={value} key={`${value.title}-${value.id}`} />)
                })
            }
        </>
    );
}