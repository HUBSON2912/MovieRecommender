import { Button, Typography } from "@mui/material";

export default function SomethingWentWrong({ onRefresh }: { onRefresh: () => void }) {
    return (
        <>
            <Typography component="p">SOMETHING WENT WRONG</Typography>
            <Button variant="outlined" onClick={onRefresh}>Refresh</Button>
        </>
    );
}