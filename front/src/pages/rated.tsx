import { useContext, useEffect, useState } from "react";
import type { Movie, Rate } from "../types";
import { getSavedRatings } from "../api/localstorage";
import { getMoviesByID } from "../api/movies";
import MovieList from "../components/movieList";
import SomethingWentWrong from "../components/sthWentWrong";
import { Typography } from "@mui/material";
import LoadingCircle from "../components/loadingCircle";
import { CurrentPageContext } from "../App";
import type { SxProps } from "@mui/material/styles";
import type { Theme } from "@mui/material/styles";

export default function RatedPage() {
    const [isError, setIsError] = useState<boolean>(false);
    
    const [savedRatings, setSavedRatings] = useState<number[] | null>(null);
    const [ratedMovies, setRatedMovies] = useState<Movie[] | null>(null)

    // read ratings
    useEffect(() => {
        setSavedRatings(getSavedRatings().map(x => x.movieId))
    }, []);

    // get movies when ratings are ready
    useEffect(() => {
        if (savedRatings == null)
            return;

        if (savedRatings.length == 0) {
            setRatedMovies([]);
            return;
        }

        getMoviesByID(savedRatings)
            .then(res => setRatedMovies(res))
            .catch(() => setIsError(true));
    }, [savedRatings]);

    // go to search page handling
    const pageContext = useContext(CurrentPageContext);

    // error occured
    if (isError) {
        return <SomethingWentWrong />;
    }

    // i didn't rate any movie
    if (ratedMovies != null && ratedMovies.length == 0) {
        return (
            <>
                <Typography component="p">You must rate some movies first.</Typography>
                <Typography component="p">Go to <Typography component="span" onClick={() => pageContext.setPage("search")} sx={styles.link}>search</Typography> page.</Typography>
            </>
        );
    }

    // movies are not loaded yet
    if (ratedMovies == null) {
        return <LoadingCircle />;
    }

    return <MovieList movies={ratedMovies} />;
}

const styles: Record<string, SxProps<Theme>> = {
    link: {
        color: "info.main"
    }
}