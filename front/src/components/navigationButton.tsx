import { useContext} from "react";
import "../css/navigation.css";
import { CurrentPageContext } from "../App";
import type { Page } from "../types";
import { Chip } from "@mui/material";

export default function NavigationButton({ text }: { text: Page }) {
    const currentPage = useContext(CurrentPageContext);

    // let componentClass: string = "navigationButton";
    // if (currentPage.page == text) {
    //     componentClass = componentClass + " active";
    // }

    const handleClick = (event: any) => {  // event isnt important here
        currentPage.setPage(text);
    }

    return (
        <Chip
            label={text}
            sx={{ cursor: "pointer", fontSize: 24, paddingX: "8px" }}
            variant={currentPage.page == text ? "filled" : "outlined"}
            color="primary"
            onClick={handleClick}
        />
    );
}