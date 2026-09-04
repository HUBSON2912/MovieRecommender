import type { Movie } from "../types";
import "../css/movieCard.css";
import { Box, Rating, Typography, type SxProps } from "@mui/material";
import type { Theme } from "@emotion/react";

export default function MovieCard({ movie, onRate }: { movie: Movie, onRate: (event: React.SyntheticEvent, value: number|null)=>void }) {
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
        <Box component="section" className="cardContainer" sx={style.cardContainer} >
            <img className="movieImage" height="400" src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`} alt="Cannot load the image" />
            <div className="movieData">
                <div className="movieDataHeader">
                    <Typography component="h2">
                        {movie.title}
                    </Typography>
                    <Typography>
                        ({movie.release_date.getFullYear()})
                    </Typography>
                </div>
                <Typography component="p" sx={style.movieDataInfo}>
                    {
                        movie.adult ? "ADULT, " : ""
                    }
                    {
                        movie.genres.map((gen, index) => gen + (index + 1 != movie.genres.length ? ", " : ""))
                    }
                </Typography>
                {/* <Typography component="p" sx={style.movieDataInfo}>
                    Vote: <Typography component="span" sx={{ fontSize: "18px" }} className={voteRank}>{movie.vote_average}</Typography> ({movie.vote_count} votes)
                </Typography> */}
                <Box sx={style.movieRating}>
                    <Rating 
                        name="vote" 
                        defaultValue={movie.vote_average/2}  // movie has rating 0-10 and there are 5 stars
                        precision={0.1}
                        onChange={onRate}
                        // todo if rated then secondary
                        // todo if rated then "clear" button
                    />
                    <Typography sx={style.movieDataInfo}>
                        ({movie.vote_count} votes)
                    </Typography>
                </Box>
                <Typography component="p" sx={style.movieDescription}>
                    {movie.overview ?? "Missing description"}
                </Typography>
            </div>
        </Box>
    );
}

const style: Record<string, SxProps<Theme>> = {
    cardContainer: {
        /* background-color: var(--md-sys-color-surface-bright); */
        backgroundColor: "background.paper",
        margin: "20px",
        flexDirection: "row",
        display: "flex",
        width: 0.6,
        /* border: 1px solid var(--md-sys-color-outline), */
        gap: "15px",
        borderRadius: 1
    },
    movieDataInfo: {
        margin: 0,
        padding: 0,
        fontSize: "18px",
    },
    movieDescription: {
        fontSize: "22px",
        marginTop: "15px"
    },
    movieRating: {
        display:"flex",
        flexDirection: "row",
        alignItems: "center",
        gap: "15px"
    }
}