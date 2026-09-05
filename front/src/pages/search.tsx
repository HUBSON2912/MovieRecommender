import { Button, Typography } from "@mui/material";
import SearchBar from "../components/searchBar";
import MovieCard from "../components/movieCard";
import { useEffect, useState } from "react";
import type { Movie } from "../types";
import { getMovies } from "../api/getMovies";
import { searchMovie } from "../api/searchMovie";
import SomethingWentWrong from "../components/sthWentWrong";

export default function SearchPage() {
    // errors
    const [isError, setIsError] = useState<boolean>(false);
    const handleRefresh = () => {
        setSearchTextInput("");
        setFoundMovies(null);
        setRating(null);
        setLoadedMovies([]);
        setIsError(false);

        handleLoadMoreMovies("set");
    }

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

    // rating logic
    const [rating, setRating] = useState<number | null>(null);
    const handleRate = (event: React.SyntheticEvent, value: number | null) => {
        console.log(value);
        setRating(value);
        // todo change value type to {id: int, value:int|null}
        // todo save in file or localstorage
    }

    // simple loading movies logic
    const [loadedMovies, setLoadedMovies] = useState<Movie[]>([]);
    const handleLoadMoreMovies = (mode: "set" | "append") => {
        getMovies(mode == "set" ? 0 : loadedMovies.length)
            .then(res => {
                if (mode == "set")
                    setLoadedMovies(res)
                else
                    setLoadedMovies(prev => [...prev, ...res])
            })
            .catch(() => {
                setIsError(true);
            });
    }
    // load movies on load
    useEffect(() => handleLoadMoreMovies("set"), []);

    if (isError) {
        return (<SomethingWentWrong onRefresh={handleRefresh} />);
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
                    foundMovies == null
                        ? loadedMovies.map((value) => {
                            return (<MovieCard movie={value} onRate={handleRate} key={`${value.title}-${value.id}`} />)
                        })
                        : foundMovies.map((value) => {
                            return (<MovieCard movie={value} onRate={handleRate} key={`${value.title}-${value.id}`} />)
                        })
                }
                {
                    foundMovies != null && foundMovies.length == 0 &&
                    <Typography component="p" sx={{ margin: 1 }}>Cannot find anything. Search for something else.</Typography>
                }
                {
                    foundMovies == null &&
                    <Button variant="outlined" onClick={() => handleLoadMoreMovies("append")}>load more</Button>
                }
            </>
        );
    }
}