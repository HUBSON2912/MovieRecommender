import type { Movie } from "../types"
import MovieCard from "./movieCard"

export default function MovieList({ movies }: { movies: Movie[] }) {
    return (
        movies.map((value, index) => {
            return (<MovieCard movie={value} key={`${value.title}-${value.id}-${index}`} />)
        })
    )
}