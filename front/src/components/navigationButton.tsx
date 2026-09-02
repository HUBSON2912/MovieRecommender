import { useContext } from "react";
import "../css/navigation.css";
import { CurrentPageContext } from "../App";
import type { Page } from "../types";

export default function NavigationButton({ text }: { text: Page }) {
    const currentPage = useContext(CurrentPageContext);

    let componentClass: string = "navigationButton";
    if (currentPage.page == text) {
        componentClass = componentClass + " active";
    }

    return (
        <li className={componentClass} onClick={() => currentPage.setPage(text)}>
            {text}
        </li>
    );
}