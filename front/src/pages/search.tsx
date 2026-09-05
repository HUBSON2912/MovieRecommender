import { Button } from "@mui/material";
import SearchBar from "../components/searchBar";
import MovieCard from "../components/movieCard";
import { useEffect, useState } from "react";
import type { Movie } from "../types";
import { getMovies } from "../api/getMovies";

export default function SearchPage() {
    const [searchTextInput, setSearchTextInput] = useState<string>("");
    const handleWriting = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSearchTextInput(event.currentTarget.value);
    }
    // handle searching
    useEffect(() => {
        // < 2 to catch movies like IT or E.T.
        if (searchTextInput.length < 2)
            return;

    }, [searchTextInput]);




    const [rating, setRating] = useState<number | null>(null);
    const handleRate = (event: React.SyntheticEvent, value: number | null) => {
        console.log(value);
        setRating(value);
        // todo change value type to {id: int, value:int|null}
        // todo save in file or localstorage
    }



    const [loadedMovies, setLoadedMovies] = useState<Movie[]>([]);
    const handleLoadMoreMovies = () => {
        getMovies(loadedMovies.length)
            .then(res => setLoadedMovies(prev => [...prev, ...res]))
            .catch(err=>console.error(err));
    }
    // load movies on load
    useEffect(handleLoadMoreMovies, []);

    return (
        <>
            <SearchBar value={searchTextInput} onChange={handleWriting} />
            {
                loadedMovies.map((value) => {
                    return (<MovieCard movie={value} onRate={handleRate} key={value.title} />)
                })
            }
            <Button variant="outlined" onClick={handleLoadMoreMovies}>load more</Button>
        </>
    );
}