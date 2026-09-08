import type { Movie } from "../types";
import "../css/movieCard.css";
import { Box, IconButton, Rating, Typography, type SxProps } from "@mui/material";
import type { Theme } from "@emotion/react";
import { useContext } from "react";
import { RatingsContext } from "../App";
import { Star } from "@mui/icons-material";
import ClearIcon from '@mui/icons-material/Clear';

export default function MovieCard({ movie }: { movie: Movie }) {
    const { ratings, setRatings, delRatings, getRate } = useContext(RatingsContext);
    const isRated = (): boolean => {
        // console.log(Boolean(getRate(movie.id)));
        return Boolean(getRate(movie.id));
    }



    return (
        <Box component="section" className="cardContainer" sx={style.cardContainer} >
            <img className="movieImage" height="400" src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`} alt="Cannot load the image" />
            <div className="movieData">
                <div className="movieDataHeader">
                    <Typography component="h2">
                        {movie.title}
                    </Typography>
                    <Typography>
                        {/* just year */}
                        ({movie.release_date.slice(0, 4)})
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
                        value={isRated() ? getRate(movie.id) : movie.vote_average / 2}  // movie has rating 0-10 and there are 5 stars
                        precision={0.1}
                        onChange={(e: React.SyntheticEvent, value: number | null) => {
                            if (value)
                                setRatings({ movieId: movie.id, rate: value });
                            else
                                delRatings(movie.id);
                            console.log(ratings);
                        }}
                        icon={isRated() ? <Star color="secondary" /> : <Star color="inherit" />}
                    />
                    {isRated() && <IconButton size="small"  onClick={()=>delRatings(movie.id)}><ClearIcon /></IconButton>}
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
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        alignContent: "center",
        gap: "15px"
    }
}