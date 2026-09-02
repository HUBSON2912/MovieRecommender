import type { Movie } from "../types";
import "../css/movieCard.css";

export default function MovieCard({ movie }: { movie: Movie }) {
    let voteRank: string;
    if (movie.vote_average >= 7.5)
        voteRank = "rank1";
    else if (movie.vote_average >= 5)
        voteRank = "rank2";
    else if (movie.vote_average >= 2.5)
        voteRank = "rank3";
    else
        voteRank = "rank4";

    return (
        <div className="cardContainer">
                <img className="movieImage" height="400" src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`} alt="Cannot load the image" />
            <div className="movieData">
                <div className="movieDataHeader">
                    <h2>{movie.title}</h2>
                    ({movie.release_date.getFullYear()})
                </div>
                <p className="movieDataTags">
                    {
                        movie.adult ? "ADULT, " : ""
                    }
                    {
                        movie.genres.map((gen, index) => gen.name + (index + 1 != movie.genres.length ? ", " : ""))
                    }
                </p>
                <p className="movieDataVotes">
                    Vote: <span className={voteRank}>{movie.vote_average}</span> ({movie.vote_count} votes)
                </p>
                <p>
                    {movie.overview ?? "Missing description"}
                </p>
            </div>
        </div>
    );
}