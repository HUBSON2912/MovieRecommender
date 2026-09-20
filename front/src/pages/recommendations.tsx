import { useEffect, useState } from "react";
import { getModelsList, getRecommendations, retrainNewModel, trainingStatus } from "../api/models";
import SelectList from "../components/selectList";
import { Box, Button, Paper, Typography, type SxProps } from "@mui/material";
import type { Theme } from "@mui/material/styles";
import { ServerIsBusyError, type Movie } from "../types";
import MovieList from "../components/movieList";
import { getSavedRatings } from "../api/localstorage";
import { MINIMAL_MOVIES_RATED_FOR_MODEL } from "../consts";
import SomethingWentWrong from "../components/sthWentWrong";
import LoadingCircle from "../components/loadingCircle";

export default function RecommendationsPage() {
    //errors
    const [isError, setIsError] = useState<boolean>(false);
    const [message, setMessage]=useState<string|null>(null);

    //loading animations
    const [loadingRecommendations, setLoadingRecommendations] = useState<boolean>(false);

    // selecting model
    const [modelNames, setModelNames] = useState<string[]>([]);
    const [selectedModel, setSelectedModel] = useState<string | null>(null);
    useEffect(() => {
        // load list of trained models
        getModelsList().then(res => setModelNames(res.sort())).catch(err => setIsError(true));
    }, []);

    // train new model logic
    const [isRetrainButtonDisabled, setIsRetrainButtonDisabled] = useState<boolean>(false);
    const handleRetrainNewButton = async () => {
        try {
            const isServerTraining = (await trainingStatus()) != "free";
            if (isServerTraining) {
                setMessage("Server is busy now.");
                return;
            }

            await retrainNewModel();
        }
        catch (err) {
            if (err instanceof ServerIsBusyError)
                setMessage("Server is busy now.");
            else
                setIsError(true);
        }
    };
    useEffect(() => {
        // disable button if no movies rated
        setIsRetrainButtonDisabled(getSavedRatings().length < MINIMAL_MOVIES_RATED_FOR_MODEL);
    }, []);

    // get recommendations logic
    const [recommendedMovies, setRecommendedMovies] = useState<Movie[]>([])
    const handleGetRecommendations = () => {
        if (!selectedModel)
            return;

        setLoadingRecommendations(true);

        getRecommendations(selectedModel)
            .then(res => setRecommendedMovies(res))
            .catch(() => setIsError(true))
            .finally(() => {
                setLoadingRecommendations(false);
            });
    }

    if (isError)
        return <SomethingWentWrong />

    return (
        <>
            <Box sx={styles.containerHeadText}>
                <Typography component="p">Select model that best fits to you and press RUN button. If you want to create a new model you must have at least {MINIMAL_MOVIES_RATED_FOR_MODEL} movies rated. Training a new model takes a while.</Typography>
                {message && <Typography>{message}</Typography>}
            </Box>
            <Box sx={styles.selectModelContainer}>
                <SelectList items={modelNames} onClickItem={setSelectedModel} selected={selectedModel} title={modelNames.length == 0 ? "No saved models" : "Select model"} />
                <Box sx={styles.buttonPanel}>
                    <Button
                        variant="outlined"
                        disabled={selectedModel == null}
                        loading={loadingRecommendations}
                        onClick={handleGetRecommendations}
                    >Run</Button>

                    <Button variant="outlined" disabled={isRetrainButtonDisabled} onClick={handleRetrainNewButton}>Retrain new</Button>
                </Box>
            </Box>

            {loadingRecommendations && <LoadingCircle />}
            <MovieList movies={recommendedMovies} />
        </>
    );
}

const styles: Record<string, SxProps<Theme>> = {
    containerHeadText: {
        width: 0.5,
        marginBottom: 3
    },
    selectModelContainer: {
        display: "flex",
        alignContent: "center",
        alignItems: "center",
        gap: 5
    },
    buttonPanel: {
        display: "flex",
        flexDirection: "column",
        gap: 2
    }
}