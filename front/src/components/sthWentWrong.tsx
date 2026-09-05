import { Button, Typography } from "@mui/material";

export default function SomethingWentWrong({ onRefresh }: { onRefresh: () => void }) {
    return (
        <>
            <Typography component="p">Something went wrong</Typography>
            <Button variant="outlined" onClick={onRefresh}>Refresh</Button>
        </>
    );
}