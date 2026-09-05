import { Button } from "@mui/material";
import SearchBar from "../components/searchBar";
import MovieCard from "../components/movieCard";
import { useEffect, useState } from "react";
import type { Movie } from "../types";
import { getMovies } from "../api/getMovies";
import { searchMovie } from "../api/searchMovie";

export default function SearchPage() {
    const [searchTextInput, setSearchTextInput] = useState<string>("");
    const [foundMovies, setFoundMovies] = useState<Movie[] | null>(null);
    const handleWriting = (event: React.ChangeEvent<HTMLInputElement>) => {
        const newVal = event.currentTarget.value;
        setSearchTextInput(newVal);

        if (newVal.length == 0) {
            setFoundMovies(null); // clear searching results
        }
        console.log("found:", foundMovies)
        console.log("loaded:", loadedMovies)
    }
    const handleSearching = () => {
        searchMovie(searchTextInput).then(res => setLoadedMovies(res)).catch(err => console.error(err));
    }


    const [rating, setRating] = useState<number | null>(null);
    const handleRate = (event: React.SyntheticEvent, value: number | null) => {
        console.log(value);
        setRating(value);
        // todo change value type to {id: int, value:int|null}
        // todo save in file or localstorage
    }



    const [loadedMovies, setLoadedMovies] = useState<Movie[]>([]);
    const handleLoadMoreMovies = (mode: "set" | "append") => {
        getMovies(loadedMovies.length)
            .then(res => {
                if (mode == "set")
                    setLoadedMovies(res)
                else
                    setLoadedMovies(prev => [...prev, ...res])
            })
            .catch(err => console.error(err));
    }
    // load movies on load
    useEffect(() => handleLoadMoreMovies("set"), []);

    return (
        <>
            <SearchBar value={searchTextInput} onChange={handleWriting} onSearch={handleSearching} />
            {
                foundMovies==null
                ? loadedMovies.map((value) => {
                    return (<MovieCard movie={value} onRate={handleRate} key={`${value.title}-${value.id}`} />)
                })
                : foundMovies.map((value) => {
                    return (<MovieCard movie={value} onRate={handleRate} key={`${value.title}-${value.id}`} />)
                })
            }
            <Button variant="outlined" onClick={() => handleLoadMoreMovies("append")}>load more</Button>
        </>
    );
}