import { Box } from "@mui/material";
import SearchBar from "../components/searchBar";
import MovieCard from "../components/movieCard";
import { useEffect, useState } from "react";
import type { Movie } from "../types";

export default function SearchPage() {
    const [searchTextInput, setSearchTextInput] = useState<string>("");
    const handleWriting = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSearchTextInput(event.currentTarget.value);
    }

    useEffect(() => {
        // < 2 to catch movies like IT or E.T.
        if (searchTextInput.length < 2)
            return;

        // TODO send AJAX request to the api for movies

    }, [searchTextInput]);

    const movie: Movie = {
        adult: false,
        genres: [{ 'id': 16, 'name': 'Animation' }, { 'id': 35, 'name': 'Comedy' }, { 'id': 10751, 'name': 'Family' }],
        id: 862,
        imdb_id: "tt0114709",
        popularity: 21.946943,
        release_date: new Date(1995, 9, 30),
        title: "Toy Story",
        vote_average: 7.7,
        vote_count: 5415,
        overview: "Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",
        poster_path: "/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg"
    }


    return (
        <>
            <SearchBar value={searchTextInput} onChange={handleWriting} />
            <MovieCard movie={movie} />
        </>
    );
}