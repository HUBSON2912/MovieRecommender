import { Box, Typography, type SxProps } from "@mui/material";
import type { Theme } from "@mui/material/styles";

export default function AboutPage() {
    return (
        <Box sx={styles.container}>
            <Typography component="p">
                Hi. <Typography component="a" sx={styles.link} href="https://github.com/HUBSON2912">This is me</Typography>. This is my summer project. The aim of this project was to learn more about machine learning and recommendation systems. During work I decided to implement is as API and create some frontend.
            </Typography>
            <Typography component="p">
                I learned that in real usage the model should be common for all the users. The real model should be retrained after every rate of any user (or periodically: every night, every week). I've built simplified service: users can create model for themself and choose agent that fits them best. Models are not retrained but user can order to train a new one having regard to their ratings.
            </Typography>
            <div>
                <Typography component="p">
                    Working on the project I learn something about:
                </Typography>
                <ul>
                    <Typography component="li">Funk SVD</Typography>
                    <Typography component="li">FastAPI</Typography>
                    <Typography component="li">Apache virtual hosts and reverse proxy</Typography>
                    <Typography component="li">TypeScript</Typography>
                    <Typography component="li">React + MaterialUI</Typography>
                    <Typography component="li">Unit tests in Python</Typography>
                </ul>
            </div>
        </Box>
    );
}

const styles: Record<string, SxProps<Theme>> = {
    container: {
        width: 0.6,
        display: "flex",
        flexDirection: "column",
        gap: 3
    },
    link: {
        color: "info.main"
    }
}