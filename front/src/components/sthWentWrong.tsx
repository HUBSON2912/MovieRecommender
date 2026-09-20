import { Button, Typography } from "@mui/material";

function refreshPage() {
    window.location.reload();
}

export default function SomethingWentWrong() {
    return (
        <>
            <Typography component="p">Something went wrong</Typography>
            <Button variant="outlined" onClick={refreshPage} sx={{margin:2}}>Refresh</Button>
        </>
    );
}