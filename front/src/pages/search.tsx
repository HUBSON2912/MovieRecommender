import { Button, CircularProgress, Typography } from "@mui/material";
import SearchBar from "../components/searchBar";
import { useEffect, useState } from "react";
import type { Movie } from "../types";
import { getBatchOfMovies, searchMovie } from "../api/movies";
import SomethingWentWrong from "../components/sthWentWrong";
import MovieList from "../components/movieList";
import LoadingCircle from "../components/loadingCircle";

export default function SearchPage() {
    // errors
    const [isError, setIsError] = useState<boolean>(false);

    // searching logic
    const [searchTextInput, setSearchTextInput] = useState<string>("");
    const [foundMovies, setFoundMovies] = useState<Movie[] | null>(null);
    const handleWriting = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSearchTextInput(event.target.value);
    }
    const handleSearching = () => {
        searchMovie(searchTextInput)
            .then(res => setFoundMovies(res))
            .catch(() => {
                setIsError(true);
            });
    }
    const handleClearingSearchBar = () => {
        setSearchTextInput("");
        setFoundMovies(null);
    }

    // loading movies logic
    const [loadedMovies, setLoadedMovies] = useState<Movie[]>([]);
    const handleLoadMoreMovies = (mode: "set" | "append") => {
        getBatchOfMovies(mode == "set" ? 0 : loadedMovies.length)
            .then(res => {
                if (mode == "set")
                    setLoadedMovies(res)
                else
                    setLoadedMovies(prev => [...prev, ...res])
            })
            .catch(() => {
                setIsError(true);
            })
            .finally(() => {
                // disable loading animations/elements
                setLoadingLoadMoreButton(false);
            });
    }

    // load movies on load
    useEffect(() => handleLoadMoreMovies("set"), []);

    // loading screen
    const [loadingLoadMoreButton, setLoadingLoadMoreButton] = useState<boolean>(false);

    if (isError) {
        return (<SomethingWentWrong />);
    }
    else {
        return (
            <>
                <SearchBar
                    value={searchTextInput}
                    onChange={handleWriting}
                    onSearch={handleSearching}
                    onClear={handleClearingSearchBar}
                />
                {
                    // do not search and not loaded movies yet
                    foundMovies == null && loadedMovies.length == 0 &&
                    <LoadingCircle />
                }

                <MovieList movies={foundMovies == null ? loadedMovies : foundMovies} />
                {
                    foundMovies != null && foundMovies.length == 0 &&
                    <Typography component="p" sx={{ margin: 1 }}>Cannot find anything. Search for something else.</Typography>
                }
                {
                    // if I am not searching and after movies loaded at the begining
                    foundMovies == null && loadedMovies.length != 0 &&
                    <Button
                        variant="outlined"
                        loading={loadingLoadMoreButton}
                        onClick={() => {
                            setLoadingLoadMoreButton(true);
                            handleLoadMoreMovies("append");
                        }}
                    >load more</Button>
                }
            </>
        );
    }
}