import { List, ListItem, ListSubheader, Paper, useTheme, type SxProps } from "@mui/material";

function ListElement({ label, onClick, selected }: { label: string, onClick: (val: string) => void, selected: boolean }) {
    const theme = useTheme();
    return (
        <ListItem
            onClick={() => onClick(label)}
            sx={{
                transition: theme.transitions.create(['background-color', 'transform']),
                borderTop: `2px ${theme.palette.divider} solid`,
                backgroundColor: selected ? theme.palette.grey[700] : theme.palette.background.paper
            }}
        > {label}</ListItem >
    );
}

export default function SelectList({ items, onClickItem, maxHeight = 200, title = null, selected }: { items: string[], onClickItem: (value: string) => void, maxHeight?: string | number, title?: string | null, selected: string | null }) {
    return (
        <Paper style={{ maxHeight: maxHeight, overflow: 'auto' }}>
            <List
                subheader={title ? <ListSubheader component="div">{title}</ListSubheader> : <></>}
            >
                {items.map((value) =>
                    <ListElement label={value} onClick={onClickItem} selected={value == selected} />
                )}
            </List>
        </Paper>
    );
}